# from src.shared import helper
from src.department.v1.domain.department import Department
from src.department.v1.repository.department_repository import DepartmentRepository

class DepartmentRepositoryOrator(DepartmentRepository):
    def __init__(self, db):
        self.db = db

    def get_all(self, request_object):
        query = self.db.table('department')

        if request_object.title != "":
            query = query.where('title', 'like', '%{}'.format(request_object.title))

        query = query.get()

        result = []
        for row in query:
            data = Department.from_dict({
                'id': row['id'],
                'name': row['name'],
                'status': row['status'],
                'create_at': row['create_at'],
                'modified_at': row['modified_at']
            })
            result.append(data)

        return result
