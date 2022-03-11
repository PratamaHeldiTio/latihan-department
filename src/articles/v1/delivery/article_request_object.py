from src.shared import helper
from src.shared.request_object import ValidRequestObject, InvalidRequestObject
from config.schemas.json.loader import JSONSchemaLoader

class ListArticleRequestObject(ValidRequestObject):
    def __init__(self, **kwargs):
        self.sortBy = kwargs.get("sortBy")
        self.orderBy = kwargs.get("orderBy")
        self.limit = kwargs.get("limit")
        self.page = kwargs.get("page")
        self.search = kwargs.get("search")

    @classmethod
    def from_dict(cls, adict, validator=None):
        JSONSchemaLoader.load(path='config/schemas/json/', filename='*json')
        schema = JSONSchemaLoader.get('get_list_article')

        if not validator.is_valid(adict=adict, schema=schema):
            invalid_req = InvalidRequestObject()
            invalid_req.parse_error(errors=validator.get_error())
            return invalid_req

        data = validator.get_valid_data()

        return ListArticleRequestObject(**{
            "sortBy": data.get("sortBy", "id"),
            "orderBy": data.get("orderBy", "asc"),
            "limit": int(data.get("limit", "10")),
            "page": int(data.get("page", "1")),
            "search": data.get("search", "")
        })

    def __nonzero__(self):
        return True

class CreateArticleRequestObject(ValidRequestObject):
    def __init__(self, **kwargs):
        self.title = kwargs.get('title')
        self.content = kwargs.get('content')
        self.created_by = kwargs.get('created_by')
        self.modified_by = kwargs.get('modified_by')

    @classmethod
    def from_dict(cls, adict, validator=None):
        JSONSchemaLoader.load(path='config/schemas/json/', filename='*json')
        schema = JSONSchemaLoader.get('create_article')

        if not validator.is_valid(adict=adict, schema=schema):
            invalid_req = InvalidRequestObject()
            invalid_req.parse_error(errors=validator.get_error())
            return invalid_req

        data = validator.get_valid_data()

        return CreateArticleRequestObject(**{
            'title': data.get('title', ''),
            'content': data.get('content', ''),
            'created_by': data.get('createdBy', ''),
            'modified_by': data.get('modifiedBy', '')
        })

class UpdateArticleRequestObject(ValidRequestObject):
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.title = kwargs.get('title')
        self.content = kwargs.get('content')
        self.created_by = kwargs.get('created_by')
        self.modified_by = kwargs.get('modified_by')

    @classmethod
    def from_dict(cls, adict, validator=None):
        JSONSchemaLoader.load(path='config/schemas/json/', filename='*json')
        schema = JSONSchemaLoader.get('update_article')

        if not validator.is_valid(adict=adict, schema=schema):
            invalid_req = InvalidRequestObject()
            invalid_req.parse_error(errors=validator.get_error())
            return invalid_req

        data = validator.get_valid_data()

        return UpdateArticleRequestObject(**{
            'id': data.get('id', ''),
            'title': data.get('title', ''),
            'content': data.get('content', ''),
            'created_by': data.get('createdBy', ''),
            'modified_by': data.get('modifiedBy', '')
        })
