import uvicorn
from fastapi import FastAPI
from injector import inject

from app.endpoints.Endpoint import Endpoint


@inject
class RestAPIServer:
    def __init__(self, app: FastAPI) -> None:
        self.app = app

    def register_endpoint(self, endpoint: Endpoint) -> None:
        endpoint.register(self.app)

    def start(self) -> None:
        uvicorn.run(self.app, host="0.0.0.0", port=8000)
