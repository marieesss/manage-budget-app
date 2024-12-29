from marshmallow import Schema, fields, validate, ValidationError
from .base import TransactionTypeValidator
class categorie_schema(Schema):
    name= fields.Str(required=True)
    type = fields.Str(
        required=True,
        validate=TransactionTypeValidator
    )