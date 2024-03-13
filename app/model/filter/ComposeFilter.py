from typing import List

from app.model.filter.Filter import Filter
from app.model.filter.FilterBase import FilterBase


class CompositeFilter(FilterBase):
    operands: List[Filter]