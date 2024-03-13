from __future__ import annotations

from typing import Literal, List, Annotated, Union

from pydantic import Field


from app.model.filter.AndOperationFilter import AndOperationFilter
from app.model.filter.LowerThanSizeFilter import LowerThanSizeFilter
from app.model.filter.FilterBase import FilterBase
from app.model.filter.HigherThanSizeFilter import HigherThanSizeFilter
from app.model.filter.MatchExtensionFilter import MatchExtensionFilter
from app.service.filesystem.FileSystemItem import FileSystemItem


class OrOperationFilter(FilterBase):
    type: Literal['OrOperation'] = Field("OrOperation", frozen=True)
    operands: List[Filter]
    def apply(self, item: FileSystemItem) -> bool:
        # Check if the item's filename ends with the specified extension
        for operand_filter in self.operands:
            if operand_filter.apply(item):
                return True
        return False

Filter = Annotated[
    Union[AndOperationFilter, OrOperationFilter, HigherThanSizeFilter, LowerThanSizeFilter, MatchExtensionFilter],
    Field(discriminator='type')]

AndOperationFilter.update_forward_refs()