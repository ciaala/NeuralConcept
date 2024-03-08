from dataclasses import dataclass

from app.model.filter.Filter import Filter
from app.model.filter.FilterFactory import register_filter
from app.service.filesystem.FileSystemService import FileSystemItem


@register_filter
@dataclass
class HigherSizeFilter(Filter):
    size: int

    def apply(self, item: FileSystemItem) -> bool:
        return item.size > self.size
