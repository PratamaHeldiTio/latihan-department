from config.config import Config
from src.department.v1.usecase.abc_department_usecase import DepartmentUsecase
from src.shared.response_object import ResponseSuccess
from src.department.v1.serializers.department_serializers import ListDepartment

class ListDepartmentUsecase(DepartmentUsecase):
    def __init__(self, repo):
        self.repo = repo

    def process_request(self, request_object):
        department = self.repo.get_all(request_object)
        schema = ListDepartment()
        serialize = schema.dump(department, many=True)

        response = {
            'success': True,
            'code': Config.STATUS_CODES[Config.SUCCESS],
            'message': Config.SUCCESS.lower(),
            'data': serialize
        }

        return ResponseSuccess(response)
