from app.db import db
from .base import BaseTable, TypeEnum

class Categorie(BaseTable):
    __tablename__ = "categorie"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.Enum(TypeEnum), default=TypeEnum.expense,  nullable=False)
    name = db.Column(db.String(128), nullable=False)