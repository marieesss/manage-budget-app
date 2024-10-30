from marshmallow import Schema, fields

class categorie:
    name= fields.Str(required=True)

class transaction_schema(Schema):
    budget_id = fields.Int(required=True)
    categore = fields.Str(required=True)
    lastname = fields.Str(required=True)
    password = fields.Str(required=True)