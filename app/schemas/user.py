from marshmallow import Schema, fields


class auth_schema(Schema):
    email = fields.Email(required=True)
    firstname = fields.Str(required=True)
    lastname = fields.Str(required=True)
    password = fields.Str(required=True)


class login_schema(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True)
