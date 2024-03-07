from typing import List, Type, Callable
from fastapi import Depends, FastAPI, HTTPException, Request

from fastapi import FastAPI
from fastapi.params import Body
from injector import inject
from pydantic import BaseModel

from app.Config import Config
from app.endpoints.Endpoint import Endpoint
from app.endpoints.filter.Filter import Filter, OrOperationFilter, AndOperationFilter, HigherSizeFilter, \
    LowerSizeFilter, MatchExtensionFilter
from app.endpoints.filter.FilterParser import FilterParser
from app.service.filter.FilterService import FilterService


@inject
class FilterEndpoint(Endpoint):
    def __init__(self, filter_service: FilterService, config: Config) -> None:
        super().__init__()
        self.config = config
        self.data = ["abc", "def", "ghi"]
        self.filter_service = filter_service

    def register(self, app: FastAPI) -> None:
        app.post("/filter")(self.process)

    async def process(self,
                      filter_request: AndOperationFilter | OrOperationFilter | HigherSizeFilter | LowerSizeFilter |
                                      MatchExtensionFilter = Depends(FilterParser)) -> List[str]:
        return self.filter_service.filter(filter=filter_request, path=self.config.shared_path)
