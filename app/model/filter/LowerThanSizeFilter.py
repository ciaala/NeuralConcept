from typing import Literal

from pydantic import Field

from app.model.filter.FilterBase import FilterBase
from app.service.filesystem.FileSystemItem import FileSystemItem


class LowerThanSizeFilter(FilterBase):
    type: Literal['LowerThanSize'] = Field("LowerThanSize", frozen=True)
    size: int

    def apply(self, item: FileSystemItem) -> bool:
        return item.size < self.size
