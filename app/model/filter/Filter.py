from __future__ import annotations

from typing import Annotated

from pydantic import Field

from app.model.filter.AndOperationFilter import AndOperationFilter
from app.model.filter.HigherThanSizeFilter import HigherThanSizeFilter
from app.model.filter.LowerThanSizeFilter import LowerThanSizeFilter
from app.model.filter.MatchExtensionFilter import MatchExtensionFilter
from app.model.filter.OrOperationFilter import OrOperationFilter

Filter = Annotated[AndOperationFilter | OrOperationFilter | HigherThanSizeFilter | LowerThanSizeFilter | MatchExtensionFilter, Field(discriminator='type') ]

AndOperationFilter.update_forward_refs()
OrOperationFilter.update_forward_refs()