from dataclasses import dataclass

from app.model.filter.Filter import CompositeFilter
from app.model.filter.FilterFactory import register_composite_filter
from app.service.filesystem.FileSystemService import FileSystemItem


@register_composite_filter
@dataclass
class AndOperationFilter(CompositeFilter):

    def apply(self, item: FileSystemItem) -> bool:
        # Check if the item's filename ends with the specified extension
        for operand_filter in self.operands:
            if not operand_filter.apply(item):
                return False
        return True
