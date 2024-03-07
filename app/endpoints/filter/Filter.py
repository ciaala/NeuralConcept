import json
from dataclasses import dataclass
from typing import Type, Dict, List, Any

from pydantic import BaseModel

from app.service.filesystem.FileSystemService import FileSystemItem

FILTER_TYPE_TO_CLASS: Dict[str, Type['Filter']] = {}


def register_filter(cls: Type['Filter']) -> Type['Filter']:
    FILTER_TYPE_TO_CLASS[cls.__name__] = cls
    return cls


@dataclass
class Filter:
    pass

    def apply(self, item: FileSystemItem) -> bool:
        raise NotImplementedError("Must be implemented by subclass")


# Specific filter types
@register_filter
@dataclass
class LowerSizeFilter(Filter):
    size: int

    def apply(self, item: FileSystemItem) -> bool:
        return item.size < self.size


@register_filter
@dataclass
class HigherSizeFilter(Filter):
    size: int

    def apply(self, item: FileSystemItem) -> bool:
        return item.size > self.size


@register_filter
@dataclass
class MatchExtensionFilter(Filter):
    extension: str

    def apply(self, item: FileSystemItem) -> bool:
        # Check if the item's filename ends with the specified extension
        return item.filename.endswith(self.extension)


@register_filter
@dataclass
class OrOperationFilter(Filter):
    operands: List[Filter]

    def apply(self, item: FileSystemItem) -> bool:
        # Check if the item's filename ends with the specified extension
        for operand_filter in self.operands:
            if operand_filter.apply(item):
                return True
        return False


@register_filter
@dataclass
class AndOperationFilter(Filter):
    operands: List[Filter]
    def apply(self, item: FileSystemItem) -> bool:
        # Check if the item's filename ends with the specified extension
        for operand_filter in self.operands:
            if not operand_filter.apply(item):
                return False
        return True

def parse_filter(filter_dict: Dict[str, Any]) -> Filter:
    filter_type = filter_dict.get('type', '') + 'Filter'
    cls = FILTER_TYPE_TO_CLASS.get(filter_type)
    if not cls:
        raise ValueError(f"Unknown filter type: {filter_type}")

    if issubclass(cls, (OrOperationFilter, AndOperationFilter)):
        operands = [parse_filter(f) for f in filter_dict['operands']]
        return cls(operands=operands)
    else:
        return cls(**{k: v for k, v in filter_dict.items() if k != 'type'})


if __name__ == '__main__':
    json_data = '''
    {
        "type": "OrOperation",
        "operands": [
            {"type": "LowerSize", "size": 1024},
            {"type": "AndOperation", "operands": [
                {"type": "HigherSize", "size": 512},
                {"type": "MatchExtension", "extension": "txt"}
            ]}
        ]
    }
    '''

    # Parse the JSON data
    top_level_filter = parse_filter(json.loads(json_data))

    # Demonstrating the parsed structure
    print(json.dumps(top_level_filter))
