import json

import pytest

from app.model.filter.AndOperationFilter import AndOperationFilter
from app.endpoints.filter.FilterParser import parse_filter
from app.model.filter.HigherSizeFilter import HigherSizeFilter
from app.model.filter.LowerSizeFilter import LowerSizeFilter
from app.model.filter.MatchExtensionFilter import MatchExtensionFilter
from app.model.filter.OrOperationFilter import OrOperationFilter


def test_filter_parser() -> None:
    # GIVEN
    # A filter in JSon structure
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
    json_as_dict = json.loads(json_data)
    # WHEN parsed
    top_level_filter = parse_filter(json_as_dict)
    # Then it matches the structure
    assert(isinstance(top_level_filter, OrOperationFilter))
    assert(isinstance(top_level_filter.operands[0], LowerSizeFilter))
    assert(top_level_filter.operands[0].size == 1024)
    assert (isinstance(top_level_filter.operands[1], AndOperationFilter))
    and_op = top_level_filter.operands[1]
    assert (isinstance(and_op.operands[0], HigherSizeFilter))
    assert(and_op.operands[0].size == 512)
    assert (isinstance(and_op.operands[1], MatchExtensionFilter))
    assert(and_op.operands[1].extension == 'txt')


def test_parser_fails_with_not_existent_filter() -> None:
    # GIVEN
    # A filter in JSon structure
    json_data = '''
    {
        "type": "NotOperation",
        "operands": [
            {"type": "LowerSize", "size": 1024}
        ]
    }
    '''
    json_as_dict = json.loads(json_data)
    # WHEN parsed
    with pytest.raises(ValueError) as excinfo:
        parse_filter(json_as_dict)
    assert str(excinfo.value) == 'Unknown filter type: NotOperation'


def test_parser_fails_with_invalid_json_content() -> None:
    # GIVEN
    # A filter in JSon structure
    json_data = '''
    {
        "whatever": "something"
    }
    '''
    json_as_dict = json.loads(json_data)
    # WHEN parsed
    with pytest.raises(ValueError) as excinfo:
        parse_filter(json_as_dict)
    assert str(excinfo.value) == 'The json content does not match a filter definition'