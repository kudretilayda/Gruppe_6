import firebase_admin
from firebase_admin import credentials, auth
import os

class FirebaseConfig:
    """Basis Firebase-Konfiguration"""

    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(FirebaseConfig, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not FirebaseConfig._initialized:
            # Option 1: Umgebungsvariablen
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
                "client_x509_cert_url": f"https://www.googleapis.com/robot/v1/metadata/x509/{os.getenv('FIREBASE_CLIENT_EMAIL')}"
            })

            # Option 2: Direkt über JSON-Datei
            # cred = credentials.Certificate("path/to/serviceAccountKey.json")

            try:
                firebase_admin.initialize_app(cred)
                FirebaseConfig._initialized = True
            except ValueError:
                pass  # App ist bereits initialisiert

    @staticmethod
    def verify_token(id_token):
        try:
            return auth.verify_id_token(id_token)
        except Exception as e:
            raise ValueError(f"Ungültiges Token: {e}")

    @staticmethod
    def get_user_by_email(email):
        try:
            return auth.get_user_by_email(email)
        except auth.UserNotFoundError:
            return None
        except Exception as e:
            raise ValueError(f"Fehler beim Abrufen des Benutzers: {e}")

    @staticmethod
    def create_custom_token(uid):
        try:
            return auth.create_custom_token(uid)
        except Exception as e:
            raise ValueError(f"Fehler beim Erstellen des benutzerdefinierten Tokens: {e}")

