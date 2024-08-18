import logging

class LoggingMixin:
    """
    Service mixin class to write logs into file.
    """
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.DEBUG)
        file_handler = logging.FileHandler(f"iphone_store/logs_{self.__class__.__name__}.log")
        file_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def log_debug(self, message: str):
        self.logger.debug(message)

    def log_info(self, message: str):
        self.logger.info(message)

    def log_warning(self, message: str):
        self.logger.warning(message)

    def log_error(self, message: str):
        self.logger.error(message)

    def log_critical(self, message: str):
        self.logger.critical(message)