from functools import wraps
from flask_jwt_extended import verify_jwt_in_request
from flask_jwt_extended import get_jwt
from flask import jsonify
import logging



def admin_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims["is_administrator"]:
                logging.info(claims)
                return fn(*args, **kwargs)
            else:
                return jsonify(msg="Admins only!"), 403

        return decorator

    return wrapper


def user_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            logging.info(f"here")
            verify_jwt_in_request()
            claims = get_jwt()
            logging.info(f"Admin access by: {claims}")
            if claims["is_user"]:
                logging.info(f"Admin access by: {claims}")
                return fn(*args, **kwargs)
            else:
                return jsonify(msg="Admins only!"), 403

        return decorator

    return wrapper