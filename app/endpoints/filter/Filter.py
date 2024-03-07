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


# Specific filter types




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
