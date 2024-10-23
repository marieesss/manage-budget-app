from app.models.user import User
from app.utils.jwt import create_jwt
from app.utils.request import generate_response
from app.utils.jwt import create_jwt
from flask import jsonify


class BudgetService:
      
    def create_budget(email : str, name):
        """ Create an user budget

        Parameters
        -----------------
        token : token provided by user
        name : name given

        Returns
        ----------
        Confirmation message 
        """
        try:
            return generate_response(message="Login Hello", status=200)
        except Exception as error:
            print(error)
            raise error
        
      
