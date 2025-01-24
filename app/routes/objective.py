from app.utils.decorators import user_required
from flask import Blueprint
from app.utils.request import get_json_data, generate_response, validate_json_schema
from flask_jwt_extended import get_jwt
from app.schemas.objective import objective_schema, objective_update_schema
from app.services.objective import ObjectiveService
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


objective_route = Blueprint('objectives route', __name__)

@objective_route.route('/', methods=['POST'])
@user_required()
def create_objective():

    try:
        json_data, error = get_json_data()

        if error:
            return generate_response(error, error="Bad request", status=400)
        

        logger.info(json_data)


        validation_error = validate_json_schema(json_data=json_data, schema=objective_schema)
        if validation_error:
            return validation_error 

        res = ObjectiveService.create_objective(budget_id =json_data["budget_id"],
                                                amount = json_data["amount"], 
                                                name = json_data["name"], 
                                                categorie_id = json_data["categorie_id"], 
                                                type= json_data["type"])
        return res

    except Exception as e:
        logger.error("An unexpected error occurred: %s", e)
        return generate_response(message="An error occurred", status=500, error=e)
    


@objective_route.route('/<budget_id>', methods=['GET'])
@objective_route.route('/<budget_id>/<type>', methods=['GET'])
@user_required()
def get_objectives(budget_id : int, type : str = None):
    try:
        claims = get_jwt()

        res = ObjectiveService.get_budget_objectives(budget_id=budget_id, email=claims["sub"], type= type)

        return res
    except Exception as e:
        logger.error("An unexpected error occurred: %s", e)
        return generate_response(message="An error occurred", status=500, error=e)
    
@objective_route.route('/', methods=['PUT'])
@user_required()
def update_objectives():

    try:
        claims = get_jwt()
        json_data, error = get_json_data()

        if error:
            return generate_response(error, error="Bad request", status=400)
        

        validation_error = validate_json_schema(json_data=json_data, schema=objective_update_schema)
        if validation_error:
            return validation_error 

        res = ObjectiveService.update_objective(budget_id =json_data["budget_id"],
                                                objective_id=json_data["objective_id"], 
                                                amount = json_data["amount"], 
                                                name = json_data["name"], 
                                                categorie_id = json_data["categorie_id"], 
                                                type= json_data["type"], 
                                                email=claims["sub"])
        return res

    except Exception as e:
        logger.error("An unexpected error occurred: %s", e)
        return generate_response(message="An error occurred", status=500, error=e)
    


@objective_route.route('/<objective_id>', methods=['DELETE'])
@user_required()
def delete_objective(objective_id : int, type : str = None):
    try:
        claims = get_jwt()

        res = ObjectiveService.delete_objective(objective_id=objective_id, email=claims["sub"])

        return res
    except Exception as e:
        logger.error("An unexpected error occurred: %s", e)
        return generate_response(message="An error occurred", status=500, error=e)
    
