from app.db import db
from app.models.user import User

class UserService:
    def create_user(email, firstname, lastname, password):
        try:
            user = User(
                email=email,
                firstname=firstname,
                lastname=lastname,
                password=password
            )
            db.session.add(user)
            db.session.commit()

            return user

        except Exception as error:
            db.session.rollback()
            return error
        
    def get_user_by_mail(email):
        try:
            return User.query.filter_by(email=email).first()
        except Exception as error:
            db.session.rollback()
            return error
      
      
