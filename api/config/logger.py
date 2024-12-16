"""
Docstring
"""
import os
from logging.handlers import RotatingFileHandler
import logging

import api.config.settings

class Logger:
    """
    Docstring
    """
    @staticmethod
    def get_logger(name: str,
                   log_file: str = "api.log",
                   level: int = logging.DEBUG):
        """
        Docstring
        :param name:
        :param log_file:
        :param level:
        :return:
        """
        # Ensure the directory for the log file exists
        log_dir = os.path.dirname(api.config.settings.LOG_DIR)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir)
        # Create a logger
        logger = logging.getLogger(name)
        logger.setLevel(level)
        # Avoid adding handlers multiple times
        if not logger.handlers:
            # Create a file handler with rotation
            file_handler = RotatingFileHandler(log_file,
                                               maxBytes=5 * 1024 * 1024,
                                               backupCount=3)
            file_handler.setLevel(level)

            # Create a console handler
            console_handler = logging.StreamHandler()
            console_handler.setLevel(level)

            # Define log format
            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
            file_handler.setFormatter(formatter)
            console_handler.setFormatter(formatter)

            # Add handlers to the logger
            logger.addHandler(file_handler)
            logger.addHandler(console_handler)


        return logger
