from flask_jwt_extended import create_access_token

def create_jwt(data, role="user"):
    if role == "admin":
        additional_claims = {
            "is_administator": True
        }
    else:
        additional_claims = {
            "is_user": True
        }
    return create_access_token(identity=data, additional_claims=additional_claims)