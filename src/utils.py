import math
from typing import List, Optional

import pandas as pd

from .models import SortParams


def load_csv_data(
    filepath: str, parse_dates: Optional[List[str]] = None
) -> pd.DataFrame:
    """Load respective data from a CSV file into a pandas DataFrame."""
    try:
        df = pd.read_csv(filepath, parse_dates=parse_dates)
        return df
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def generate_pagination_metadata(dataframe: pd.DataFrame, limit: int):
    """Generate metadata for pagination."""
    total_items = len(dataframe)
    total_pages = math.ceil(total_items / limit)

    return {"total_items": total_items, "total_pages": total_pages}


def get_paginated_data(dataframe: pd.DataFrame, page: int, limit: int) -> pd.DataFrame:
    """Return paginated data for a certain page and limit."""
    skip = (page - 1) * limit
    data = dataframe.iloc[skip : skip + limit].to_dict(orient="records")

    return data


def sort_data(dataframe: pd.DataFrame, sort: SortParams) -> pd.DataFrame:
    """Sort a pandas DataFrame based on SortParams."""
    if sort.sort_by:
        return dataframe.sort_values(
            by=sort.sort_by, ascending=sort.order == "asc", inplace=False
        )
    return dataframe
