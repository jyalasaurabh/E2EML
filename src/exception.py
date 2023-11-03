import sys
from src.logger import logging

def error_message(error,details:sys):
    _,_,exc_tb=details.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error Occured: [{0}] line number: [{1}] Error Message: [{2}]".format(file_name,exc_tb.tb_lineno,str(error))
    return error_message

class CustomException(Exception):
    def __init__(self, error,details:sys): 
        super().__init__(error)
        self.error_message=error_message(error,details)

    def __str__(self) -> str:
        return self.error_message
    