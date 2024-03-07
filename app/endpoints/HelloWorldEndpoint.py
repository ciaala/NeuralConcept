from fastapi import FastAPI
from fastapi.openapi.models import Response

from app.endpoints.Endpoint import Endpoint


class HelloWorld(Endpoint):
    def __init__(self):
        super().__init__()

    def register(self, app: FastAPI) -> None:
        app.get("/")(self.process)

    def process(self) -> str:
        return "Hello World! from the Cloud Service Application"
