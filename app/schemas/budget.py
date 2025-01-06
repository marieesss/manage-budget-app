from marshmallow import Schema, fields


class create_budget_payload(Schema):
    name = fields.Str(required=True)
