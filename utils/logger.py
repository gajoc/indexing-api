import logging
from functools import wraps


class GeneiLogger:

    _file_handler = None

    @classmethod
    def set_logger(cls, file_name):
        cls._file_handler = logging.FileHandler(file_name)
        message_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        cls._file_handler.setFormatter(message_format)

    @classmethod
    def get_logger(cls, name):
        logger = logging.getLogger(name)
        logger.addHandler(cls._file_handler)
        return logger


def log_exception(logger_name):
    """GeneiLogger needs to be set before use"""
    def inner_decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logger = GeneiLogger.get_logger(logger_name)
                logger.exception(e)
                raise
        return wrapper
    return inner_decorator
