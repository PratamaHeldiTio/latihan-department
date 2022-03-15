from config.config import Config

from src.articles.v1.usecase.abc_article_usecase import ArticleUsecase
from src.shared import response_object as ro
from src.articles.v1.serializers.article_serializers import ListArticleToJsonFormat
from src.shared.helper import response_object

class ListArticleUsecase(ArticleUsecase):

    def __init__(self, repo):
        self.repo = repo

    def process_request(self, request_objects):
        articles = self.repo.get_all(request_objects)
        total = len(articles)
        schema = ListArticleToJsonFormat()
        serialize = schema.dump(articles, many=True)
        meta = {
            'page': getattr(request_objects, 'page'),
            'limit': getattr(request_objects, 'limit'),
            'total': total
        }

        response = response_object(
            status_code=Config.SUCCESS,
            message=Config.SUCCESS,
            data=serialize,
            meta=meta)

        return ro.ResponseSuccess(response)

class CreateArticleUsecase(ArticleUsecase):
    def __init__(self, repo):
        self.repo = repo

    def process_request(self, request_object):
        self.repo.create(request_object)

        response = response_object(status_code=Config.CREATED, message=Config.CREATED)
        return ro.ResponseSuccess(response)

class DeleteArticleUsecase(ArticleUsecase):
    def __init__(self, repo):
        self.repo = repo

    def process_request(self, id):
        article_available = self.repo.article_is_exist(id)

        if article_available:
            self.repo.delete_by_id(id)
            response = response_object(status_code=Config.SUCCESS, message=Config.SUCCESS)
        else:
            response = response_object(status_code=Config.DATA_NOT_FOUND, message=Config.DATA_NOT_FOUND)

        return ro.ResponseSuccess(response)

class UpdateArticleUsecase(ArticleUsecase):
    def __init__(self, repo):
        self.repo = repo

    def process_request(self, request_object):
        article_available = self.repo.article_is_exist(getattr(request_object, 'id'))

        if article_available:
            self.repo.update_by_id(request_object)
            response = response_object(status_code=Config.SUCCESS, message=Config.SUCCESS)
        else:
            response = response_object(status_code=Config.DATA_NOT_FOUND, message=Config.DATA_NOT_FOUND)

        return ro.ResponseSuccess(response)
