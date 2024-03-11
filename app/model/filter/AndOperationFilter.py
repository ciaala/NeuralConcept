from typing import List

from pydantic import Field

from app.model.filter.FilterBase import CompositeFilter, FilterBase
from app.model.filter.FilterFactory import register_composite_filter
from app.service.filesystem.FileSystemService import FileSystemItem


@register_composite_filter
class AndOperationFilter(CompositeFilter):
    type: str = Field("AndOperation", frozen=True)

    def apply(self, item: FileSystemItem) -> bool:
        # Check if the item's filename ends with the specified extension
        for operand_filter in self.operands:
            if not operand_filter.apply(item):
                return False
        return True
