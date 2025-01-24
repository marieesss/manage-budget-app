from flask import request, jsonify
from marshmallow import ValidationError

def get_json_data():
    """Load responses"""
    json_data = request.get_json()
    if not json_data:
        return None, "No input data provided"
    return json_data, None

def generate_response(message=None, data=None, error=None, status=200):
    """Generate response"""
    return {
        "message": message,
        "data": data,
        "error": error
    }, status


def validate_json_schema(schema, json_data):
    """Validate request schema"""
    try:
        schema().load(json_data)
        return None
    except ValidationError as err:
        return generate_response(
            message="Invalid request data",
            status=400,
            error=err.messages
        ) 

