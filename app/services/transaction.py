from app.db import db
from datetime import datetime
from app.models.transaction import Transaction
from app.models.budget import Budget
from app.utils.request import generate_response
from sqlalchemy.exc import IntegrityError
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class TransactionService:
      
    def create_transaction(budget_id: int, amount : float, categorie_id: int= None, comment : str = None , transaction_date = datetime.now(), type : str = "expense"):
        """ Create a transaction

        Parameters
        -----------------

        Returns
        ----------
        Confirmation message 
        """
        try:
            transaction = Transaction(
                budget_id=budget_id,
                categorie_id= categorie_id, 
                amount= amount, 
                comment=comment,
                transaction_date=transaction_date, 
                type= type
            )
            try: 
                db.session.add(transaction)
                db.session.commit()
                return generate_response(message="Transaction created", status=200)   
            except IntegrityError:
                db.session.rollback()
                return generate_response(message="Transaction already exists", status=500) 
        except Exception as error:
            logger.error("An unexpected error occurred: %s", error)
            db.session.rollback()
            return generate_response(message="An unexpected error occurred", status=500, error=str(error))        

    def get_budget_transactions(budget_id: int, email: str):
        """Get an array of transactions for a specific budget, validating user ownership."""
        try:
            # Récupérer le budget
            budget = Budget.get_budget_id(budget_id)
            if not budget:
                return generate_response(message="Budget not found", status=404)

            # Vérifier si le budget est associé à l'utilisateur via l'email
            if budget.user.email != email:
                return generate_response(message="Unauthorized access to budget", status=403)

            # Récupérer les transactions associées au budget
            transactions = budget.transactions
            transaction_data = [
                {
                    "id": transaction.id,
                    "budget": budget.name,
                    "categorie": transaction.categorie.name if transaction.categorie else None,
                    "comment": transaction.comment,
                    "amount": float(transaction.amount),
                    "transaction_date": transaction.transaction_date.strftime('%Y-%m-%d %H:%M:%S'),
                    "type": transaction.type.name,
                }
                for transaction in transactions
            ]

            return generate_response(data=transaction_data, message="Transactions retrieved", status=200)

        except Exception as error:
            logger.error(f"An error occurred while retrieving budget transactions: {error}")
            return generate_response(message="An unexpected error occurred", status=500, error=str(error))
        

    def get_budget_transactions_by_categorie(budget_id: int, email: str, categorie : str):
        """Get an array of transactions for a specific budget and categorie """
        try:
            # Récupérer le budget
            budget = Budget.get_budget_id(budget_id)
            if not budget:
                return generate_response(message="Budget not found", status=404)

            # Vérifier si le budget est associé à l'utilisateur via l'email
            if budget.user.email != email:
                return generate_response(message="Unauthorized access to budget", status=403)

            # Récupérer les transactions associées au budget
            transactions = budget.get_budgets(transaction_type=categorie)
            transaction_data = [
                {
                    "id": transaction.id,
                    "budget": budget.name,
                    "categorie": transaction.categorie.name if transaction.categorie else None,
                    "comment": transaction.comment,
                    "amount": float(transaction.amount),
                    "transaction_date": transaction.transaction_date.strftime('%Y-%m-%d %H:%M:%S'),
                    "type": transaction.type.name,
                }
                for transaction in transactions
            ]

            return generate_response(data=transaction_data, message="Transactions retrieved", status=200)

        except Exception as error:
            logger.error(f"An error occurred while retrieving budget transactions: {error}")
            return generate_response(message="An unexpected error occurred", status=500, error=str(error))


