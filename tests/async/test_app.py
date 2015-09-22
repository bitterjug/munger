import pytest
from webapp.application import Application


@pytest.fixture
def app():
    return Application()


@pytest.mark.gen_test
def test_app(base_url, http_client):
    response = yield http_client.fetch(base_url)
    assert response.code == 200
