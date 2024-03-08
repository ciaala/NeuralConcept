from injector import singleton, inject

from app.endpoints.FilterEndpoint import FilterEndpoint
from app.endpoints.HelloWorldEndpoint import HelloWorld
from app.logger.LoggerFactory import LoggerFactory
from app.server.server import RestAPIServer


@singleton
@inject
class Application:
    def __init__(self,
                 server: RestAPIServer,
                 filter_files: FilterEndpoint,
                 hello_world: HelloWorld,
                 logger_factory: LoggerFactory):
        self.logger = logger_factory.get_logger(Application)
        self.server = server
        self.server.register_endpoint(filter_files)
        self.server.register_endpoint(hello_world)

    def start(self) -> None:
        self.logger.info("Starting")
        self.server.start()
