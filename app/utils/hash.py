import bcrypt 

def hash_password(password):
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)
    return hash

def verify_password(password, password_to_check):
    result = bcrypt.checkpw(password,password_to_check.encode('utf-8')) 
    return result
