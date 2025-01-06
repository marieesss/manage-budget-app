from flask import Blueprint
from app.schemas import auth_schema, login_schema
from app.services.user import UserService
from app.utils.request import get_json_data, generate_response, validate_json_schema

auth_route = Blueprint('authentification route', __name__)

@auth_route.route('/register', methods=['POST'])
def register():
    try:
        json_data, error = get_json_data()

        if error:
            return generate_response(error, error="Bad request", status=400)

        validate_json_schema(json_data=json_data, schema=auth_schema)

        res = UserService.register(json_data)

        return res

    except Exception as e:
        return generate_response(message="An error occurred", status=500, error="Internal Server Error")


@auth_route.route('/login', methods=(['POST']))
def login():
    json_data, error = get_json_data()
    if error:
        return generate_response(message="Bad request", error=error, status=400)
    data = validate_json_schema(json_data=json_data, schema=login_schema)
    try:
        res = UserService.login(email=data["email"], password=data["password"])
        return res
    except Exception as e:
        return generate_response(message="An error occurred during login", status=500, error=str(e))

