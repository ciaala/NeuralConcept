from http.client import HTTPException
from typing import Type, Callable
from fastapi import Depends, FastAPI, HTTPException, Request

from app.endpoints.filter.Filter import Filter, parse_filter


async def FilterParser(request: Request) -> Filter:
    json_data = await request.json()
    try:
        return parse_filter(json_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
