# src/server/main.py

from flask import Flask, request
from flask_restx import Api
from flask_cors import CORS
import os
from dotenv import load_dotenv

from config.security_config import SecurityConfig
from api.User import person_namespace
from api.Wardrobe import wardrobe_namespace
from api.Clothing import clothing_namespace
from api.Outfit import outfit_namespace
from api.Style import style_namespace

# Umgebungsvariablen laden
load_dotenv()

# Flask-App initialisieren
app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# API konfigurieren
api = Api(
    app,
    version='1.0',
    title='Digital Wardrobe API',
    description='API für digitale Kleiderschrankverwaltung',
    doc='/swagger'
)

# Namespaces registrieren
api.add_namespace(person_namespace, path='/api/persons')
api.add_namespace(wardrobe_namespace, path='/api/wardrobes')
api.add_namespace(clothing_namespace, path='/api/clothing')
api.add_namespace(outfit_namespace, path='/api/outfits')
api.add_namespace(style_namespace, path='/api/styles')

# Middleware für Token-Validierung
@app.before_request
def authenticate():
    if request.path.startswith('/api/'):
        if request.path == '/api/login' or request.path == '/api/register':
            return
        
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return {'message': 'No token provided'}, 401
        
        try:
            token = auth_header.split(' ')[1]
            SecurityConfig.check_auth(token)
        except Exception as e:
            return {'message': str(e)}, 401

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=int(os.getenv('PORT', 5000)),
        debug=os.getenv('FLASK_ENV') == 'development'
    )