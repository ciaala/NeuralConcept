from __future__ import annotations

from typing import List, Dict

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from pydantic import ValidationError


class FilterBase(BaseModel):
    filter_type: str


class LowerThanSize(FilterBase):
    filter_type: str = Field("LowerThanSize", frozen=True)
    size: int


class HigherThanSize(FilterBase):
    filter_type: str = Field("HigherThanSize", frozen=True)
    size: int


class MatchFileExtension(FilterBase):
    filter_type: str = Field("MatchFileExtension", frozen=True)
    extension: str


class AndOperation(FilterBase):
    filter_type: str = Field("AndOperation", frozen=True)
    filters: List[Filter]


class OrOperation(FilterBase):
    filter_type: str = Field("OrOperation", frozen=True)
    filters: List[Filter]


Filter = LowerThanSize | HigherThanSize | MatchFileExtension | AndOperation | OrOperation

AndOperation.update_forward_refs()
OrOperation.update_forward_refs()
app = FastAPI()

class FilterResponse:
    message: str = Field("Filter processed successfully", description="Type of message")
    filter: str
@app.post("/filter")
async def filter_endpoint(filter: Filter) -> Dict[str, str]:
    try:
        if filter.filter_type == "LowerThanSize":
            # process LowerThanSize filter
            pass
        elif filter.filter_type == "HigherThanSize":
            # process HigherThanSize filter
            pass
        elif filter.filter_type == "MatchFileExtension":
            # process MatchFileExtension filter
            pass
        elif filter.filter_type == "AndOperation":
            # process AndOperation filter
            pass
        elif filter.filter_type == "OrOperation":
            # process OrOperation filter
            pass
        else:
            raise HTTPException(status_code=400, detail="Unsupported filter type")
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(e))
    response = {"message": "Filter processed successfully", "filter": str(filter)}
    print(response)
    return response
