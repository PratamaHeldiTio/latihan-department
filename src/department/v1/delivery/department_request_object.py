from src.shared import helper
from src.shared.request_object import ValidRequestObject, InvalidRequestObject
from config.schemas.json.loader import JSONSchemaLoader

class ListDepartmentRequestObject(ValidRequestObject):

    def __init__(self, **kwargs):
        self.sortBy = kwargs.get("sortBy")
        self.orderBy = kwargs.get("orderBy")
        self.limit = kwargs.get("limit")
        self.page = kwargs.get("page")
        self.search = kwargs.get("search")

    @classmethod
    def from_dict(cls, adict, validator=None):
        JSONSchemaLoader.load(path='config/schemas/json/', filename="*.json")
        schema = JSONSchemaLoader.get("get_list_department")

        if not validator.is_valid(adict=adict, schema=schema):
            invalid_req = InvalidRequestObject()
            invalid_req.parse_error(errors=validator.get_errors())
            return invalid_req

        data = validator.get_valid_data()

        return ListDepartmentRequestObject(**{
            "sortBy": data.get("sortBy", "id"),
            "orderBy": data.get("orderBy", "asc"),
            "limit": int(data.get("limit", "10")),
            "page": int(data.get("page", "1")),
            "search": data.get("search", "")
        })

class CreateDeparmentRequestObject(ValidRequestObject):

    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.status = kwargs.get("status")

    @classmethod
    def from_dict(cls, adict, validator=None):
        JSONSchemaLoader.load(path='config/schemas/json/', filename="*.json")
        schema = JSONSchemaLoader.get("create_department")

        if not validator.is_valid(adict=adict, schema=schema):
            invalid_req = InvalidRequestObject()
            invalid_req.parse_error(errors=validator.get_errors())
            return invalid_req

        data = validator.get_valid_data()

        return CreateDeparmentRequestObject(**{
            "name": data.get("name", ""),
            "status": data.get("status", "")
        })


class UpdateDepartmentRequestObject(ValidRequestObject):
    def __init__(self, **kwargs):
        self.id = kwargs.get("id")
        self.name = kwargs.get("name")
        self.status = kwargs.get("status")

    @classmethod
    def from_dict(cls, adict, validator=None):
        JSONSchemaLoader.load(path='config/schemas/json/', filename="*.json")
        schema = JSONSchemaLoader.get("update_department")

        if not validator.is_valid(adict=adict, schema=schema):
            invalid_req = InvalidRequestObject()
            invalid_req.parse_error(errors=validator.get_errors())
            return invalid_req

        data = validator.get_valid_data()

        return UpdateDepartmentRequestObject(**{
            "id": data.get("id", ""),
            "name": data.get("name", ""),
            "status": data.get("status", "")
        })
