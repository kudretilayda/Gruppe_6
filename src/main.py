#from SecurityDecorator import secured

from flask import Flask
from flask_restx import Api, Resource, fields
from flask_cors import CORS
from src.server.Admin import Administration

from src.server.bo.Outfit import Outfit
from src.server.bo.Style import Style
from src.server.bo.User import User
from src.server.bo.Wardrobe import Wardrobe
from src.server.bo.Constraints import (
    UnaryConstraint,
    BinaryConstraint,
    ImplicationConstraint,
    MutexConstraint,
    CardinalityConstraint, ConstraintRule)

import traceback
from SecurityDecorator import secured

app = Flask(__name__)

#CORS aktivieren
#CORS steht für Cross-Origin Resource Sharing und ist ein Mechanismus, der es Webseiten ermöglicht, Ressourcen von anderen Domains zu laden.
"""CORS(app, resources={r"/api/":{"origins":"*"}})"""
CORS(app, supports_credentials=True, resources=r'/wardrobe/*')

#API-Objekt erstellen
api = Api(app, version='1.0', title='DigitalWardrobe API',
          description='An API for managing a digital wardrobe.')

# Namespace
#Der Namespace ist Container für die API-Endpunkte, die zu einem bestimmten Thema gehören.
Wardrobe_ns = api.namespace('wardrobe', description='Wardrobe-related functionalities')

# Modelle für Flask-Restx: Flast-Restx verwendet die Modelle, um die JSON-Objekte zu serialisieren und zu deserialisieren,
#Restx ist eine Erweiterung von Flask, die es ermöglicht, RESTful APIs zu erstellen.
#RESTful APIs sind APIs, die auf dem REST-Prinzip basieren, das besagt, dass jede Ressource über eine eindeutige URL angesprochen wird.


# Modelle für Flask-RestX
bo = api.model('BusinessObject', {
    'id': fields.Integer(attribute='_id', description='Der Unique Identifier eines BusinessObject')
})

# User Modell
user = api.inherit('User', bo, {
    'google_id': fields.String(attribute='_google_id', required=True, description='Google ID of the user'),
    'firstname': fields.String(attribute='_firstname', required=True, description='First name of the user'),
    'lastname': fields.String(attribute='_lastname', required=True, description='Last name of the user'),
    'nickname': fields.String(attribute='_nickname', description='Nickname of the user'),
    'email': fields.String(attribute='_email', required=True, description='Email address of the user')
})

wardrobe = api.inherit('Wardrobe', bo, {
    'person_id': fields.String(attribute='_person_id', description='Owner ID'),
    'owner_name': fields.String(attribute='_owner_name', description='Owner name')
})


clothing_type = api.inherit('ClothingType', bo, {
    'type_name': fields.String(attribute='_type_name', required=True, description='Type name'),
    'category': fields.String(attribute='_category', required=True, description='Category'),
    'type_description': fields.String(attribute='_type_description', description='Type description')
})

clothing_item = api.inherit('ClothingItem', bo, {
    'wardrobe_id': fields.String(attribute='_wardrobe_id', required=True),
    'clothing_type': fields.String(attribute='_clothing_type', required=True),
    'item_name': fields.String(attribute='_item_name', required=True),
})


outfit = api.inherit('Outfit', bo, {
    'name': fields.String(attribute='_name', required=True, description='Name of the outfit'),
    'style_id': fields.Integer(attribute='_style_id', required=True, description='Identifier of the associated style'),
    'wardrobe_id': fields.Integer(attribute='_wardrobe_id', required=True, description='Identifier of the wardrobe associated with the outfit'),
    'items': fields.List(fields.Integer, attribute='_items', description='List of clothing item IDs in the outfit')
})

# Constraint Modell
constraint = api.inherit('Constraint', bo, {
    'style_id': fields.Integer(attribute='_style_id', required=True, description='Identifier of the associated style'),
    'type': fields.String(attribute='_type', required=True, description='Type of the constraint (e.g., binary, unary)'),
    'value': fields.String(attribute='_value', required=True, description='Constraint-specific rules in JSON format')
})

''' 
# BinaryConstraint Modell
binary_constraint = api.inherit('BinaryConstraint', constraint, {
    'object1': fields.String(attribute='_object1', description='Bezugsobjekt 1'),
    'object2': fields.String(attribute='_object2', description='Bezugsobjekt 2'),
    'bedingung': fields.String(attribute='_bedingung', description='Bedingung des BinaryConstraints')
})

# CardinalityConstraint Modell
cardinality_constraint = api.inherit('CardinalityConstraint', constraint, {
    'min_count': fields.Integer(attribute='_min_count', description='Minimale Kardinalität'),
    'max_count': fields.Integer(attribute='_max_count', description='Maximale Kardinalität'),
    'object1': fields.String(attribute='_object1', description='Erstes Objekt'),
    'object2': fields.String(attribute='_object2', description='Zweites Objekt')
})

# ImplicationConstraint Modell
implication_constraint = api.inherit('ImplicationConstraint', constraint, {
    'condition': fields.String(attribute='_condition', description='Bedingung'),
    'implication': fields.String(attribute='_implication', description='Implikation')
})

# MutexConstraint Modell
mutex_constraint = api.inherit('MutexConstraint', constraint, {
    'object1': fields.String(attribute='_object1', description='Erstes Objekt'),
    'object2': fields.String(attribute='_object2', description='Zweites Objekt')
})

@kleiderschrank.route('/user')
class UserListOperations(Resource):
    @kleiderschrank.marshal_list_with(user)
    def get(self):
        """Alle User auslesen"""
        return []  # Zunächst leere Liste zurückgeben
    
@kleiderschrank.route('/constraint')
class ConstraintListOperations(Resource):
    @kleiderschrank.marshal_list_with(constraint)
    def get(self):
        """Alle Constraints auslesen"""
        return []  # Zunächst leere Liste zurückgeben
    
@kleiderschrank.route('/unary-constraint')
class UnaryConstraintListOperations(Resource):
    @kleiderschrank.marshal_list_with(unary_constraint)
    def get(self):
        """Alle UnaryConstraints auslesen"""
        return []

@kleiderschrank.route('/binary-constraint')
class BinaryConstraintListOperations(Resource):
    @kleiderschrank.marshal_list_with(binary_constraint)
    def get(self):
        """Alle BinaryConstraints auslesen"""
        return []

@kleiderschrank.route('/cardinality-constraint')
class CardinalityConstraintListOperations(Resource):
    @kleiderschrank.marshal_list_with(cardinality_constraint)
    def get(self):
        """Alle CardinalityConstraints auslesen"""
        return []

@kleiderschrank.route('/implication-constraint')
class ImplicationConstraintListOperations(Resource):
    @kleiderschrank.marshal_list_with(implication_constraint)
    def get(self):
        """Alle ImplicationConstraints auslesen"""
        return []

@kleiderschrank.route('/mutex-constraint')
class MutexConstraintListOperations(Resource):
    @kleiderschrank.marshal_list_with(mutex_constraint)
    def get(self):
        """Alle MutexConstraints auslesen"""
        return []

if __name__ == '__main__':
    app.run(debug=True)
'''