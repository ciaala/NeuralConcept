from __future__ import annotations

from typing import Literal, List, Annotated, Union

from pydantic import Field

from app.model.filter.FilterBase import FilterBase
from app.model.filter.HigherThanSizeFilter import HigherThanSizeFilter
from app.model.filter.LowerThanSizeFilter import LowerThanSizeFilter
from app.model.filter.MatchExtensionFilter import MatchExtensionFilter
from app.model.filter.OrOperationFilter import OrOperationFilter
from app.service.filesystem.FileSystemItem import FileSystemItem


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

AndOperationFilter.update_forward_refs()
