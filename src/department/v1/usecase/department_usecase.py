from config.config import Config
from src.department.v1.usecase.abc_department_usecase import DepartmentUsecase
from src.shared import response_object as ro
from src.department.v1.serializers.department_serializers import ListDepartment, CreateDepartment
from src.department.v1.domain.department import Department

class ListDepartmentUsecase(DepartmentUsecase):
    def __init__(self, repo):
        self.repo = repo

    def process_request(self, request_objects):
        department = self.repo.get_all(request_objects)
        total = self.repo.get_total(request_objects)
        schema = ListDepartment()
        serialize = schema.dump(department, many=True)

        response = {
            'success': True,
            'code': Config.STATUS_CODES[Config.SUCCESS],
            'message': Config.SUCCESS.lower(),
            'data': serialize,
            'meta': {
                'page': getattr(request_objects, 'page'),
                'limit': getattr(request_objects, 'limit'),
                'total': total
            }
        }

        return ro.ResponseSuccess(response)

class CreateDepartmentUsecase(DepartmentUsecase):
    def __init__(self, repo):
        self.repo = repo

    def process_request(self, request_object):
        self.repo.create(request_object)

        response = {
            'success': True,
            'code': Config.HTTP_STATUS_CODES[201],
            'message': Config.SUCCESS.lower(),
            'data': []
        }

        return ro.ResponseSuccess(response)

class UpdateDepartmentUsecase(DepartmentUsecase):
    def __init__(self, repo):
        self.repo = repo

    def process_request(self, request_object):
    # update data
        self.repo.update_by_id(request_object)

        response = {
            'success': True,
            'code': Config.STATUS_CODES[Config.SUCCESS],
            'message': Config.SUCCESS.lower(),
            'data': []
        }
        return ro.ResponseSuccess(response)

class DeleteDepartmentUsecase(DepartmentUsecase):
    def __init__(self, repo):
        self.repo = repo

    def process_request(self, id):
    # delete data
        self.repo.delete_by_id(id)

        response = {
            'success': True,
            'code': Config.STATUS_CODES[Config.SUCCESS],
            'message': Config.SUCCESS.lower(),
            'data': []
        }
        return ro.ResponseSuccess(response)
