# src/server/utils/app_config.py

class AppConfig:
    """Konfigurationsklasse für die Anwendung."""
    
    # Flask-App Konfiguration
    FLASK_APP_SECRET = 'your-secret-key'  # In Produktion aus Umgebungsvariablen laden
    FLASK_DEBUG = True  # In Produktion auf False setzen
    
    # CORS Konfiguration
    CORS_ORIGINS = ["http://localhost:3000"]  # Frontend URLs
    
    # Firebase Konfiguration
    FIREBASE_CONFIG = {
        "apiKey": "your-api-key",
        "authDomain": "your-auth-domain",
        "projectId": "your-project-id",
        "storageBucket": "your-storage-bucket",
        "messagingSenderId": "your-messaging-sender-id",
        "appId": "your-app-id"
    }

# src/server/utils/security_config.py

from functools import wraps
from flask import request, abort
import firebase_admin
from firebase_admin import credentials, auth

class SecurityConfig:
    """Konfigurationsklasse für die Sicherheit."""
    
    _instance = None
    _initialized = False
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SecurityConfig, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not SecurityConfig._initialized:
            # Firebase Admin SDK initialisieren
            try:
                cred = credentials.Certificate('path/to/serviceAccount.json')
                firebase_admin.initialize_app(cred)
            except ValueError:
                # App bereits initialisiert
                pass
            SecurityConfig._initialized = True
    
    @staticmethod
    def check_auth():
        """Decorator für Firebase Authentication."""
        def decorator(f):
            @wraps(f)
            def decorated_function(*args, **kwargs):
                auth_header = request.headers.get('Authorization')
                if not auth_header:
                    abort(401, 'No authorization header')
                
                try:
                    # "Bearer" vom Token entfernen
                    token = auth_header.split(' ')[1]
                    # Token verifizieren
                    decoded_token = auth.verify_id_token(token)
                    # User-ID zum Request hinzufügen
                    request.user = decoded_token
                    return f(*args, **kwargs)
                except Exception as e:
                    abort(401, str(e))
            
            return decorated_function
        return decorator