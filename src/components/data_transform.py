import sys
import os
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.exception import CustomException
from src.logger import logging
from src.utils import save_obj


@dataclass
class DataTransformConfig:
    preprocessor_obj_file_path = os.path.join("artifacts", "preprocessor.pkl")


class DataTranform:
    def __init__(self) -> None:
        self.data_transform_config = DataTransformConfig()

    def get_data_transformer(self):
        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = ["gender", "race_ethnicity",
                                   "parental_level_of_education", "lunch", "test_preparation_course"]
            num_pipeline = Pipeline(
                steps=[("imputer", SimpleImputer(stratergy="median")),
                       ("scalar", StandardScaler())]
            )
            cat_pipeline = Pipeline(
                steps=[("imputer", SimpleImputer(strategy="most_frequent"))
                       ("one_hot_encoder", OneHotEncoder())
                       ("scalar", StandardScaler())
                       ]
            )
            logging.info("Categorical/numerical Encoding Completed")

            preprocessor = ColumnTransformer([
                ("num_pipeline", num_pipeline, numerical_columns),
                ("cat_pipeline", cat_pipeline, categorical_columns),
            ])

            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_transform(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("reading of train test data completed")

            preprocessor_obj = self.get_data_transformer()
            logging.info("pipeline preprocessor completed")

            target_column_name = "math_score"
            numerical_columns = ["writing_score", "reading_score"]

            input_feature_train_df = train_df.drop(
                columns=[target_column_name], axis=1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(
                columns=[target_column_name], axis=1)
            target_feature_test_df = test_df[target_column_name]

            input_feature_train_arr = preprocessor_obj.fit_transform(
                input_feature_train_df)
            input_feature_test_arr = preprocessor_obj.transform(
                input_feature_test_df)

            train_arr = np.c_[input_feature_train_arr,
                              np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr,
                             np.array(target_feature_test_df)]

            save_obj(
                file_path=self.data_transform_config.preprocessor_obj_file_path,
                obj=preprocessor_obj

            )

            return {
                train_arr,
                test_arr,
                self.data_transform_config.preprocessor_obj_file_path
            }

        except Exception as e:
            raise CustomException(e, sys)
