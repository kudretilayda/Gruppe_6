from functools import wraps
from flask import request
from google.oauth2 import id_token
from google.auth.transport import requests
import os

def require_auth(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return {'message': 'No token provided'}, 401
        try:
            token = auth_header.split(' ')[1]
            idinfo = id_token.verify_oauth2_token(
                token, requests.Request(), os.getenv('GOOGLE_CLIENT_ID'))
            if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
                raise ValueError('Invalid issuer')
            request.user = idinfo
            return f(*args, **kwargs)
        except Exception as e:
            return {'message': 'Invalid token'}, 401
    return decorated_function