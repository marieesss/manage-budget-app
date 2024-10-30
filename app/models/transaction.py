from app.db import db
from sqlalchemy.ext.hybrid import hybrid_property
from .base import BaseTable, TypeEnum
from datetime import datetime


class Transaction(BaseTable):
    __tablename__ = "transaction"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    budget_id = db.Column(db.String(128), db.ForeignKey('budget.id'), nullable=False)
    categorie_id = db.Column(db.String(128), db.ForeignKey('categorie.id'))
    amount = db.Column(db.DECIMAL(10,2), nullable=False)
    transaction_date = db.Column(db.DateTime, default=datetime.now,  nullable=False)
    type = db.Column(db.Enum(TypeEnum), default=TypeEnum.expense,  nullable=False)
    categorie = db.relationship("Categorie", backref="transaction")
