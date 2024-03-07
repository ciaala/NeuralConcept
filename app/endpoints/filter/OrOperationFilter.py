from dataclasses import dataclass
from typing import List

from app.endpoints.filter.Filter import Filter
from app.endpoints.filter.FilterFactory import register_composite_filter
from app.service.filesystem.FileSystemService import FileSystemItem


@register_composite_filter
@dataclass
class OrOperationFilter(Filter):
    operands: List[Filter]

    def apply(self, item: FileSystemItem) -> bool:
        # Check if the item's filename ends with the specified extension
        for operand_filter in self.operands:
            if operand_filter.apply(item):
                return True
        return False
