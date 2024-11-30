from functools import wraps
from flask import request, abort
import json
from typing import Callable, Any
import firebase_admin
from firebase_admin import credentials, auth
import os
from dotenv import load_dotenv

load_dotenv()

# Firebase initialisieren
try:
    cred = credentials.Certificate({
        "type": "service_account",
        "project_id": os.getenv('FIREBASE_PROJECT_ID'),
        "private_key_id": os.getenv('FIREBASE_PRIVATE_KEY_ID'),
        "private_key": os.getenv('FIREBASE_PRIVATE_KEY').replace('\\n', '\n'),
        "client_email": os.getenv('FIREBASE_CLIENT_EMAIL'),
        "client_id": os.getenv('FIREBASE_CLIENT_ID'),
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": os.getenv('FIREBASE_CLIENT_CERT_URL')
    })
    firebase_admin.initialize_app(cred)
except Exception as e:
    print(f"Fehler bei der Firebase-Initialisierung: {e}")

class SecurityError(Exception):
    """Basis-Exception für Security-Fehler"""
    pass

class AuthenticationError(SecurityError):
    """Exception für Authentifizierungsfehler"""
    pass

def secured(function: Callable) -> Callable:
    """
    Decorator für geschützte Endpunkte.
    Prüft Firebase-Token und fügt User-Info zum Request hinzu.
    """
    @wraps(function)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        token = None
        
        try:
            if 'Authorization' in request.headers:
                # Bearer Token Format: "Bearer <token>"
                auth_header = request.headers['Authorization']
                if ' ' in auth_header:
                    token = auth_header.split(' ')[1]
                else:
                    token = auth_header

            if not token:
                raise AuthenticationError('Kein Authorization Token gefunden')

            try:
                # Token verifizieren und decodieren
                decoded_token = auth.verify_id_token(token)
                request.user = decoded_token
                
                # Optional: Zusätzliche Token-Validierung
                if not _validate_token_claims(decoded_token):
                    raise AuthenticationError('Token-Claims ungültig')
                
                return function(*args, **kwargs)
                
            except auth.InvalidIdTokenError:
                raise AuthenticationError('Ungültiger Token')
            except auth.ExpiredIdTokenError:
                raise AuthenticationError('Token abgelaufen')
            except auth.RevokedIdTokenError:
                raise AuthenticationError('Token widerrufen')
            except auth.CertificateFetchError:
                raise AuthenticationError('Fehler beim Zertifikat-Abruf')
                
        except AuthenticationError as e:
            return {'error': 'Authentifizierungsfehler', 'message': str(e)}, 401
        except Exception as e:
            return {'error': 'Interner Server-Fehler', 'message': str(e)}, 500

    return wrapper

def _validate_token_claims(decoded_token: dict) -> bool:
    """
    Zusätzliche Validierung der Token-Claims.
    Kann nach Bedarf erweitert werden.
    """
    try:
        # Prüfe ob Token nicht zu alt ist (optional)
        auth_time = decoded_token.get('auth_time', 0)
        # Prüfe ob Email verifiziert ist (optional)
        email_verified = decoded_token.get('email_verified', False)
        
        required_claims = ['sub', 'aud', 'iat']
        return all(claim in decoded_token for claim in required_claims)
        
    except Exception as e:
        print(f"Fehler bei der Token-Validierung: {e}")
        return False

def get_current_user_id() -> str:
    """Hilfsfunktion zum Abrufen der aktuellen User-ID"""
    if hasattr(request, 'user') and request.user:
        return request.user.get('user_id')
    return None

def has_role(role: str) -> bool:
    """
    Prüft ob der aktuelle User eine bestimmte Rolle hat.
    Kann für feingranulare Berechtigungen verwendet werden.
    """
    if hasattr(request, 'user') and request.user:
        user_roles = request.user.get('roles', [])
        return role in user_roles
    return False

# Zusätzlicher Decorator für Rollenbasierte Zugriffskontrolle
def require_role(role: str) -> Callable:
    """Decorator für rollenbasierten Zugriff"""
    def decorator(function: Callable) -> Callable:
        @wraps(function)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if not has_role(role):
                return {'error': 'Nicht autorisiert', 
                        'message': f'Rolle {role} erforderlich'}, 403
            return function(*args, **kwargs)
        return wrapper
    return decorator