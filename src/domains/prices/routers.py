from typing import Annotated, List

import pandas as pd
from fastapi import APIRouter, Depends, HTTPException, Query, status

from src.constants import ExceptionMessages
from src.loaders import df_equities, df_price_history
from src.models import PaginatedResponse, PaginationParams, SortParams
from src.utils import generate_pagination_metadata, get_paginated_data, sort_data

from .models import Price, PriceFilterParams
from .utils import filter_data

router = APIRouter()


@router.get("", response_model=PaginatedResponse[List[Price]])
def get_stocks(
    filter_params: Annotated[PriceFilterParams, Query()],
    pagination_params: Annotated[PaginationParams, Depends()],
    sorting_params: Annotated[SortParams, Depends()],
):
    """Get all stock prices"""
    data = pd.merge(df_price_history, df_equities, on="portid")

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
