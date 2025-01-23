from app.db import db
from sqlalchemy.ext.hybrid import hybrid_property
from .base import BaseTable


class Budget(BaseTable):
    __tablename__ = "budget"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.String(128), db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(128), nullable=False)
    transactions = db.relationship("Transaction", backref="budget")
    objectives = db.relationship("Objective", backref="objective_budget")



    @classmethod    
    def get_budget_id(self, id : int):
        return self.query.filter_by(id=id).first() 
          
    def get_budgets(self, transaction_type=None):
        if transaction_type:
            return [transaction for transaction in self.transactions if transaction.type.name == transaction_type]
        return self.transactions
    
    def get_budget_objectives (self, objective_type = None):
        if objective_type:
            return [objective for objective in self.objectives if objective.type.name == objective_type]
        return self.objectives
        



        