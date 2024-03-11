from pydantic import Field

from app.model.filter.FilterBase import FilterBase
from app.model.filter.FilterFactory import register_filter
from app.service.filesystem.FileSystemService import FileSystemItem


@register_filter
class LowerThanSizeFilter(FilterBase):
    type: str = Field("LowerThanSize", frozen=True)
    size: int

    def apply(self, item: FileSystemItem) -> bool:
        return item.size < self.size
