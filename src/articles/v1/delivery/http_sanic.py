from sanic import Blueprint
from sanic.response import json
from config.config import Config
from src.articles.v1.repository.article_repository_orator import ArticleRepositoryOrator
from src.shared.request.request_sanic import RequestSanicDict
from src.articles.v1.usecase.article_usecase import ListArticleUsecase, CreateArticleUsecase
from src.articles.v1.delivery.article_request_object import \
    ListArticleRequestObject, \
    CreateArticleRequestObject
from src.shared.validator.validator_jsonschema import JSONSchemaValidator

bp_articles = Blueprint('V1/Articles', url_prefix='v1/articles')

@bp_articles.route('/', methods=['GET', 'POST'])
async def index(request):
    request_dict = RequestSanicDict(request)
    repo_init = ArticleRepositoryOrator(d=request.app.db)
    validator = JSONSchemaValidator

    # if request.method == 'GET':
    #     repo_init = ArticleRepositoryOrator(db=request.app.db)
    #     usecase = ListArticleUsecase(repo=repo_init)
    #     request_object = ListArticleRequestObject.from_dict(adict=request.raw_args, validator=validator)
    #     response_object = usecase.execute(request_object)

    if request.method == 'POST':
        usecase = CreateArticleUsecase(repo=repo_init)
        adict = request_dict.json_to_dict()
        request_object = CreateArticleRequestObject.from_dict(adict=adict, validator=JSONSchemaValidator)
        response_object = usecase.execute(request_object)
    return json(response_object.value, status=Config.STATUS_CODES[response_object.type])
