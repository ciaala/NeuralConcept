from typing import List

from fastapi import FastAPI
from injector import inject

from app.Config import Config
from app.endpoints.Endpoint import Endpoint
from app.model.filter.Filter2 import Filter
from app.service.filter.FilteringFileSystemService import FilteringFileSystemService

@inject
class FilterEndpoint(Endpoint):
    def __init__(self, filter_service: FilteringFileSystemService, config: Config) -> None:
        super().__init__()
        self.config = config
        self.filter_service = filter_service

    def register(self, app: FastAPI) -> None:
        app.post("/filter")(self.filter)

    async def filter(self, filter_request: Filter) -> List[str]:
        return self.filter_service.filter(filter_object=filter_request, path=self.config.shared_path)
