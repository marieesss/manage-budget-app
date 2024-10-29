from flask import Blueprint
from app.schemas import create_budget_payload
from app.utils.request import get_json_data, generate_response, validate_json_schema
from app.utils.decorators import user_required
from flask_jwt_extended import get_jwt
from app.services.budget import BudgetService




budget_route = Blueprint('budget route', __name__)


@budget_route.route('/', methods=['POST'])
@user_required()
def create_budget():

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
    



@budget_route.route('/', methods=['GET'])
@user_required()
def get_budgets():

    try:
        claims = get_jwt()

        res = BudgetService.get_user_budgets(email=claims["sub"])

        return generate_response(message=res, status=200)

    except Exception as e:
        return generate_response(message="An error occurred", status=500, error=e)
    

@budget_route.route('/<budget_id>', methods=['GET'])
@user_required()
def get_budget_by_id(budget_id):
    try:
        claims = get_jwt()
        res = BudgetService.get_budget_by_id(budget_id=budget_id, email=claims["sub"])

        return generate_response(message=res, status=200)

    except Exception as e:
        return generate_response(message="An error occurred", status=500, error=e)

