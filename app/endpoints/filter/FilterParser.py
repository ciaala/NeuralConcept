from typing import Dict, Any

from fastapi import HTTPException, Request

from app.model.filter.Filter import Filter, CompositeFilter
from app.model.filter.FilterFactory import COMPOSITE_FILTER_TYPE_TO_CLASS, FILTER_TYPE_TO_CLASS


def parse_filter(filter_dict: Dict[str, Any]) -> Filter:
    filter_type = filter_dict.get('type', '')
    filter_class = filter_type + 'Filter' if filter_type else ''
    cls = FILTER_TYPE_TO_CLASS.get(filter_class)
    if cls:
        filter = cls(**{k: v for k, v in filter_dict.items() if k != 'type'})
        if isinstance(filter, Filter):
            return filter
        else:
            raise ValueError(f"Unknown object type: {type(filter).__name__}")

    composite_cls = COMPOSITE_FILTER_TYPE_TO_CLASS.get(filter_class)
    if composite_cls:
        operands = [parse_filter(f) for f in filter_dict['operands']]
        composite_filter = composite_cls(operands=operands)
        if isinstance(composite_filter, CompositeFilter):
            return composite_filter
        else:
            raise ValueError(f"Unknown object type: {type(composite_filter).__name__}")
    else:
        if filter_type:
            raise ValueError(f'Unknown filter type: {filter_type}')
        else:
            raise ValueError('The json content does not match a filter definition')


async def FilterParser(request: Request) -> Filter:
    json_data = await request.json()
    try:
        return parse_filter(json_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
