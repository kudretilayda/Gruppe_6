from flask import Flask
from flask_cors import CORS
from flask_restx import Api, Resource, fields

from server.Admin import WardrobeAdministration
from server.bo.User import Person
from server.bo.Wardrobe import Wardrobe
from server.bo.Style import Style
from server.bo.Outfit import Outfit
from server.bo.ClothingItem import ClothingItem
from server.bo.ClothingType import ClothingType
from server.constraints.Constraint import Constraint
from server.constraints.BinaryConstraint import BinaryConstraint
from server.constraints.UnaryConstraint import UnaryConstraint
from server.constraints.CardinalityConstraint import CardinalityConstraint
from server.constraints.ImplicationConstraint import ImplicationConstraint
from server.constraints.MutexConstraint import MutexConstraint
import traceback
from SecurityDecorator import secured

app=Flask(__name__)

# CORS aktivieren
CORS(app, supports_credentials=True, resources=r'/wardrobe/*')

# API-Objekt erstellen
api = Api(app, version='1.0', title='Digital Wardrobe API',
          description='An API for managing a digital wardrobe.')

# Namespace
wardrobe_ns = api.namespace('wardrobe', description='Digital Wardrobe functionalities')

# Modelle für Flask-RestX
bo = api.model('BusinessObject', {
    'id': fields.String(attribute='_id', description='Unique identifier'),
})

user = api.inherit('Person', bo, {
    'user_id': fields.String(attribute='_user_id', description='User ID'),
    'google_id': fields.String(attribute='_google_id', description='Google user ID'),
    'first_name': fields.String(attribute='_first_name', description='First name'),
    'last_name': fields.String(attribute='_last_name', description='Last name'),
    'nick_name': fields.String(attribute='_nick_name', description='Nickname'),
    'email': fields.String(attribute='_email', description='Email address')
})
