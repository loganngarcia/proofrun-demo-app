import pytest
from pydantic import ValidationError

from app import import_row


def test_explicit_nickname():
    assert import_row({"name": "Grace", "nickname": "Gracie"})["nickname"] == "Gracie"


def test_explicit_null_nickname():
    assert import_row({"name": "Grace", "nickname": None})["nickname"] is None


def test_omitted_nickname_is_allowed():
    # Customers may omit nickname. Fails after the Pydantic 1 -> 2 upgrade.
    assert import_row({"name": "Grace"})["nickname"] is None


def test_missing_name_rejected():
    with pytest.raises(ValidationError):
        import_row({"nickname": "Grace"})
