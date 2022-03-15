from config.config import Config
from src.department.v1.usecase.abc_department_usecase import DepartmentUsecase
from src.shared import response_object as ro
from src.department.v1.serializers.department_serializers import ListDepartment
from src.shared.helper import response_object
class ListDepartmentUsecase(DepartmentUsecase):
    def __init__(self, repo):
        self.repo = repo

    def process_request(self, request_objects):
        department = self.repo.get_all(request_objects)
        total = len(department)
        schema = ListDepartment()
        serialize = schema.dump(department, many=True)
        meta= {
            'page': getattr(request_objects, 'page'),
            'limit': getattr(request_objects, 'limit'),
            'total': total
        }

        response = response_object(
            status_code=Config.SUCCESS,
            message=Config.SUCCESS,
            data=serialize,
            meta=meta
        )
        return ro.ResponseSuccess(response)

class CreateDepartmentUsecase(DepartmentUsecase):
    def __init__(self, repo):
        self.repo = repo

    def process_request(self, request_object):
        self.repo.create(request_object)

        response = response_object(status_code=Config.CREATED, message=Config.CREATED)
        return ro.ResponseSuccess(response)

class UpdateDepartmentUsecase(DepartmentUsecase):
    def __init__(self, repo):
        self.repo = repo

    def process_request(self, request_object):
        # check department is exist
        department = self.repo.department_is_exist(getattr(request_object, 'id'))
        if department:
            self.repo.update_by_id(request_object)
            response = response_object(status_code=Config.SUCCESS, message=Config.SUCCESS)
        else:
            response = response_object(status_code=Config.DATA_NOT_FOUND, message=Config.DATA_NOT_FOUND)

        return ro.ResponseSuccess(response)

class DeleteDepartmentUsecase(DepartmentUsecase):
    def __init__(self, repo):
        self.repo = repo

    def process_request(self, id):
        # check department is exist
        department = self.repo.department_is_exist(id)
        if department:
            self.repo.delete_by_id(id)
            response = response_object(status_code=Config.SUCCESS, message=Config.SUCCESS)
        else:
            response = response_object(status_code=Config.DATA_NOT_FOUND, message=Config.DATA_NOT_FOUND)

        return ro.ResponseSuccess(response)
