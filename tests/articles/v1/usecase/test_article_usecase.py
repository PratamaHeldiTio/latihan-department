from unittest import mock

from math import ceil

from config.config import Config
from schemas.json.loader import JSONSchemaLoader
from src.articles.v1.domain.article import Article
from src.articles.v1.serializers.article_serializers import ListArticleToJsonFormat
from src.articles.v1.usecase.article_usecase import ListArticleUsecase
from src.shared.validator.validator_jsonschema import JSONSchemaValidator
from src.articles.v1.delivery.article_request_object import ListArticleRequestObject
from src.shared.helper import response_object


def domain_article():
    article_1 = Article.from_dict(
        {
            'id': 1,
            'title': 'Title blog 1',
            'content': 'Content blog',
            'created_at': '2018-07-11',
            'created_by': 'system',
            'modified_at': '2018-07-12',
            'modified_by': 'system'
        }
    )

    return [article_1]

def test_article_get_all():

    JSONSchemaLoader.load(path='config/schemas/json/', filename="*.json")
    validator = JSONSchemaValidator()

    repo = mock.Mock()
    repo.get_all.return_value = domain_article()
    repo.get_total.return_value = len(domain_article())
    use_case = ListArticleUsecase(repo)

    request_object = ListArticleRequestObject.from_dict({'page':1, 'limit':10}, validator=validator)
    response_objects = use_case.execute(request_object)

    serialize = ListArticleToJsonFormat(many=True).dump(domain_article())
    meta = {'page': 1,'limit':10, 'total' : len(domain_article())}

    expected_return = response_object(Config.SUCCESS,Config.SUCCESS, serialize, meta)

    assert response_objects.value == expected_return
