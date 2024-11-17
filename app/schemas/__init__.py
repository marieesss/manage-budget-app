from .user import auth_schema, login_schema
from .budget import create_budget_payload
from marshmallow import Schema, fields, validate
from .transaction import transaction_schema


# used in categorie or transaction
class type_payload(Schema):
    type = fields.Str(validate=validate.OneOf(["read", "write"]))