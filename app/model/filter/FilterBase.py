from typing import List

from pydantic import BaseModel

from app.service.filesystem.FileSystemItem import FileSystemItem


class FilterBase(BaseModel):
    type: str

    def apply(self, item: FileSystemItem) -> bool:
        raise NotImplementedError("Must be implemented by subclass")



