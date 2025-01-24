from app.db import db
from datetime import datetime, timezone
from app.models.objectives import Objective
from app.models.budget import Budget
from app.utils.request import generate_response
from sqlalchemy.exc import IntegrityError
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class ObjectiveService:
      
    def create_objective(name: str, budget_id: int, amount : float, categorie_id: int, type : str = "expense"):
        """ Create a transaction

        Parameters
        -----------------

        Returns
        ----------
        Confirmation message 
        """
        try:
            objective = Objective(
                budget_id=budget_id,
                name= name,
                categorie_id= categorie_id, 
                amount= amount, 
                type= type
            )
            try: 
                objective.save()
                return generate_response(message="Objective created", status=200)   
            except IntegrityError:
                db.session.rollback()
                return generate_response(message="Objective already exists", status=500) 
        except Exception as error:
            logger.error("An unexpected error occurred: %s", error)
            db.session.rollback()
            return generate_response(message="An unexpected error occurred", status=500, error=str(error))     



    def get_budget_objectives(budget_id: int, email : str, type : str = None):
        """ get budget Objectives

        Parameters
        -----------------

        Returns
        ----------
        Array of objectives
        """
        try:
            budget = Budget.get_budget_id(id=budget_id)
            if not budget: 
                return generate_response(message="Budget not found", status=400, error="Conflict")
            elif not budget.user.email == email:
                return generate_response(message="This is not your budget", status=401, error="Conflict")
            
            budget_objectives = Objective.get_all_budget_objective(id=budget_id)

            objectives_data = [
            {
                "id": obj.id,
                "budget_id": obj.budget_id,
                "categorie_id": obj.categorie_id,
                "amount": obj.amount,
                "name": obj.name,
                "type": obj.type.name
            } 
            for obj in budget_objectives
        ]
            return generate_response(data=objectives_data, message="Objectives retrieved successfully", status=200)

        except Exception as error:
            logger.error("An unexpected error occurred: %s", error)
            db.session.rollback()
            return generate_response(message="An unexpected error occurred", status=500, error=str(error))
        
    def update_objective(name: str, budget_id: int, amount : float, categorie_id: int, email : str, objective_id: int,  type : str = "expense"):
        """ Update budget objectives

        Parameters
        -----------------

        Returns
        ----------
        Confirmation message 
        """

        try:
            budget = Budget.get_budget_id(id=budget_id)
            if not budget: 
                return generate_response(message="Budget not found", status=400, error="Conflict")
            elif not budget.user.email == email:
                return generate_response(message="This is not your budget objectives", status=401, error="Conflict")
            
            objective_to_update= Objective.get_by_objective_id(id=objective_id)


            if not objective_to_update :
                return generate_response(message="Objective not found", status=400, error="Conflict")
            
            objective_to_update.budget_id = budget_id
            objective_to_update.name = name
            objective_to_update.categorie_id = categorie_id
            objective_to_update.amount = amount
            objective_to_update.type = type


            objective_to_update.update()


            return generate_response(data="Updated value", message="Objectives retrieved successfully", status=200)

        except Exception as error:
            logger.error("An unexpected error occurred: %s", error)
            db.session.rollback()
            return generate_response(message="An unexpected error occurred", status=500, error=str(error))
        

    def delete_objective(email : str, objective_id : str):
        """ Update budget objectives

        Parameters
        -----------------

        Returns
        ----------
        Confirmation message 
        """

        try:
            objective = Objective.get_by_objective_id(id=objective_id)
            
            if not objective: 
                return generate_response(message="Budget not found", status=400, error="Conflict")
            elif not objective.objective_budget.user.email == email:
                return generate_response(message="This is not your budget objectives", status=401, error="Conflict")
            
            objective.delete()

            return generate_response(data="Objective deleted", message="Objectives retrieved successfully", status=200)

        except Exception as error:
            logger.error("An unexpected error occurred: %s", error)
            db.session.rollback()
            return generate_response(message="An unexpected error occurred", status=500, error=str(error))






