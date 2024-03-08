import os

from injector import inject

from app.logger.LoggerFactory import LoggerFactory


@inject
class Config:

    def __init__(self, logger_factory: LoggerFactory) -> None:
        self.logger = logger_factory.get_logger(Config)
        self.shared_path = os.getenv('SHARED_PATH', ".")
        absolute_path = os.path.abspath(self.shared_path)
        self.logger.info(f"Shared path: {self.shared_path} (={absolute_path})")
