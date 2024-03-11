from pydantic import Field

from app.model.filter.FilterBase import CompositeFilter
from app.model.filter.FilterFactory import register_composite_filter
from app.service.filesystem.FileSystemItem import FileSystemItem


@register_composite_filter
class OrOperationFilter(CompositeFilter):
    type: str = Field("OrOperation", frozen=True)

    def apply(self, item: FileSystemItem) -> bool:
        # Check if the item's filename ends with the specified extension
        for operand_filter in self.operands:
            if operand_filter.apply(item):
                return True
        return False
