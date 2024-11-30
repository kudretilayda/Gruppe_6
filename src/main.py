from flask import Flask
from flask_restx import Api
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)
api = Api(app, version='1.0', title='Digital Wardrobe API',
          description='API for managing digital wardrobe items and styles')


from routes.person_routes import *
from routes.wardrobe_routes import *
from routes.style_routes import *
from routes.outfit_routes import *
from routes.clothing_type_routes import *
from routes.clothing_item_routes import *

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)