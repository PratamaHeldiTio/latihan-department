import json
import pytest
from config.config import Config
from src.app import connect_db, create_app


api_url = '/v1/department/'


@pytest.yield_fixture
def db_con():
    db = connect_db()
    app = create_app(Config)
    app.db = db
    yield app


@pytest.fixture
def test_cli(loop, db_con, test_client):
    return loop.run_until_complete(test_client(db_con))

async def test_get_all(test_cli):
    resp = await test_cli.get(api_url)
    response = json.loads(resp.content._buffer[0])
    assert resp.status == 200
    assert response['success']
    assert response['code'] == 200
    assert response['message'] == "success"
