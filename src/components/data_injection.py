import os
import sys
from src.logger import info_logger
from src.exception import CustomException
from src.components.data_transform import DataTranform
from src.components.model_train import ModelTrainer

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass
class DataInjectionConfig:
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")
    raw_data_path: str = os.path.join("artifacts", "data.csv")


class DataInjection:
    def __init__(self) -> None:
        self.injection_config = DataInjectionConfig()

    def initiate_data_injection(self):
        info_logger.info("Entered data injection method")
        try:
            df = pd.read_csv("notebook/data/stud.csv")
            info_logger.info(
                "Data Read successfull/ Read dataset as dataframe")
            os.makedirs(os.path.dirname(
                self.injection_config.train_data_path), exist_ok=True)
            df.to_csv(self.injection_config.raw_data_path,
                      index=False, header=True)
            info_logger.info("Train test split initiated")
            train_set, test_set = train_test_split(
                df, test_size=0.2, random_state=42)

            train_set.to_csv(self.injection_config.train_data_path,
                             index=False, header=True)
            test_set.to_csv(self.injection_config.test_data_path,
                            index=False, header=True)
            info_logger.info("Train test split completed")

            return (self.injection_config.train_data_path,
                    self.injection_config.test_data_path)
        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    obj = DataInjection()
    train_path, test_path = obj.initiate_data_injection()
    data_transform = DataTranform()
    train_array, test_array, _ = data_transform.initiate_data_transform(
        train_path, test_path)
    model_trainer = ModelTrainer()
    print(model_trainer.initiate_training(train_array, test_array))
