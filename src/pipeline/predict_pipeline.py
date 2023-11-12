import sys
from src.exception import CustomException
from src.logger import info_logger
from src.utils import load_object

import pandas as pd


class PredictPipeline:
    def __init__(self) -> None:
        pass

    def predict(self, features):
        try:
            model_path = "artifacts\model.pkl"
            preprocessor_path = "artifacts\preprocessor.pkl"
            model = load_object(model_path)
            preprocessor = load_object(preprocessor_path)
            data_scale = preprocessor.transform(features)
            return model.predict(data_scale)
        except Exception as e:
            raise CustomException(e, sys)


class CustomData:
    def __init__(self, gender: str, race_ethnicity: str,
                 parental_level_education, lunch: str,
                 test_prep_course: str, reading_score: int,
                 writing_score: int) -> None:
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_education = parental_level_education
        self.lunch = lunch
        self.test_prep_course = test_prep_course
        self.reading_score = reading_score
        self.writing_score = writing_score

    def getDataFrame(self):
        try:
            custom_dic = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_prep_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score]
            }
            return pd.DataFrame(custom_dic)
        except Exception as e:
            raise CustomException(e, sys)
