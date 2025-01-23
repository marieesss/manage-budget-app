from app.db import db
from .base import BaseTable, TypeEnum
from datetime import datetime
from datetime import datetime
from sqlalchemy import extract


class Objective(BaseTable):
    __tablename__ = "budget_objective"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    budget_id = db.Column(db.String(128), db.ForeignKey('budget.id'), nullable=False)
    categorie_id = db.Column(db.String(128), db.ForeignKey('categorie.id'))
    amount = db.Column(db.DECIMAL(10,2), nullable=False)
    name = db.Column(db.String(128), nullable=False)
    type = db.Column(db.Enum(TypeEnum), default=TypeEnum.expense,  nullable=False)
    categorie = db.relationship("Categorie", backref="objectives")
    
