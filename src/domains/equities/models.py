from datetime import date
from typing import Annotated, List

from pydantic import BaseModel, StringConstraints


class Equity(BaseModel):
    portid: Annotated[str, StringConstraints(to_upper=True, strip_whitespace=True)]
    portname: str
    sectorid: Annotated[str, StringConstraints(to_upper=True)]
    sector: Annotated[str, StringConstraints(to_upper=True)]
    subsector: Annotated[str, StringConstraints(to_upper=True)]
    subsectorid: Annotated[str, StringConstraints(to_upper=True)]
    listeddate: date


class EquityFilterParams(BaseModel):
    search: List[Annotated[str, StringConstraints(strip_whitespace=True)]] | None = None
    sector: (
        Annotated[str, StringConstraints(to_upper=True, strip_whitespace=True)] | None
    ) = None
    subsector: (
        Annotated[str, StringConstraints(to_upper=True, strip_whitespace=True)] | None
    ) = None
