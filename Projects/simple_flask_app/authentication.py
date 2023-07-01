import bcrypt

def hash_password(pswd):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(pswd.encode('utf-8'), salt)

def validate_password(pswd, hash):
    return bcrypt.checkpw(pswd.encode('utf-8'), hash)