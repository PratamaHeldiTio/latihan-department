from marshmallow import Schema, fields

class ListArticleToJsonFormat(Schema):
    id = fields.Int(attribute="id")
    title = fields.Str(attribute="title")
    content = fields.Str(attribute="content")
    createdAt = fields.Str(attribute='created_at')
    modifiedAt = fields.Str(attribute='modified_at')
    createdBy = fields.Str(attribute='created_by')
    modifiedBy = fields.Str(attribute='modified_by')


class ListArticleToVariavleFormat(Schema):
    id = fields.Int(attribute="id")
    title = fields.Str(attribute="title")
    content = fields.Str(attribute="content")
    created_at = fields.Str(attribute='createdAt')
    modified_at = fields.Str(attribute='modifiedAt')
    created_by = fields.Str(attribute='createdBy')
    modified_by = fields.Str(attribute='modifiedBy')
