from app.db import db
from .base import BaseTable, TypeEnum

class Categorie(BaseTable):
    __tablename__ = "categorie"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.Enum(TypeEnum), default=TypeEnum.expense,  nullable=False)
    name = db.Column(db.String(128), nullable=False)
    __table_args__ = (db.UniqueConstraint('type', 'name', name='categorie_type_name_unique'),)

    @classmethod
    def get_all_categories(self):
        return self.query.all()
    @classmethod
    def get_all_categories_by_type(self, categorie_type):
        return self.query.filter_by(type=categorie_type)