from sanic import Blueprint
from sanic.response import json
from config.config import Config
from src.department.v1.repository.department_repository_orator import DepartmentRepositoryOrator
from src.shared.request.request_sanic import RequestSanicDict
from src.department.v1.usecase.department_usecase import ListDepartmentUsecase
from src.department.v1.delivery.department_request_object import ListDepartmentRequestObject
from src.shared.validator.validator_cerberus import ValidatorCerberus


bp_department = Blueprint('Department V1', url_prefix='v1/department')

@bp_department.route('/', methods=['GET'])
async def index(request):
    obj_dict = RequestSanicDict(request).parse_all_to_dict()

    if request.method == 'GET':
        validator = ValidatorCerberus()
        repo_init = DepartmentRepositoryOrator(db=request.app.db)
        usecase = ListDepartmentUsecase(repo=repo_init)
        request_object = ListDepartmentRequestObject.from_dict(adict=request.raw_args, validator=validator)
        response_object = usecase.execute(request_object)

    return  json(response_object.value, status=Config.STATUS_CODES[response_object.type])
