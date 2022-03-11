from sanic import Blueprint
from sanic.response import json
from config.config import Config
from src.articles.v1.repository.article_repository_orator import ArticleRepositoryOrator
from src.shared.request.request_sanic import RequestSanicDict
from src.articles.v1.usecase.article_usecase import \
    ListArticleUsecase, \
    CreateArticleUsecase, \
    UpdateArticleUsecase, \
    DeleteArticleUsecase
from src.articles.v1.delivery.article_request_object import \
    ListArticleRequestObject, \
    CreateArticleRequestObject, \
    UpdateArticleRequestObject
from src.shared.validator.validator_jsonschema import JSONSchemaValidator

bp_articles = Blueprint('V1/Articles', url_prefix='v1/articles')

@bp_articles.route('/', methods=['GET', 'POST'])
async def index(request):
    request_dict = RequestSanicDict(request)
    repo_init = ArticleRepositoryOrator(db=request.app.db)
    validator = JSONSchemaValidator()

    if request.method == 'GET':
        usecase = ListArticleUsecase(repo=repo_init)
        adict = request_dict.query_to_dict()
        request_object = ListArticleRequestObject.from_dict(adict=adict, validator=validator)
        response_object = usecase.execute(request_object)

    if request.method == 'POST':
        usecase = CreateArticleUsecase(repo=repo_init)
        adict = request_dict.json_to_dict()
        request_object = CreateArticleRequestObject.from_dict(adict=adict, validator=validator)
        response_object = usecase.execute(request_object)

    return json(response_object.value, status=Config.STATUS_CODES[response_object.type])

@bp_articles.route('/<identifier>', methods=['PUT', 'DELETE'])
async def detail(request, identifier):
    request_dict = RequestSanicDict(request)
    repo_init = ArticleRepositoryOrator(db=request.app.db)
    validator = JSONSchemaValidator()
    identifier = int(identifier)

    if request.method == 'PUT':
        usecase = UpdateArticleUsecase(repo=repo_init)
        adict = request_dict.json_to_dict()
        adict['id'] = identifier
        request_object = UpdateArticleRequestObject.from_dict(adict=adict, validator=validator)
        response_object = usecase.execute(request_object)

    if request.method == 'DELETE':
        usecase = DeleteArticleUsecase(repo=repo_init)
        response_object = usecase.execute(identifier)

    return json(response_object.value, status=Config.STATUS_CODES[response_object.type])
