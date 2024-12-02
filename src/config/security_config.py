# src/server/utils/security_config.py

from functools import wraps
from flask import request, abort
import firebase_admin
from firebase_admin import auth
import os
from datetime import datetime, timedelta
import jwt
from config.firebase_config import FirebaseConfig

class SecurityConfig:
    """Konfigurationsklasse für die Sicherheit der Anwendung."""
    
    _instance = None
    _initialized = False
    SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'your-secret-key')  # In Produktion aus Umgebungsvariablen

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SecurityConfig, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not SecurityConfig._initialized:
            self.firebase = FirebaseConfig()
            SecurityConfig._initialized = True

    @staticmethod
    def check_auth(token):
        """Überprüft den Firebase Authentication Token."""
        try:
            # Token validieren
            decoded_token = auth.verify_id_token(token)
            
            # Token-Ablaufzeit prüfen
            exp = decoded_token.get('exp')
            if exp:
                now = datetime.utcnow()
                exp_datetime = datetime.fromtimestamp(exp)
                if now > exp_datetime:
                    raise ValueError("Token ist abgelaufen")
            
            return decoded_token
        except Exception as e:
            raise ValueError(f"Ungültiger Token: {str(e)}")

    @staticmethod
    def create_access_token(user_id, expires_delta=timedelta(hours=1)):
        """Erstellt einen JWT Access Token."""
        expire = datetime.utcnow() + expires_delta
        token_data = {
            'user_id': user_id,
            'exp': expire,
            'iat': datetime.utcnow()
        }
        return jwt.encode(token_data, SecurityConfig.SECRET_KEY, algorithm='HS256')

    @staticmethod
    def get_current_user():
        """Holt den aktuellen Benutzer aus dem Token."""
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return None
        
        try:
            token = auth_header.split(' ')[1]
            decoded_token = SecurityConfig.check_auth(token)
            return decoded_token
        except Exception:
            return None

    @staticmethod
    def requires_auth(f):
        """Decorator für geschützte Routen."""
        @wraps(f)
        def decorated(*args, **kwargs):
            auth_header = request.headers.get('Authorization')
            if not auth_header:
                abort(401, description="Keine Autorisierung vorhanden")

            try:
                token = auth_header.split(' ')[1]
                decoded_token = SecurityConfig.check_auth(token)
                # Token-Informationen dem Request hinzufügen
                request.user = decoded_token
                return f(*args, **kwargs)
            except ValueError as e:
                abort(401, description=str(e))
            except Exception as e:
                abort(500, description=f"Interner Server-Fehler: {str(e)}")

        return decorated

    @staticmethod
    def requires_roles(*roles):
        """Decorator für rollenbasierte Zugriffskontrolle."""
        def wrapper(f):
            @wraps(f)
            def wrapped(*args, **kwargs):
                auth_header = request.headers.get('Authorization')
                if not auth_header:
                    abort(401, description="Keine Autorisierung vorhanden")

                try:
                    token = auth_header.split(' ')[1]
                    decoded_token = SecurityConfig.check_auth(token)
                    
                    # Rollen aus Custom Claims prüfen
                    user_roles = decoded_token.get('roles', [])
                    if not any(role in user_roles for role in roles):
                        abort(403, description="Keine ausreichende Berechtigung")
                    
                    request.user = decoded_token
                    return f(*args, **kwargs)
                except Exception as e:
                    abort(401, description=str(e))
            
            return wrapped
        return wrapper

    @staticmethod
    def validate_request_data():
        """Validiert und bereinigt Request-Daten."""
        @wraps(f)
        def decorated(*args, **kwargs):
            if not request.is_json:
                abort(400, description="Content-Type muss application/json sein")

            data = request.get_json()
            if not data:
                abort(400, description="Keine Daten im Request-Body")

            # XSS-Prevention
            if isinstance(data, dict):
                for key, value in data.items():
                    if isinstance(value, str):
                        # Einfache HTML-Tag-Entfernung (in der Praxis würde man eine Library wie bleach verwenden)
                        data[key] = value.replace('<', '&lt;').replace('>', '&gt;')

            request.cleaned_data = data
            return f(*args, **kwargs)
        return decorated

    @staticmethod
    def setup_security_headers(response):
        """Fügt Sicherheits-Header zu Responses hinzu."""
        # Security Headers
        response.headers['Content-Security-Policy'] = "default-src 'self'"
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['X-Frame-Options'] = 'SAMEORIGIN'
        response.headers['X-XSS-Protection'] = '1; mode=block'
        response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
        return response

    @staticmethod
    def init_app(app):
        """Initialisiert Sicherheitskonfiguration für die Flask-App."""
        # CORS konfigurieren
        app.config['CORS_HEADERS'] = 'Content-Type'
        
        # Session-Konfiguration
        app.config['SESSION_COOKIE_SECURE'] = True
        app.config['SESSION_COOKIE_HTTPONLY'] = True
        app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
        
        # Response-Header hinzufügen
        @app.after_request
        def add_security_headers(response):
            return SecurityConfig.setup_security_headers(response)
        
        # Rate Limiting (einfaches Beispiel)
        @app.before_request
        def limit_remote_addr():
            if request.path.startswith('/api/'):
                # Implementieren Sie hier Rate Limiting-Logik
                pass