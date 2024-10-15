from app.db import db
from app.models.user import User
from app.utils.hash import verify_password
from app.utils.jwt import create_jwt
from flask_jwt_extended import create_access_token
from app.utils.request import generate_response
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


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
        
    def verify_user_login(email, password):
        try:
            user = User.get_user_by_mail(email=email)
            if not user :
                generate_response(message="Email not found", error="Bad Request", status=400)
            else : 
                logged = user.authenticate(password_to_check=password)
                return logged
        except Exception as error:
            print(error)
            raise error


      
      
