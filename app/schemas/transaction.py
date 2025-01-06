from marshmallow import Schema, fields
from .base import TransactionTypeValidator

class categorie:
    name= fields.Str(required=True)

class transaction_schema(Schema):
    budget_id = fields.Int(required=True)
    categorie_id= fields.Int()
    amount = fields.Float(required=True)
    comment= fields.Str()
    transaction_date = fields.DateTime()
    type = fields.Str(
        required=True,
        validate=TransactionTypeValidator
    )