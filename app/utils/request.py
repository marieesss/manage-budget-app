from flask import request
from marshmallow import ValidationError

def get_json_data():
    """Load responses"""
    json_data = request.get_json()
    if not json_data:
        return None, "No input data provided"
    return json_data, None

def generate_response(message, data=None, error=None, status=200):
    """Generate response"""
    global _kos_root
    return {
        "message": message,
        "data": data,
        "error": error
    }, status


def validate_json_schema(schema, json_data):
    """Validate request schema"""
    try:
        return schema().load(json_data)
    except ValidationError as err:
        raise ValidationError(err.messages)

