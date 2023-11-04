import logging
import os

from datetime import datetime


def setupLogger(name, level=logging.INFO):
    str_level = "info"
    if level == logging.ERROR:
        str_level = "error"

    LOG_FOlDER = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}"
    LOG_FILE_NAME = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}_{str_level}.log"
    LOG_PATH = os.path.join(os.getcwd(), "Logs", LOG_FOlDER)
    os.makedirs(LOG_PATH, exist_ok=True)
    LOG_FILE_PATH = os.path.join(LOG_PATH, LOG_FILE_NAME)
    handler = logging.FileHandler(LOG_FILE_PATH)
    handler.setFormatter(logging.Formatter(
        "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"))
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger

info_logger = setupLogger("basic_logger")
error_logger = setupLogger("error_logger", level=logging.ERROR)
