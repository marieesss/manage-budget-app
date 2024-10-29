from app.models.user import User
from app.db import db
from app.models.budget import Budget
from app.utils.request import generate_response


class BudgetService:
      
    def create_budget(email : str, name : str):
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
            user_id = User.get_user_by_mail(email=email)
            if not user_id:
                return generate_response(message="User not found", status=400, error="Conflict")
            budget = Budget(
                name=name,
                user_id=user_id.id
            )

            db.session.add(budget)
            db.session.commit()
            return "created"
        except Exception as error:
            print(error)
            raise error
        
    def get_user_budgets(email : str):
        """ Get an array of budget

        Parameters
        -----------------
        token : token provided by user

        Returns
        ----------
        Array : 
            id
            name
            created_at
        """
        try:
            user = User.get_user_by_mail(email=email)
            if not user:
                return generate_response(message="User not found", status=400, error="Conflict")
            else:
                budgets = user.get_budgets()
                budget_data=[]
                for budget in budgets:
                    budget_data.append({"id": budget.id, "name": budget.name, "created_at": budget.created_at})
                return budget_data
        except Exception as error:
            print(error)
            raise error
        
    def get_budget_by_id(budget_id: int, email : str):
        """ Get a budget

        Parameters
        -----------------
        token : token provided by user

        Returns
        ----------
        Array : 
            id
            name
            created_at
        """
        try:
            budget = Budget.get_budget_id(id=budget_id)
            if not budget: 
                return generate_response(message="Budget not found", status=400, error="Conflict")
            elif not budget.user.email == email:
                return generate_response(message="This is not your budget", status=401, error="Conflict")
            return {"budget" : budget.name }
        except Exception as error:
            print(error)
            raise error
        
      
