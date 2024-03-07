from injector import singleton, inject

from app.endpoints.FilterEndpoint import FilterEndpoint
from app.endpoints.HelloWorldEndpoint import HelloWorld
from app.server.server import RestAPIServer


@singleton
@inject
class Application:
    def __init__(self,
                 server: RestAPIServer,
                 filter_files: FilterEndpoint,
                 hello_world: HelloWorld):
        self.server = server
        self.server.register_endpoint(filter_files)
        self.server.register_endpoint(hello_world)

    def start(self) -> None:
        self.server.start()
