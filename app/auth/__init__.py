from uuid import uuid4
import base64
import hashlib
import bcrypt
from haveibeenpwnd import check_password
from ..models import User

class AuthError(Exception):
    def __init__(self, message):
        self.message = message

def encode(password):
    # return base64.b64encode(hashlib.sha256(password).digest())
    return password

def is_safe(password):
    if check_password(password)['count'] != 0:
        raise AuthError('password is weak')
    return True

def sign_up(name, email, password):
    is_safe(password)
    if User.query.filter(User.email == email).first() is not None:
        raise AuthError('email already registired')
    pw = password.encode('utf-8')
    hashed = bcrypt.hashpw(encode(pw), bcrypt.gensalt())
    try:
        token = str(uuid4())
        user = User(name, email, hashed.decode(), token)
        user.add()
    except Exception: raise AuthError('try again')
    return True

def sign_in(email, password):
    pw = bytes(password, 'utf-8')
    user = User.query.filter(User.email==email).first()
    if user is None: raise AuthError('email not found')
    if bcrypt.checkpw(encode(pw), str(user.password).encode('utf-8')):
        return user.token
    else:
        return AuthError('invalid token')

def get_by_token(token):
    user = User.query.filter(User.token == token).first()
    if user is None: AuthError('hacker, you can\'t do it anyway :)')
    return user

