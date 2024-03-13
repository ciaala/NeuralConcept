from typing import Literal

from pydantic import Field

from app.model.filter.FilterBase import FilterBase
from app.service.filesystem.FileSystemItem import FileSystemItem


class HigherThanSizeFilter(FilterBase):
    type: Literal['HigherThanSize'] = Field("HigherThanSize", frozen=True)
    size: int

    def apply(self, item: FileSystemItem) -> bool:
        return item.size > self.size
