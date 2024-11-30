from flask import Flask
from flask_cors import CORS
from flask_restx import Api, Resource, fields
from server.Admin import KleiderschrankAdministration
from server.bo.Style import Style
from server.bo.Outfit import Outfit
from server.bo.User import Person
from server.bo.Wardrobe import Wardrobe
from server.bo.ClothingItems import ClothingItem
from server.bo.ClothingType import ClothingType
from server.bo.Constraint import Constraint
import traceback

app = Flask(__name__)

# CORS aktivieren
CORS(app, supports_credentials=True, resources=r'/wardrobe/*')

# API-Objekt erstellen
api = Api(app, version='1.0', title='DigitalWardrobe API',
          description='Eine API zur Verwaltung eines digitalen Kleiderschranks.')

# Namespace
wardrobe_ns = api.namespace('wardrobe', description='Kleiderschrank-bezogene Funktionalitäten')

# Basis Business Object Model
bo = api.model('BusinessObject', {
    'id': fields.Integer(attribute='_id', description='Eindeutige ID eines Business Objects')
})

# Model Definitionen
person = api.inherit('Person', bo, {
    'google_id': fields.String(attribute='_google_id', description='Google ID der Person'),
    'first_name': fields.String(attribute='_first_name', description='Vorname'),
    'last_name': fields.String(attribute='_last_name', description='Nachname'),
    'nickname': fields.String(attribute='_nickname', description='Nickname')
})

wardrobe = api.inherit('Wardrobe', bo, {
    'owner_id': fields.Integer(attribute='_owner_id', description='Besitzer ID'),
})

clothing_item = api.inherit('ClothingItem', bo, {
    'wardrobe_id': fields.Integer(attribute='_wardrobe_id', required=True),
    'type_id': fields.Integer(attribute='_type_id', required=True),
    'name': fields.String(attribute='_name', required=True),
    'description': fields.String(attribute='_description')
})

clothing_type = api.inherit('ClothingType', bo, {
    'name': fields.String(attribute='_name', required=True),
    'description': fields.String(attribute='_description')
})

style = api.inherit('Style', bo, {
    'name': fields.String(attribute='_name', required=True),
    'description': fields.String(attribute='_description'),
    'features': fields.String(attribute='_features')
})

outfit = api.inherit('Outfit', bo, {
    'style_id': fields.Integer(attribute='_style_id', required=True),
    'name': fields.String(attribute='_name', required=True)
})

constraint = api.inherit('Constraint', bo, {
    'style_id': fields.Integer(attribute='_style_id', required=True),
    'type': fields.String(attribute='_type', required=True),
    'value': fields.String(attribute='_value', required=True)
})

# Person Endpoints
@wardrobe_ns.route('/persons')
@wardrobe_ns.response(500, 'Server Error')
class PersonListOperations(Resource):
    
    @secured
    @wardrobe_ns.marshal_list_with(UserWarning)
    def get(self):
        """Alle Personen auslesen"""
        adm = KleiderschrankAdministration()
        persons = adm.get_all_persons()
        return persons

    @secured
    @wardrobe_ns.marshal_with(person, code=200)
    @wardrobe_ns.expect(person)
    def post(self):
        """Neue Person anlegen"""
        adm = Admin()
        proposal = Person.from_dict(api.payload)

        if proposal is not None:
            p = adm.create_person(
                proposal.get_google_id(),
                proposal.get_first_name(),
                proposal.get_last_name(),
                proposal.get_nickname()
            )
            return p, 200
        else:
            return '', 500

# Weitere Endpoints folgen ähnlichem Muster für:
# - Wardrobe
# - ClothingItem
# - ClothingType
# - Style
# - Outfit
# - Constraint

if __name__ == '__main__':
    app.run(debug=True)