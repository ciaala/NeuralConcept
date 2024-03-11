from pydantic import Field

from app.model.filter.FilterBase import FilterBase
from app.model.filter.FilterFactory import register_filter
from app.service.filesystem.FileSystemItem import FileSystemItem


@register_filter
class MatchExtensionFilter(FilterBase):
    type: str = Field("MatchFileExtension", frozen=True)
    extension: str

    def apply(self, item: FileSystemItem) -> bool:
        # Check if the item's filename ends with the specified extension
        return item.filename.endswith(self.extension)
