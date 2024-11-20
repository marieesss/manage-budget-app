from app.utils.decorators import user_required
from flask import Blueprint
from app.schemas import categorie_schema
from app.services.categorie import CategorieService
from app.utils.request import get_json_data, generate_response, validate_json_schema
import logging

categorie_route = Blueprint('categorie route', __name__)

@categorie_route.route('/', methods=['POST'])
@user_required()
def create_categorie():

    try:
        json_data, error = get_json_data()

        if error:
            return generate_response(error, error="Bad request", status=400)

        validate_json_schema(json_data=json_data, schema=categorie_schema)

        res = CategorieService.create_categorie(name=json_data["name"], type=json_data["type"])

        return res

    except Exception as e:
        return generate_response(message="An error occurred during login", status=500, error=str(e))
    

@categorie_route.route('/', methods=['GET'])
@user_required()
def get_categories():
    try:
        res = CategorieService.get_all_categories()

        return generate_response(data=res, status=200)

    except Exception as e:
        return generate_response(message="An error occurred", status=500, error=str(e))
    

@categorie_route.route('/<categorie_type>', methods=['GET'])
@user_required()
def get_categories_by_type(categorie_type):
    try:
        res = CategorieService.get_all_categories_by_type(categorie_type=categorie_type)
        
        return generate_response(data=res, status=200)

    except Exception as e:
        return generate_response(message="An error occurred", status=500, error=str(e))


