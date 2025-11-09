from fastapi import HTTPException, Security, status
from fastapi.security import APIKeyHeader

from .configs import settings

api_key_header = APIKeyHeader(name=settings.api_key_header_name)


async def get_api_key(api_key_header: str = Security(api_key_header)):
    if api_key_header != settings.api_key_header_name:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="We could not validate your credentials.",
        )

    return api_key_header
