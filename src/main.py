from flask import Flask
from flask_cors import CORS
from flask_restx import Api, Resource, fields

from server.Admin import Admin
from server.bo.User import User
from server.bo.Wardrobe import Wardrobe
from server.bo.Style import Style
from server.bo.Outfit import Outfit
from server.bo.ClothingItem import ClothingItem
from server.bo.ClothingType import ClothingType

# from src.server.bo.Constraints.Constraint import Constraint
# from src.server.bo.Constraints.Unary import UnaryConstraint
# from src.server.bo.Constraints.Binary import BinaryConstraint
# from src.server.bo.Constraints.Implication import ImplicationConstraint
# from src.server.bo.Constraints.Cardinality import CardinalityConstraint
# from src.server.bo.Constraints.Mutex import MutexConstraint

from SecurityDecorator import secured

# Flask instanziieren
app = Flask(__name__)

# Cors instanziieren
CORS(app, resources={r"/*": {"origins": ["http://localhost:3000"]
        #"methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        #"allow_headers": ["Content-Type", "Authorization"],
        #"supports_credentials": True
    }
})

# Sicherheitsheader zum Vermeiden von Cors Problemen
@app.after_request
def add_security_headers(response):
    response.headers.pop("Cross-Origin-Opener-Policy", None)
    response.headers["Cross-Origin-Opener-Policy"] = "unsafe-none"  # CORS Fehlermeldung vermeiden
    return response


if __name__ == '__main__':
    app.run(debug=True)

'''
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3306, debug=True)
'''