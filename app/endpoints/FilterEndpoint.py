from typing import List, Annotated

from fastapi import FastAPI
from fastapi.params import Body
from injector import inject

from app.Config import Config
from app.endpoints.Endpoint import Endpoint
from app.model.filter.AndOperationFilter import AndOperationFilter
from app.model.filter.HigherThanSizeFilter import HigherThanSizeFilter
from app.model.filter.LowerThanSizeFilter import LowerThanSizeFilter
from app.model.filter.MatchExtensionFilter import MatchExtensionFilter
from app.model.filter.OrOperationFilter import OrOperationFilter
from app.service.filter.FilterService import FilterService

Filter = AndOperationFilter | OrOperationFilter | HigherThanSizeFilter | LowerThanSizeFilter | MatchExtensionFilter


@inject
class FilterEndpoint(Endpoint):
    def __init__(self, filter_service: FilterService, config: Config) -> None:
        super().__init__()
        self.config = config
        self.filter_service = filter_service

    def register(self, app: FastAPI) -> None:
        app.post("/filter")(self.filter)

    async def filter(self, filter_request: Annotated[Filter, Body(...)]) -> List[str]:
        return self.filter_service.filter(filter_object=filter_request, path=self.config.shared_path)
