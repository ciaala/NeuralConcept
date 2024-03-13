
import pytest
from fastapi import FastAPI
from unittest.mock import AsyncMock, MagicMock
from httpx import AsyncClient

from app.endpoints.FilterEndpoint import FilterEndpoint
from app.service.filter.FilterService import FilterService
from app.Config import Config

@pytest.fixture
def mock_filter_service():
    service = MagicMock(spec=FilterService)
    service.filter = MagicMock(return_value=["filtered_path1", "filtered_path2"])
    return service

@pytest.fixture
def mock_config():
    config = MagicMock(spec=Config)
    config.shared_path = "/test/shared/path"
    return config

@pytest.fixture
def app(mock_filter_service, mock_config):
    application = FastAPI()
    filter_endpoint = FilterEndpoint(filter_service=mock_filter_service, config=mock_config)
    filter_endpoint.register(application)
    return application

@pytest.mark.asyncio
async def test_filter_endpoint(app):
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/filter", json={"type": "HigherThanSize", "size": 1024})
    assert response.status_code == 200
    assert response.json() == ["filtered_path1", "filtered_path2"]