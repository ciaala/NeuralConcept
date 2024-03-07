from dataclasses import dataclass

from app.endpoints.filter.Filter import Filter
from app.endpoints.filter.FilterFactory import register_filter
from app.service.filesystem.FileSystemService import FileSystemItem


@register_filter
@dataclass
class HigherSizeFilter(Filter):
    size: int

    def apply(self, item: FileSystemItem) -> bool:
        return item.size > self.size
