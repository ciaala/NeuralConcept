import os
from typing import List

from app.model.filter.Filter2 import FilterBase
from app.service.filesystem.FileSystemItem import FileSystemItem


class FilteringFileSystemService:
    def filter(self, filter_object: FilterBase, path: str) -> List[str]:
        files: List[str] = []
        for entry in os.listdir(path):
            full_path = os.path.join(path, entry)
            if os.path.isfile(full_path):
                # os.path.getsize gets the size of the file
                size = os.path.getsize(full_path)
                item = FileSystemItem(filename=entry, size=size)
                if filter_object.apply(item):
                    files.append(item.filename)
        return files
