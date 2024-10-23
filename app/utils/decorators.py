from functools import wraps
from flask_jwt_extended import verify_jwt_in_request
from flask_jwt_extended import get_jwt
from flask import jsonify
from app.utils.request import generate_response



def admin_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims.get("is_admin", False):
                return fn(*args, **kwargs)
            else:
                return generate_response(message="Wrong token", error="Unauthorized", status=401)

        return decorator

    return wrapper


def user_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims.get("is_user", False):
                return fn(*args, **kwargs)
            else:
                return generate_response(message="Wrong token", error="Unauthorized", status=401)

        return decorator

    return wrapper