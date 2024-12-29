from app.utils.decorators import user_required
from flask import Blueprint
from app.schemas import transaction_schema
from app.services import TransactionService
from app.utils.request import get_json_data, generate_response, validate_json_schema
from flask_jwt_extended import get_jwt
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


transaction_route = Blueprint('transaction route', __name__)

@transaction_route.route('/', methods=['POST'])
@user_required()
def create_transaction():

    try:
        json_data, error = get_json_data()

        if error:
            return generate_response(error, error="Bad request", status=400)

        validate_json_schema(json_data=json_data, schema=transaction_schema)

        res = TransactionService.create_transaction(budget_id =json_data["budget_id"], amount = json_data["amount"], categorie_id = json_data.get("categorie_id"), transaction_date=json_data.get("transaction_date"), type= json_data.get("type"), comment=json_data.get("comment"))

        return res

    except Exception as e:
        logger.error("An unexpected error occurred: %s", e)
        return generate_response(message="An error occurred", status=500, error=e)


