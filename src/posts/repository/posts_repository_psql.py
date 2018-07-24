from src.shared import helper
from src.posts.domain.posts import Posts
from src.posts.repository.posts_repository import PostsRepository

class PostsRepositoryPSQL(PostsRepository):
    def __init__(self, db):
        self.db = db
        self.limit = 10
        super(PostsRepositoryPSQL, self).__init__()

    def get_all(self, filters):
        
        query = self._filter_query(filters)
        result = []
        for row in query:
            data = Posts.from_dict({
                'id': row['id'],
                'title': row['title'],
                'content': row['content'],
                'category_id': row['category_id'],
                'author_id': row['author_id'],
                'created_at': row['created_at'],
                'updated_at':row['updated_at']
            })
            result.append(data)
       
        return {
            'count': query.count(),
            'currentPage': query.current_page,
            'hasMorePages': query.has_more_pages(),
            'lastPage': query.last_page,
            'nextPage': query.next_page,
            'perPage': query.per_page,
            'prevPage': query.previous_page,
            'total': query.total,
            'result': result
        }

    def get_by_id(self, pk):

        query = self.db.table('posts').where('id', pk).where('is_active',True).first()
        if query:
            return Posts.from_dict({
                'id': query['id'],
                'title': query['title'],
                'content': query['content'],
                'category_id': query['category_id'],
                'author_id': query['author_id'],
                'created_at': helper.get_now_timestamp(),
                'updated_at': helper.get_now_timestamp()
            })
        return query
    
    def create(self, adict):
        
        return self.db.table('posts').insert_get_id({
            'title': adict['title'],
            'content': adict['content'],
            'author_id': adict['author_id'],
            'category_id': adict['category_id'],
            'is_active':True,
            'created_at': helper.get_now_timestamp(),
            'updated_at': helper.get_now_timestamp(),
        })

    def update(self, adict):

        return self.db.table('posts').where('id', adict['id']).update({
            'title': adict['title'],
            'content': adict['content'],
            'author_id': adict['author_id'],
            'category_id': adict['category_id'],
            'is_active':adict['is_active'],
            'updated_at': helper.get_now_timestamp(),
        })

    def delete(self, adict): 
        return self.db.table('posts').where('id', '=', adict['id']).delete()

    def _filter_query(self, adict):
        
        query = self.db.table('posts')
        # query = query.select("posts.id","posts.title","posts.content","posts.is_active","posts.created_at","posts.category_id")
        # query = query.join("authors","posts.author_id","=","authors.id")
     
        page = helper.get_value_from_dict(adict, 'page', 1)
      
        limit = helper.get_value_from_dict(adict, 'limit',  self.limit)

        is_active = helper.get_value_from_dict(adict, 'is_active', '')
        if is_active != "":
            query = query.where('is_active','=','{}'.format(is_active) )

        title = helper.get_value_from_dict(adict, 'title', '')
        if title.strip() != "":
            query = query.where('title', 'like', "%{}%".format(title))
        
        content = helper.get_value_from_dict(adict, 'content', '')
        if content.strip() != "":
            query = query.where('content', 'like', "%{}%".format(content))

        sort = helper.get_value_from_dict(adict, 'sort', 'created_at')
        if sort == '-created_at':
            query = query.order_by('created_at', 'DESC')
        else:
            query = query.order_by('created_at', 'ASC')

        return query.paginate(limit, page)
       