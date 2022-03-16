import pytest

from schemas.json.loader import JSONSchemaLoader
from src.articles.v1.repository.article_repository_orator import ArticleRepositoryOrator
from src.articles.v1.delivery.article_request_object import ListArticleRequestObject
from src.app import connect_db
from src.shared.validator.validator_jsonschema import JSONSchemaValidator

@pytest.fixture(scope="module")
def db_con():
    db = connect_db()
    yield db
    db.disconnect()

def test_get_all(db_con):
    JSONSchemaLoader.load(path='config/schemas/json', filename="*.json")
    validator = JSONSchemaValidator()
    request_object = ListArticleRequestObject.from_dict({}, validator)
    result = ArticleRepositoryOrator(db=db_con).get_all(request_object)

    assert isinstance(result, list)
