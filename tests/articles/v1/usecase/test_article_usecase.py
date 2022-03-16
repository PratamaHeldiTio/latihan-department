from unittest import mock
from schemas.json.loader import JSONSchemaLoader
from src.articles.v1.usecase.article_usecase import ListArticleUsecase
from src.shared.validator.validator_jsonschema import JSONSchemaValidator
from src.articles.v1.delivery.article_request_object import ListArticleRequestObject


def test_execute():
    JSONSchemaLoader.load(path='config/schemas/json/', filename="*.json")
    validator = JSONSchemaValidator()

    repository = mock.Mock()
    use_case = ListArticleUsecase(repository)

    request_object = ListArticleRequestObject.from_dict({}, validator=validator)
    response_object = use_case.execute(request_object)

    assert bool(response_object) is False

