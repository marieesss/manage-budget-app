from app.db import db
from sqlalchemy.ext.hybrid import hybrid_property
from app.utils.hash import hash_password, verify_password
from .base import BaseTable


class User(BaseTable):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    firstname = db.Column(db.String(128), nullable=False)
    lastname = db.Column(db.String(128),nullable=False)
    _password = db.Column("password",db.String(128),nullable=False)


    #
    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = hash_password(password=password)

    def authenticate(self, password_to_check):
        res = verify_password(self._password, password_to_check)
        return res

    @classmethod
    def get_user_by_mail(self, email):
        return self.query.filter_by(email=email).first()    

        