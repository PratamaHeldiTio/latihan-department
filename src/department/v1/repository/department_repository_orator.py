from src.shared import helper
from src.department.v1.domain.department import Department
from src.department.v1.repository.department_repository import DepartmentRepository

class DepartmentRepositoryOrator(DepartmentRepository):
    def __init__(self, db):
        self.db = db

    def get_all(self, request_objects):
        query = self.db.table('department').get()

        result = []
        for row in query:
            data = Department.from_dict({
                'id': row['id'],
                'name': row['name'],
                'status': row['status'],
                'created_at': row['created_at'],
                'modified_at': row['modified_at']
            })
            result.append(data)

        return result

    def create(self, request_objects):
        query = self.db.table('department').insert({
            'name': getattr(request_objects, "name"),
            'status': getattr(request_objects, "status"),
            'created_at': helper.get_now_timestamp(),
            'modified_at': helper.get_now_timestamp(),
        })

        return query

    def update_by_id(self, request_objects):
        query = self.db.table('department').where('id', request_objects['id']).update({
            'name': request_objects['name'],
            'status': request_objects['status'],
            'modified_at': helper.get_now_timestamp()
        })

        return query

    def delete_by_id(self, request_objects):
        query = self.db.table('department').where('id', request_objects['id']).delete()

        return query

