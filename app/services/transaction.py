from app.db import db
from datetime import datetime
from app.models.transaction import Transaction
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
        
 
        
      
