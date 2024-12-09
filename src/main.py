from flask import Flask
from flask_cors import CORS
from flask_restx import Api, Resource, fields
from server.Administration import Administration
from server.bo.BinaryConstraint import BinaryConstraint
from server.bo.CardinalityConstraint import CardinalityConstraint
from server.bo.ClothingItems import ClothingItem
from server.bo.ConstraintRule import Constraint
from server.bo.ImplicationConstraint import ImplicationConstraint
from server.bo.MutexConstraint import MutexConstraint
from server.bo.Outfit import Outfit
from server.bo.Style import Style
from server.bo.UnaryConstraint import UnaryConstraint
from server.bo.User import User
from server.bo.Wardrobe import Wardrobe
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
    'id': fields.String(attribute='_id', description='Unique identifier'),
    'created_at': fields.DateTime(attribute='_created_at', description='Creation timestamp')
})


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
    'clothing_type_id': fields.String(attribute='_clothing_type_id', required=True),
    'product_name': fields.String(attribute='_product_name', required=True),
    'color': fields.String(attribute='_color'),
    'brand': fields.String(attribute='_brand'),
    'season': fields.String(attribute='_season')
})


outfit = api.inherit('Outfit', bo, {
    'name': fields.String(attribute='_name', required=True, description='Name of the outfit'),
    'style_id': fields.Integer(attribute='_style_id', required=True, description='Identifier of the associated style'),
    'wardrobe_id': fields.Integer(attribute='_wardrobe_id', required=True, description='Identifier of the wardrobe associated with the outfit'),
    'items': fields.List(fields.Integer, attribute='_items', description='List of clothing item IDs in the outfit'),
    'occasions': fields.List(fields.String, attribute='_occasions', description='Occasions for which the outfit is suitable'),
    'rating': fields.Integer(attribute='_rating', description='User rating for the outfit'),
    'times_worn': fields.Integer(attribute='_times_worn', description='Number of times the outfit has been worn')
})

style = api.inherit('Style', bo, {
    'name': fields.String(attribute='_name', required=True, description='Name of the style'),
    'description': fields.String(attribute='_description', description='Description of the style'),
    'creator_id': fields.Integer(attribute='_creator_id', required=True, description='ID of the user who created the style'),
    'is_public': fields.Boolean(attribute='_is_public', description='Whether the style is publicly available'),
    'seasons': fields.List(fields.String, attribute='_seasons', description='Seasons associated with the style'),
    'occasions': fields.List(fields.String, attribute='_occasions', description='Occasions suitable for the style'),
    'constraints': fields.List(fields.Nested(constraint), attribute='_constraints', description='List of constraints for the style'),
    'tags': fields.List(fields.String, attribute='_tags', description='Tags associated with the style')
})

constraint = api.inherit('Constraint', bo, {
    'style_id': fields.Integer(attribute='_style_id', required=True, description='Identifier of the associated style'),
    'type': fields.String(attribute='_type', required=True, description='Type of the constraint (e.g., binary, unary)'),
    'value': fields.String(attribute='_value', required=True, description='Constraint-specific rules in JSON format')
})
