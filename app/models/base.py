from app.db import db
from datetime import datetime
import enum


class BaseTable(db.Model):
    __abstract__ = True
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)


class TypeEnum(enum.Enum):
    expense = "expense"
    income = "income"