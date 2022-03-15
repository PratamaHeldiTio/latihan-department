from src.shared import helper
from src.articles.v1.repository.article_repository import ArticleRepository

class ArticleRepositoryOrator(ArticleRepository):
    def __init__(self, db):
        self.db = db

    def get_all(self, request_object):
        search = getattr(request_object, 'search')
        page = getattr(request_object, 'page')
        limit = getattr(request_object, 'limit')
        sort_by = getattr(request_object, 'sortBy')
        order_by = getattr(request_object, 'orderBy')
        offset = page * limit - limit

        query = self.db.table('article')

        if search:
            query = query.where('title', 'ilike', '%{}%'.format(search))

        query = query.order_by(sort_by, order_by)
        query = query.offset(offset).limit(limit).get()

        result = []
        for row in query:
            data = ({
                'id': row['id'],
                'title': row['title'],
                'content': row['content'],
                'created_at': row['created_at'],
                'modified_at':row['modified_at'],
                'created_by': row['created_by'],
                'modified_by': row['modified_by'],
            })
            result.append(data)

        return result

    def create(self, request_object):
        return self.db.table('article').insert({
            'title': getattr(request_object, 'title'),
            'content': getattr(request_object, 'content'),
            'created_at': helper.get_now_timestamp(),
            'modified_at': helper.get_now_timestamp(),
            'created_by': getattr(request_object, 'created_by'),
            'modified_by': getattr(request_object, 'modified_by'),
        })

    def update_by_id(self, request_object):
        return self.db.table('article').where('id', getattr(request_object, 'id')).update({
            'title': getattr(request_object, 'title'),
            'content': getattr(request_object, 'content'),
            'created_by': getattr(request_object, 'created_by'),
            'modified_by': getattr(request_object, 'modified_by'),
            'modified_at': helper.get_now_timestamp()
        })

    def delete_by_id(self, id):
        return self.db.table('article').where('id', '=', id).delete()

    def article_is_exist(self, id):
        return self.db.table('article').where('id', id).count()
