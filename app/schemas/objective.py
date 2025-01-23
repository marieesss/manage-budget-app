from marshmallow import Schema, fields
from .base import TransactionTypeValidator

class categorie:
    name= fields.Str(required=True)

class objective_schema(Schema):
    budget_id = fields.Int(required=True)
    categorie_id= fields.Int(required=True)
    name= fields.Str(required=True)
    amount = fields.Float(required=True)
    type = fields.Str(
        required=True,
        validate=TransactionTypeValidator
    )