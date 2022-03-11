class Article(object):
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.title = kwargs.get('title')
        self.content = kwargs.get('content')
        self.created_at = kwargs.get('created_at')
        self.modified_at = kwargs.get('modified_at')
        self.created_by = kwargs.get('created_by')
        self.modified_by = kwargs.get('modified_by')

    @classmethod
    def from_dict(cls, adict):
        article = Article(**{
            "id": adict.get('id'),
            "title": adict.get('title'),
            "content": adict.get('content'),
            "created_at": adict.get('created_at'),
            "modified_at": adict.get('modified_at'),
            "created_by": adict.get('created_by'),
            "modified_by": adict.get('modified_by')
        })

        return article
