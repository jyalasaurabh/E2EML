import os
import sys

from sklearn.ensemble import AdaBoostRegressor, GradientBoostingRegressor, RandomForestRegressor
from src.logger import info_logger
from src.utils import evaluateModel, save_obj
from src.exception import CustomException
from dataclasses import dataclass
from catboost import CatBoostRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor


@dataclass
class ModelTrainConfig:
    train_model_file_path = os.path.join("artifacts", "mode.pkl")


class ModelTrainer:
    def __init__(self) -> None:
        self.model_trainer_config = ModelTrainConfig()

    def initiate_training(self, train_array, test_array):
        try:
            info_logger.info("splitting tarin/test data")
            x_train, y_train, x_test, y_test = (
                train_array[:, :-1],  # take last column
                train_array[:, -1],  # all rows except last
                test_array[:, :-1],  # take last column
                test_array[:, -1],  # all rows except last
            )
            models = {
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "k-Neighbours Classifier": KNeighborsRegressor(),
                "XGBClassifiers": XGBRegressor(),
                "CatBoosting Classifier": CatBoostRegressor(),
                "AdaBoost Classifier": AdaBoostRegressor()
            }
            model_report = evaluateModel(
                x_train, y_train, x_test, y_test, models)

            # to get best model from dict
            best_model_score = max(sorted(model_report.values()))

            # to get best model name from dict
            best_model_name = list(model_report.keys())[list(
                model_report.values()).index(best_model_score)]

            best_model = models[best_model_name]

            if best_model_score < 0.6:
                raise CustomException("No best model found")

            info_logger.info("best model found on train/test")

            save_obj(self.model_trainer_config.train_model_file_path,
                     obj=best_model)

            predict = best_model.predict(x_test)

            r2_square = r2_score(y_test, predict)
            return r2_square

        except Exception as e:
            raise CustomException(e, sys)
