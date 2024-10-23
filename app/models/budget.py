from app.db import db
from sqlalchemy.ext.hybrid import hybrid_property
from .base import BaseTable


class Budget(BaseTable):
    __tablename__ = "budget"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.String(128), db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(128), nullable=False)

        