from typing import Annotated, List

from fastapi import APIRouter, Depends, HTTPException, Query, status
from pydantic import StringConstraints

from src.constants import ExceptionMessages
from src.loaders import df_equities
from src.models import PaginatedResponse, PaginationParams, SortParams
from src.utils import generate_pagination_metadata, get_paginated_data, sort_data

from .models import Equity, EquityFilterParams
from .utils import filter_data

router = APIRouter()


@router.get("", response_model=PaginatedResponse[List[Equity]])
def get_equities(
    filter_params: Annotated[EquityFilterParams, Query()],
    pagination_params: Annotated[PaginationParams, Depends()],
    sorting_params: Annotated[SortParams, Depends()],
):
    """Get all equities"""
    data = df_equities

    if data is None:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=ExceptionMessages.DATA_LOADING_FAILED,
        )

    data = filter_data(data, filter_params)
    data = sort_data(data, sorting_params)

    returned_data = get_paginated_data(
        data, page=pagination_params.page, limit=pagination_params.limit
    )

    pagination_metadata = generate_pagination_metadata(
        data, limit=pagination_params.limit
    )

    return {
        "data": returned_data,
        "meta": {**pagination_params.dict(), **pagination_metadata},
    }


@router.get("/{portid}", response_model=Equity)
def get_equity_by_portid(portid: Annotated[str, StringConstraints(to_upper=True)]):
    """Get detailed equity information by its portid"""
    data = df_equities

    if data is None:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=ExceptionMessages.DATA_LOADING_FAILED,
        )

    returned_data = data[data["portid"] == portid].to_dict(orient="records")

    if not returned_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Equity with portid '{portid}' not found.",
        )

    return returned_data[0]
