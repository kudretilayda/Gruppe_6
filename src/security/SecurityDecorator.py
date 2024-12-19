# src/server/security/SecurityHandler.py

import firebase_admin
from firebase_admin import credentials, auth
import os
from ..config import Config

class SecurityHandler:
    """Handler für die Firebase-Initialisierung und Token-Validierung"""
    
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SecurityHandler, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
            
        cred = credentials.Certificate(Config.FIREBASE_CONFIG)
        self.app = firebase_admin.initialize_app(cred)
        self._initialized = True

    def verify_token(self, token):
        """Validiert einen Firebase Token"""
        try:
            decoded_token = auth.verify_id_token(token)
            return decoded_token
        except Exception as e:
            raise ValueError(f"Invalid token: {str(e)}")

# src/server/security/SecurityDecorator.py

from functools import wraps
from flask import request
from .SecurityDecorator import SecurityHandler

class SecurityDecorator:
    """Decorator für die Token-Validierung"""

    @staticmethod
    def check_valid_token(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not 'Authorization' in request.headers:
                return {'error': 'No Authorization header'}, 401

            token = request.headers['Authorization']
            if token.startswith('Bearer '):
                token = token.split(' ')[1]

            try:
                handler = SecurityHandler()
                decoded_token = handler.verify_token(token)
                request.user = decoded_token
                return f(*args, **kwargs)
            except ValueError as e:
                return {'error': str(e)}, 401

        return decorated_function