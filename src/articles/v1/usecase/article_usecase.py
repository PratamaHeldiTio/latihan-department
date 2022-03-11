from config.config import Config

from src.articles.v1.usecase.abc_article_usecase import ArticleUsecase
from src.shared import response_object as ro
from src.articles.v1.serializers.article_serializers import ListArticleToJsonFormat

class ListArticleUsecase(ArticleUsecase):

    def __init__(self, repo):
        self.repo = repo

    def process_request(self, request_objects):
        articles = self.repo.get_all(request_objects)
        total = self.repo.get_total(request_objects)
        schema = ListArticleToJsonFormat()
        serialize = schema.dump(articles, many=True)

        response = {
            'success': True,
            'code': Config.STATUS_CODES[Config.SUCCESS],
            'message': Config.SUCCESS.lower(),
            'data': serialize.data,
            'meta': {
                'page': getattr(request_objects, 'page'),
                'limit': getattr(request_objects, 'limit'),
                'total': total
            }
        }

        return ro.ResponseSuccess(response)

class CreateArticleUsecase(ArticleUsecase):
    def __init__(self, repo):
        self.repo = repo

    def process_request(self, request_object):
        self.repo.create(request_object)

        response = {
            'status': True,
            'code': Config.HTTP_STATUS_CODES[201],
            'message': Config.SUCCESS.lower(),
            'data': []
        }

        return ro.ResponseSuccess(response)

class DeleteArticleUsecase(ArticleUsecase):
    def __init__(self, repo):
        self.repo = repo

    def process_request(self, id):
        self.repo.delete_by_id(id)

        response = {
            'status': True,
            'code': Config.STATUS_CODES[Config.SUCCESS],
            'message': Config.SUCCESS.lower(),
            'data': []
        }

        return ro.ResponseSuccess(response)

class UpdateArticleUsecase(ArticleUsecase):
    def __init__(self, repo):
        self.repo = repo

    def process_request(self, request_object):
        self.repo.update_by_id(request_object)

        response = {
            'status': True,
            'code': Config.STATUS_CODES[Config.SUCCESS],
            'message': Config.SUCCESS.lower(),
            'data': []
        }

        return ro.ResponseSuccess(response)
