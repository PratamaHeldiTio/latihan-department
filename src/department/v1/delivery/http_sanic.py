from sanic import Blueprint
from sanic.response import json
from config.config import Config
from src.department.v1.repository.department_repository_orator import DepartmentRepositoryOrator
from src.shared.request.request_sanic import RequestSanicDict
from src.department.v1.usecase.department_usecase import \
    ListDepartmentUsecase, \
    CreateDepartmentUsecase, \
    UpdateDepartmentUsecase, \
    DeleteDepartmentUsecase
from src.department.v1.delivery.department_request_object import \
    ListDepartmentRequestObject, \
    CreateDeparmentRequestObject, \
    UpdateDepartmentRequestObject
from src.shared.validator.validator_jsonschema import JSONSchemaValidator


bp_department = Blueprint('V1/department', url_prefix='v1/department')

@bp_department.route('/', methods=['GET', 'POST'])
async def index(request):
    request_dict = RequestSanicDict(request)
    repo_init = DepartmentRepositoryOrator(db=request.app.db)
    validator = JSONSchemaValidator()

    if request.method == 'GET':
        usecase = ListDepartmentUsecase(repo=repo_init)
        adict = request_dict.query_to_dict()
        request_object = ListDepartmentRequestObject.from_dict(adict=adict, validator=validator)
        response_object = usecase.execute(request_object)

    if request.method == 'POST':
        usecase = CreateDepartmentUsecase(repo=repo_init)
        adict = request_dict.json_to_dict()
        request_object = CreateDeparmentRequestObject.from_dict(adict=adict, validator=validator)
        response_object = usecase.execute(request_object)

    return  json(response_object.value, status=Config.STATUS_CODES[response_object.type])

@bp_department.route('/<identifier>', methods=['GET', 'PUT', 'DELETE'])
async def detail (request, identifier):
    identifier = int(identifier)
    request_dict = RequestSanicDict(request)
    repo_init = DepartmentRepositoryOrator(db=request.app.db)
    validator = JSONSchemaValidator()

    if request.method == 'GET':
        adict = {'id': identifier}
        usecase = ListDepartmentUsecase(repo=repo_init)
        request_object = ListDepartmentRequestObject.from_dict(adict=adict, validator=validator)
        response_object = usecase.execute(request_object)

    if request.method == 'PUT':
        usecase =UpdateDepartmentUsecase(repo=repo_init)
        adict = request_dict.json_to_dict()
        adict['id'] = identifier
        request_object = UpdateDepartmentRequestObject.from_dict(adict=adict, validator=validator)
        response_object = usecase.execute(request_object)

    if request.method == 'DELETE':
        usecase =DeleteDepartmentUsecase(repo=repo_init)
        response_object = usecase.execute(identifier)

    return  json(response_object.value, status=Config.STATUS_CODES[response_object.type])
