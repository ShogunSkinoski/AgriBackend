import pytest

from modules.flies.domain.flies import Flies

def test_if_flies_model_is_valid():
    flies = Flies(greenhouse_id=1, sector_id=1, total_flies=1)
    assert flies.greenhouse_id == 1
    assert flies.sector_id == 1
    assert flies.total_flies == 1
    assert flies.created_at is not None

def test_if_flies_model_can_be_created_with_dict():
    flies = Flies.from_dict({"greenhouse_id": 1, "sector_id": 1, "total_flies": 1})
    assert flies.greenhouse_id == 1
    assert flies.sector_id == 1
    assert flies.total_flies == 1
    assert flies.created_at is not None

def test_if_flies_model_can_be_created_with_dict_and_created_at():
    flies = Flies.from_dict({"greenhouse_id": 1, "sector_id": 1, "total_flies": 1, "created_at": "2021-01-01"})
    assert flies.greenhouse_id == 1
    assert flies.sector_id == 1
    assert flies.total_flies == 1
    assert flies.created_at == "2021-01-01"

def test_if_flies_dict_can_be_created_from_model():
    flies_model = Flies(greenhouse_id=1, sector_id=1, total_flies=1)
    flies_dict = flies_model.to_dict()
    assert flies_dict["greenhouse_id"] == 1
    assert flies_dict["sector_id"] == 1
    assert flies_dict["total_flies"] == 1
    assert flies_dict["created_at"] is not None