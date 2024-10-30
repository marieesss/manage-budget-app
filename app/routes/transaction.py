from app.utils.decorators import user_required
from flask import Blueprint
from app.schemas import auth_schema, login_schema
from app.services.user import UserService
from app.utils.request import get_json_data, generate_response, validate_json_schema
from flask_jwt_extended import get_jwt


transaction_route = Blueprint('transaction route', __name__)

@transaction_route.route('/', methods=['POST'])
@user_required()
def create_transaction():

    try:
        json_data, error = get_json_data()
        claims = get_jwt()

        if error:
            return generate_response(error, error="Bad request", status=400)

        validate_json_schema(json_data=json_data, schema=create_budget_payload)

        res = BudgetService.create_budget(email=claims["sub"], name=json_data["name"])

        return generate_response(message=res, status=200)

    except Exception as e:
        return generate_response(message="An error occurred", status=500, error=e)


