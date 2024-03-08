import os
from dataclasses import dataclass
from typing import List


@dataclass
class FileSystemItem:
    filename: str
    size: int


class FileSystemService:

    def list(self, path: str) -> List[FileSystemItem]:
        items = []
        for entry in os.listdir(path):
            full_path = os.path.join(path, entry)
            if os.path.isfile(full_path):
                # os.path.getsize gets the size of the file
                size = os.path.getsize(full_path)
                item = FileSystemItem(filename=entry, size=size)
                items.append(item)
        return items
