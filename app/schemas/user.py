from marshmallow import Schema, fields


class auth_schema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    firstname = fields.Str(required=True)
    lastname = fields.Str(required=True)
    password = fields.Str(required=True)
