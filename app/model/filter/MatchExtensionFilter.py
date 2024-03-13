from typing import Literal

from pydantic import Field

from app.model.filter.FilterBase import FilterBase
from app.service.filesystem.FileSystemItem import FileSystemItem


class MatchExtensionFilter(FilterBase):
    type: Literal['MatchExtension'] = Field("MatchExtension", frozen=True)
    extension: str

    def apply(self, item: FileSystemItem) -> bool:
        # Check if the item's filename ends with the specified extension
        return item.filename.endswith(self.extension)
