from flask_jwt_extended import create_access_token

def create_jwt(data):
    return create_access_token(identity=data)