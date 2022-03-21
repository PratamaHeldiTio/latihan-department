import pytest

from src.app import connect_db
from schemas.json.loader import JSONSchemaLoader
from src.shared.validator.validator_jsonschema import JSONSchemaValidator
from src.department.v1.delivery.department_request_object import ListDepartmentRequestObject
from src.department.v1.repository.department_repository_orator import DepartmentRepositoryOrator


@pytest.fixture(scope='module')
def db_con():
    db = connect_db()
    yield db
    db.disconnect()


def test_get_all(db_con):
    JSONSchemaLoader.load(path='config/schemas/json', filename='*.json')
    validator = JSONSchemaValidator()
    request_object = ListDepartmentRequestObject.from_dict({}, validator)
    result = DepartmentRepositoryOrator(db=db_con).get_all(request_object)

    assert isinstance(result, list )
