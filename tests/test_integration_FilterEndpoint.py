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


def test_filter_integration(client) -> None:
    # GIVEN
    shared_path = injector.get(Config).shared_path
    response = client.post("/filter",
                           json={
                               "type": "MatchExtension",
                               "extension": ".txt"})
    assert response.status_code == 200
    # Assuming your application should return a list of files ending with .txt in the shared_path
    assert ".txt" in response.json()[0]


def test_filter_integration_with_complex_filter(client) -> None:

    request = {
        "type": "AndOperation",
        "operands": [
            {
                "type": "HigherThanSize",
                "size": 512
            },
            {
                "type": "MatchExtension",
                "extension": "txt"
            }
        ]
    }

    response = client.post("/filter",
                           json=request)
    assert response.status_code == 200
    print(response.json())


def test_filter_integration_with_two_complex_filters(client) -> None:

    request = {
        "type": "OrOperation",
        "operands": [
            {
                "type": "LowerThanSize",
                "size": 1024
            },
            {
                "type": "AndOperation",
                "operands": [
                    {
                        "type": "HigherThanSize",
                        "size": 512
                    },
                    {
                        "type": "MatchExtension",
                        "extension": "txt"
                    }
                ]
            }
        ]
    }
    response = client.post("/filter",
                           json=request)
    assert response.status_code == 200
    print(response.json())
