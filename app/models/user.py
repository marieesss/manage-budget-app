from db.connect import db
from sqlalchemy.ext.hybrid import hybrid_property
from utils.hash import hash_password, verify_password


class User(db.Model):
    __tablename__ = "user"
    user_id = db.Column(db.Integer, primary_key=True, )
    email = db.Column(db.String(128), unique=True, nullable=False)
    firstname = db.Column(db.String(128), nullable=False)
    lastname = db.Column(db.String(128),nullable=False)
    _password = db.Column("password",db.String(128),nullable=False)
    created_at = db.Column(db.DateTime, default=db.datetime.now)


    #
    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = hash_password(password=password)

    def authenticate(self, password_to_check):
        return verify_password(password=self._password, password_to_check=password_to_check)

        