from marshmallow import Schema, fields

class ListDepartment(Schema):
    id = fields.Int(attribute="id")
    name = fields.Str(attribute="name")
    status = fields.Str(attribute="status")
    createdAt = fields.Str(attribute="created_at")
    modifiedAt = fields.Str(attribute="modified_at")
