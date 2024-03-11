from dataclasses import dataclass


@dataclass
class FileSystemItem:
    filename: str
    size: int
