"""Tiny customer-import service, written against Pydantic v1 semantics."""
from typing import Optional

from pydantic import BaseModel


class Customer(BaseModel):
    name: str
    nickname: Optional[str] = None  # BUG: required in Pydantic v2; v1 treated it as optional


def import_row(row: dict) -> dict:
    """Validate one imported customer row and return normalized data."""
    return Customer(**row).model_dump()
