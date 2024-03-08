import logging
from logging import Logger
from typing import Type, Any

from injector import singleton


@singleton
class LoggerFactory:
    def __init__(self) -> None:
        logging.basicConfig(
            format='%(asctime)s [%(levelname)s] [%(name)s] [%(filename)s:%(lineno)d] %(message)s',
            level=logging.INFO,
        )

    def get_logger(self, cls: Type[Any] | None) -> Logger:
        if cls:
            return logging.getLogger(cls.__name__)
        else:
            return logging.getLogger()
