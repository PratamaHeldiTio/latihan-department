from sanic import Blueprint
from sanic.response import json
from config.config import Config
from src.department.v1.repository.department_repository_orator import DepartmentRepositoryOrator
from src.shared.request.request_sanic import RequestSanicDict
from src.department.v1.usecase.department_usecase import ListDepartmentUsecase, CreateDepartmentUsecase
from src.department.v1.delivery.department_request_object import ListDepartmentRequestObject
from src.shared.validator.validator_jsonschema import JSONSchemaValidator


bp_department = Blueprint('V1/department', url_prefix='v1/department')

@bp_department.route('/', methods=['GET', 'POST'])
async def index(request):
    obj_dict = RequestSanicDict(request).parse_all_to_dict()
    if request.method == 'GET':
        validator = JSONSchemaValidator()
        repo_init = DepartmentRepositoryOrator(db=request.app.db)
        usecase = ListDepartmentUsecase(repo=repo_init)

        request_dict = RequestSanicDict(request)
        adict = request_dict.query_to_dict()
        request_object = ListDepartmentRequestObject.from_dict(adict=adict, validator=validator)
        response_object = usecase.execute(request_object)

    if request.method == 'POST':
        repo_init = DepartmentRepositoryOrator(db=request.app.db)
        usecase = CreateDepartmentUsecase(repo=repo_init)
        response_object = usecase.execute(obj_dict)

    return  json(response_object.value, status=Config.STATUS_CODES[response_object.type])
