from functools import wraps
from flask import g, request 
from flask_restful import abort


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get('Authorization', 'Token Null')
        token = [item.encode('ascii') for item in auth_header.split(' ')]
        if len(token) == 2 and token[0] == 'Token':
            user = User.verify_auth_token(token[1]) 
            if user:
                g.user = user
                return f(*args, **kwargs)
        abort(401, message='Invalid Token - Authorization Required')

    return decorated_function
