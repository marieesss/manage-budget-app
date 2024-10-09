from flask import Blueprint
from app.schemas import auth_schema
from app.services.user import UserService
from app.utils.request import get_json_data, generate_response, validate_json_schema

auth_route = Blueprint('authentification route', __name__)

@auth_route.route('/register', methods=(['POST']))
def register():
        json_data, error = get_json_data()

        if error:
            return generate_response(error, error="Bad request", status=400)
        
        result = validate_json_schema(json_data=json_data, schema=auth_schema)

        try :
            existing_user = UserService.get_user_by_mail(result["email"])

            if existing_user:
                return generate_response(message="Mail already taken", status=400, error="Conflict")

            user = UserService.create_user(
                email=result["email"],
                firstname=result["firstname"],
                lastname=result["lastname"],
                password=result["password"]
            )

            return generate_response(message="User created", status=201)
        except Exception as e:
             return generate_response(message="An error occurred", status=500, error="Internal Server Error")
