
from fastapi import Request

from app.providers.base import Provider


def get_provider(request: Request) -> Provider:
    return request.app.state.provider
