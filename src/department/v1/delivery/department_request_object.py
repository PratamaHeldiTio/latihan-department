from src.shared import helper
from src.shared.request_object import ValidRequestObject, InvalidRequestObject

class ListDepartmentRequestObject(ValidRequestObject):
    def __init__(self, title):
        self.title = title

    @classmethod
    def from_dict(cls, adict, validator):
        schema = {
            'title': {
                'type': 'string',
                'required': False,
            }
        }

        if not validator.is_valid(adict=adict, schema=schema):
            invalid_req = InvalidRequestObject()
            invalid_req.parse_error(errors=validator.get_errors())
            return invalid_req

        data = validator.get_valid_data()

        return ListDepartmentRequestObject(
            title=helper.get_value_from_dict(data, 'title', '')
        )

    def __nonzero__(self):
        return True
