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
from server.bo.Constraints import Constraints, BinaryConstraint, UnaryConstraint, CardinalityConstraint, MutexConstraint, ImplicationConstraint
import traceback
from SecurityDecorator import secured

app = Flask(__name__)

# Enable CORS
CORS(app, supports_credentials=True, resources=r'/wardrobe/*')

# Create API object
api = Api(app, version='1.0', title='Digital Wardrobe API',
          description='An API for managing a digital wardrobe.')

# Namespace
wardrobe_ns = api.namespace('wardrobe', description='Digital Wardrobe functionalities')

# Models for Flask-RestX
bo = api.model('BusinessObject', {
    'id': fields.String(attribute='_id', description='Unique identifier'),
})

user = api.inherit('User', bo, {
    'user_id': fields.String(attribute='_user_id', description='User ID'),
    'google_id': fields.String(attribute='_google_id', description='Google user ID'),
    'first_name': fields.String(attribute='_first_name', description='First name'),
    'last_name': fields.String(attribute='_last_name', description='Last name'),
    'nick_name': fields.String(attribute='_nick_name', description='Nickname'),
    'email': fields.String(attribute='_email', description='Email address')
})

wardrobe = api.inherit('Wardrobe', bo, {
    'user_id': fields.Integer(attribute='_user_id', description='ID of the owner'),
})

clothing_type = api.inherit('ClothingType', bo, {
    'type_name': fields.String(attribute='_type_name', description='Type name'),
    'type_usage': fields.String(attribute='_type_usage', description='Type usage'),
})

clothing_item = api.inherit('ClothingItem', bo, {
    'wardrobe_id': fields.Integer(attribute='_wardrobe_id', description='ID of the associated wardrobe'),
    'clothing_type_id': fields.Integer(attribute='_clothing_type_id', description='ID of the clothing type'), 
    'clothing_item_name': fields.String(attribute='_clothing_item_name', description='Name of the clothing item'),
    'color': fields.String(attribute='_color', description='Color of the clothing item'),
    'brand': fields.String(attribute='_brand', description='Brand of the clothing item'),
    'season': fields.String(attribute='_season', description='Season for the clothing item'),
})

style = api.inherit('Style', bo, {
    'style_features': fields.String(attribute='_style_features', description='Style features'),
    'style_constraints': fields.String(attribute='_style_constraints', description='Style constraints'),
})

outfit = api.inherit('Outfit', bo, {
    'outfit_name': fields.String(attribute='_outfit_name', description='Name of the outfit'),
    'style_id': fields.Integer(attribute='_style_id', description='ID of the associated style'),
})

constraint = api.inherit('Constraint', bo, {
    'style_id': fields.Integer(attribute='_style_id', description='ID of the associated style'),
    'constraint_type': fields.String(attribute='_constraint_type', description='Type of the constraint'),
    'attribute': fields.String(attribute='_attribute', description='Affected attribute'),
    'constrain': fields.String(attribute='_constrain', description='Constraint condition'),
    'val': fields.String(attribute='_val', description='Value'),
})

unary_constraint = api.inherit('UnaryConstraint', constraint, {
    'reference_object_id': fields.Integer(attribute='_reference_object_id', description='ID of the reference object'),
})

binary_constraint = api.inherit('BinaryConstraint', constraint, {
    'reference_object1_id': fields.Integer(attribute='_reference_object1_id', description='ID of the first reference object'),
    'reference_object2_id': fields.Integer(attribute='_reference_object2_id', description='ID of the second reference object'),
})

mutex_constraint = api.inherit('MutexConstraint', constraint, {
    'item_type_1': fields.Integer(attribute='_item_type_1', description='ID of the first clothing type'),
    'item_type_2': fields.Integer(attribute='_item_type_2', description='ID of the second clothing type'),
})

implication_constraint = api.inherit('ImplicationConstraint', constraint, {
    'if_type': fields.Integer(attribute='_if_type', description='ID of the "if" clothing type'),
    'then_type': fields.Integer(attribute='_then_type', description='ID of the "then" clothing type'),
})

cardinality_constraint = api.inherit('CardinalityConstraint', constraint, {
    'item_type': fields.Integer(attribute='_item_type', description='ID of the affected clothing type'),
    'min_count': fields.Integer(attribute='_min_count', description='Minimum count'),
    'max_count': fields.Integer(attribute='_max_count', description='Maximum count'),
})

