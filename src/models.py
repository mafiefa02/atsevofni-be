from typing import Annotated, Generic, Literal, TypeVar

from pydantic import BaseModel, Field


class SortParams(BaseModel):
    sort_by: str | None = None
    order: Literal["desc", "asc"] = "desc"


class PaginationParams(BaseModel):
    page: Annotated[int, Field(ge=1)] = 1
    limit: Annotated[int, Field(ge=1)] = 50


class PaginationMeta(PaginationParams):
    total_items: Annotated[int, Field(ge=0)]
    total_pages: Annotated[int, Field(ge=0)]


T = TypeVar("T")


class PaginatedResponse(BaseModel, Generic[T]):
    data: T
    meta: PaginationMeta
