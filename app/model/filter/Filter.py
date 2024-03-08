import json
from dataclasses import dataclass
from typing import List

from app.service.filesystem.FileSystemService import FileSystemItem


@dataclass
class Filter:
    def apply(self, item: FileSystemItem) -> bool:
        raise NotImplementedError("Must be implemented by subclass")


@dataclass
class CompositeFilter(Filter):
    operands: List[Filter]
