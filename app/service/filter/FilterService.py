from typing import List

from injector import inject

from app.model.filter.Filter import Filter
from app.service.filesystem.FileSystemService import FileSystemService


@inject
class FilterService:
    def __init__(self, filesystem_service: FileSystemService) -> None:
        self.filesystem_service = filesystem_service

    def filter(self, filter_object: Filter, path: str) -> List[str]:
        response: List[str] = []
        for file in self.filesystem_service.list(path):
            if filter_object.apply(file):
                response.append(file.filename)
        return response
