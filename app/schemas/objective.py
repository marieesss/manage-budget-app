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

class objective_update_schema(Schema):
    budget_id = fields.Int(required=True, error_messages={"required": "Field 'budget_id' is required."})
    objective_id = fields.Int(required=True ,  error_messages={"required": "Field 'objective_id' is required."})
    categorie_id= fields.Int(required=True, error_messages={"required": "Field 'categorie_id' is required."})
    name= fields.Str(required=True, error_messages={"required": "Field 'name' is required."})
    amount = fields.Float(required=True, error_messages={"required": "Field 'amount' is required."})
    type = fields.Str(
        required=True,
        validate=TransactionTypeValidator, 
        error_messages={"required": "Field 'type' is required."}
    )
