from marshmallow import Schema, fields, validate, ValidationError

class categorie_schema(Schema):
    name= fields.Str(required=True)
    type = fields.Str(
        required=True,
        validate=validate.OneOf(["expense", "income"], error="Type must be 'expense' or 'income'.")
    )