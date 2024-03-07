from http.client import HTTPException
from typing import Dict, Any
from fastapi import HTTPException, Request

from app.endpoints.filter.Filter import Filter
from app.endpoints.filter.FilterFactory import COMPOSITE_FILTER_TYPE_TO_CLASS, FILTER_TYPE_TO_CLASS


def parse_filter(filter_dict: Dict[str, Any]) -> Filter:
    filter_type = filter_dict.get('type', '') + 'Filter'
    cls = FILTER_TYPE_TO_CLASS.get(filter_type)
    if cls:
        return cls(**{k: v for k, v in filter_dict.items() if k != 'type'})
    else:
        composite_cls = COMPOSITE_FILTER_TYPE_TO_CLASS.get(filter_type)
        if composite_cls:
            operands = [parse_filter(f) for f in filter_dict['operands']]
            return cls(operands=operands)
        else:
            raise ValueError(f"Unknown filter type: {filter_type}")

async def FilterParser(request: Request) -> Filter:
    json_data = await request.json()
    try:
        return parse_filter(json_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))