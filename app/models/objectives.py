from app.db import db
from .base import BaseTable, TypeEnum


class Objective(BaseTable):
    __tablename__ = "budget_objective"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    budget_id = db.Column(db.String(128), db.ForeignKey('budget.id'), nullable=False)
    categorie_id = db.Column(db.String(128), db.ForeignKey('categorie.id'))
    amount = db.Column(db.DECIMAL(10,2), nullable=False)
    name = db.Column(db.String(128), nullable=False)
    type = db.Column(db.Enum(TypeEnum), default=TypeEnum.expense,  nullable=False)
    categorie = db.relationship("Categorie", backref="objectives")


    @classmethod
    def get_by_objective_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def get_all_budget_objective(cls, id):
        return cls.query.filter_by(budget_id=id).all()
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()