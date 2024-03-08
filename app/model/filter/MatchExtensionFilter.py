from dataclasses import dataclass

from app.model.filter.Filter import Filter
from app.model.filter.FilterFactory import register_filter
from app.service.filesystem.FileSystemService import FileSystemItem


@register_filter
@dataclass
class MatchExtensionFilter(Filter):
    extension: str

    def apply(self, item: FileSystemItem) -> bool:
        # Check if the item's filename ends with the specified extension
        return item.filename.endswith(self.extension)
