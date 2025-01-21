from app.db import db
from .base import BaseTable, TypeEnum
from datetime import datetime
from datetime import datetime
from sqlalchemy import extract





class Transaction(BaseTable):
    __tablename__ = "transaction"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    budget_id = db.Column(db.String(128), db.ForeignKey('budget.id'), nullable=False)
    categorie_id = db.Column(db.String(128), db.ForeignKey('categorie.id'))
    comment = db.Column(db.String(255))
    amount = db.Column(db.DECIMAL(10,2), nullable=False)
    transaction_date = db.Column(db.DateTime, default=datetime.now,  nullable=False)
    type = db.Column(db.Enum(TypeEnum), default=TypeEnum.expense,  nullable=False)
    categorie = db.relationship("Categorie", backref="transaction")
    
    @classmethod
    def get_transactions_month(cls, budget_id : int, type : str =None, year_asked : int=None, month_asked : int = None):
        # Get today date
        date = datetime.now()

        # Set month and year depending if it is provided
        year = year_asked if year_asked else date.year
        month = month_asked if month_asked else date.month

        results = cls.query.filter(cls.budget_id==budget_id, 
                                            extract('year', cls.transaction_date) == year,
                                            extract('month', cls.transaction_date) == month
        
                                           )
        # Filter by type if needed
        if type:
            results = results.filter(cls.type == type)

        transactions = results.all()

        return transactions

