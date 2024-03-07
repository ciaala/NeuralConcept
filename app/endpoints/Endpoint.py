from abc import ABC

from fastapi import FastAPI


class Endpoint(ABC):

    def register(self, app: FastAPI) -> None:
        # register a function with the app
        raise NotImplementedError("Endpoint subclasses must implement register method")
