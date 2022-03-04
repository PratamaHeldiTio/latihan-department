from src.shared import helper
from src.shared.request_object import ValidRequestObject, InvalidRequestObject
from config.schemas.json.loader import JSONSchemaLoader

class ListDepartmentRequestObject(ValidRequestObject):

    def __init__(self, **kwargs):
        self.order_by = kwargs.get("order_by")
        self.limit = kwargs.get("limit")
        self.page = kwargs.get("page")

    @classmethod
    def from_dict(cls, adict, validator=None):
        JSONSchemaLoader.load(path='config/schemas/json/', filename="*.json")
        schema = JSONSchemaLoader.get("get_list_department")

        if not validator.is_valid(adict=adict, schema=schema):
            invalid_req = InvalidRequestObject()
            invalid_req.parse_error(errors=validator.get_errors())
            return invalid_req

        data = validator.get_valid_data()

        return ListDepartmentRequestObject(data=data)

# class CreateDeparmentRequestObject(ValidRequestObject):
#     @classmethod
#     def from_dict(cls, adict, validator=None):
#         JSONSchemaLoader.load(path='config/schemas/json/', filename="*.json")
#         schema = JSONSchemaLoader.get("create_department")
#
#         if not validator.is_valid(adict=adict, schema=schema):
#             invalid_req = InvalidRequestObject()
#             invalid_req.parse_error(errors=validator.get_errors())
#             return invalid_req
#
#         data = validator.get_valid_data()
#
#         return CreateDeparmentRequestObject(data=data)
