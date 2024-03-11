from typing import List

from pydantic import BaseModel

from app.service.filesystem.FileSystemService import FileSystemItem


class FilterBase(BaseModel):
    type: str

    def apply(self, item: FileSystemItem) -> bool:
        raise NotImplementedError("Must be implemented by subclass")


class CompositeFilter(FilterBase):
    operands: List[FilterBase]
