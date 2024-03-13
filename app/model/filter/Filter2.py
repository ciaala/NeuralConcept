from __future__ import annotations

from typing import Literal, List, Annotated, Union

from pydantic import Field
from pydantic import BaseModel
from app.service.filesystem.FileSystemItem import FileSystemItem

class FilterBase(BaseModel):
    type: str

    def apply(self, item: FileSystemItem) -> bool:
        raise NotImplementedError("Must be implemented by subclass")

class LowerThanSizeFilter(FilterBase):
    type: Literal['LowerThanSize'] = Field("LowerThanSize", frozen=True)
    size: int

    def apply(self, item: FileSystemItem) -> bool:
        return item.size < self.size

class HigherThanSizeFilter(FilterBase):
    type: Literal['HigherThanSize'] = Field("HigherThanSize", frozen=True)
    size: int

    def apply(self, item: FileSystemItem) -> bool:
        return item.size > self.size
class OrOperationFilter(FilterBase):
    type: Literal['OrOperation'] = Field("OrOperation", frozen=True)
    operands: List[Filter]
    def apply(self, item: FileSystemItem) -> bool:
        # Check if the item's filename ends with the specified extension
        for operand_filter in self.operands:
            if operand_filter.apply(item):
                return True
        return False

class MatchExtensionFilter(FilterBase):
    type: Literal['MatchExtension'] = Field("MatchExtension", frozen=True)
    extension: str

    def apply(self, item: FileSystemItem) -> bool:
        # Check if the item's filename ends with the specified extension
        return item.filename.endswith(self.extension)

class AndOperationFilter(FilterBase):
    type: Literal['AndOperation'] = Field("AndOperation", frozen=True)
    operands: List[Filter]

    def apply(self, item: FileSystemItem) -> bool:
        # Check if the item's filename ends with the specified extension
        for operand_filter in self.operands:
            if not operand_filter.apply(item):
                return False
        return True



Filter = Annotated[
    Union[AndOperationFilter, OrOperationFilter, HigherThanSizeFilter, LowerThanSizeFilter, MatchExtensionFilter],
    Field(discriminator='type')]