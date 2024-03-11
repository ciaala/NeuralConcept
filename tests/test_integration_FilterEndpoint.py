import logging

import pytest
from fastapi.testclient import TestClient
from injector import Injector

from app.Application import Application
from app.Config import Config

injector = Injector()
@pytest.fixture(scope="module")
def client() -> TestClient:

    nc_cfs: Application = injector.get(Application)
    with TestClient(nc_cfs.server.app) as test_client:
        yield test_client

def test_filter_integration(client):
    # GIVEN
    shared_path = injector.get(Config).shared_path
    logging.info("App would check for file in shared_path")
    response = client.post("/filter", json={"type": "MatchExtensionFilter", "extension": ".txt"})
    assert response.status_code == 200
    # Assuming your application should return a list of files ending with .txt in the shared_path
    assert ".txt" in response.json()[0]