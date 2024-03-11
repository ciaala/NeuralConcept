from __future__ import annotations
from typing import Type, Dict

from app.model.filter.FilterBase import FilterBase
from app.model.filter.FilterBase import CompositeFilter

FILTER_TYPE_TO_CLASS: Dict[str, Type[FilterBase]] = {}
COMPOSITE_FILTER_TYPE_TO_CLASS: Dict[str, Type[CompositeFilter]] = {}


def register_filter(cls: Type[FilterBase]) -> Type[FilterBase]:
    FILTER_TYPE_TO_CLASS[cls.__name__] = cls
    return cls


def register_composite_filter(cls: Type[CompositeFilter]) -> Type[CompositeFilter]:
    COMPOSITE_FILTER_TYPE_TO_CLASS[cls.__name__] = cls
    return cls
