from app.db import db
from app.models.user import User
from app.utils.hash import verify_password
from app.utils.jwt import create_jwt
from app.utils.request import generate_response
from app.utils.jwt import create_jwt
from flask import jsonify
from app.schemas.user import auth_schema


class UserService:
      
    def login(email : str, password : str):
        """ Log user

        Parameters
        -----------------
        email : email provided
        password : password provided

        Returns
        ----------
        token 
        """
        try:
            user = User.get_user_by_mail(email=email)
            if user is None :
                return generate_response(message="Email not found", error="Bad Request", status=400)
            else : 
                logged = user.authenticate(password_to_check=password)
                if logged:
                    token = create_jwt(data=email)
                    return generate_response(message="Login successful", data=token, status=200)
                else:
                    return generate_response(message="Wrong password", error="Unauthorized", status=401)
        except Exception as error:
            print(error)
            raise error
        
        
    def register(user : auth_schema):
        """ Create user and hash password

        Parameters
        -----------------
        email : email provided
        password : password provided
        firstname : firstname
        lastname : lastname

        Returns
        ----------
        token 
        """
                
        existing_user = User.get_user_by_mail(email=user["email"])
        if existing_user:
            return generate_response(message="Mail already taken", status=400, error="Conflict")
        try:
            user = User(
                email=user["email"],
                firstname=user["firstname"],
                lastname=user["lastname"],
                password=user["password"]
            )
            db.session.add(user)
            db.session.commit()

            return generate_response(message="User created", status=201)

        except Exception as error:
            db.session.rollback()
            return error


      
      
