from src.shared import helper
from src.department.v1.domain.department import Department
from src.department.v1.repository.department_repository import DepartmentRepository

class DepartmentRepositoryOrator(DepartmentRepository):
    def __init__(self, db):
        self.db = db

    def get_all(self, request_object):
        search = getattr(request_object, 'search')
        query = self.db.table('department')
        sort_by = getattr(request_object, 'sortBy')
        order_by = getattr(request_object, 'orderBy')
        page =  getattr(request_object, 'page')
        limit = getattr(request_object, 'limit')

        if search:
            query = query.where('name', 'ilike', '%{}%'.format(search))

        query = query.order_by(sort_by, order_by)

        offset = page * limit  - limit
        query = query.offset(offset).limit(limit).get()
        result = []
        for row in query:
            data = ({
                'id': row['id'],
                'name': row['name'],
                'status': row['status'],
                'created_at': row['created_at'],
                'modified_at': row['modified_at']
            })
            result.append(data)

        return result

    def create(self, request_object):
        query = self.db.table('department').insert({
            'name': getattr(request_object, "name"),
            'status': getattr(request_object, 'status'),
            'created_at': helper.get_now_timestamp(),
            'modified_at': helper.get_now_timestamp(),
        })

        return query

    def update_by_id(self, request_object):
        query = self.db.table('department').where('id', getattr(request_object, 'id')).update({
            'name': getattr(request_object, 'name'),
            'status': getattr(request_object, 'status'),
            'modified_at': helper.get_now_timestamp()
        })

        return query

    def delete_by_id(self, id):
        query = self.db.table('department').where('id', id).delete()

        return query

    def get_total(self, request_object):
        query = self.db.table('department')

        if getattr(request_object, 'search'):
            query = query.where('name', 'ilike', '%{}%'.format(getattr(request_object, 'search')))

        return query.count()

    def department_is_exist(self, id):
        return self.db.table('department').where('id', '=', id).count()
