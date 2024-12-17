from flask import Flask, request, g
from flask_cors import CORS
from flask_restx import Api, Resource, fields

from functools import wraps
import time
import os
import traceback

from src.server.Admin import Administration
from src.server.bo.User import User
from src.server.bo.Wardrobe import Wardrobe
from src.server.bo.Style import Style
from src.server.bo.Outfit import Outfit
from src.server.bo.ClothingItem import ClothingItem
from src.server.bo.ClothingType import ClothingType
from src.server.bo.Constraints import ConstraintRule, BinaryConstraint, UnaryConstraint,CardinalityConstraint, MutexConstraint, ImplicationConstraint
from src.SecurityDecorator import secured


app = Flask(__name__)
api = Api(app, version='1.0', title='Digital Wardrobe API',
          description='An API for managing a digital wardrobe')

wardrobe_ns = api.namespace('wardrobe', description='Digital Wardrobe functionalities')

# Base Model
bo = api.model('BusinessObject', {
    'id': fields.String(attribute='_id', description='Unique identifier')
})

# User Model
user = api.inherit('User', bo, {
    'google_id': fields.String(attribute='_google_id', description='Google Authentication ID'),
    'firstname': fields.String(attribute='_firstname', description='First name'),
    'lastname': fields.String(attribute='_lastname', description='Last name'),
    'nickname': fields.String(attribute='_nickname', description='Nickname'),
    'email': fields.String(attribute='_email', description='Email address')
})

# Wardrobe Model
wardrobe = api.inherit('Wardrobe', bo, {
    'owner_id': fields.Integer(attribute='_owner_id', description='Owner ID reference'),
    'name': fields.String(attribute='_wardrobe_name', description='Wardrobe name')
})

# ClothingType Model
clothing_type = api.inherit('ClothingType', bo, {
    'name': fields.String(attribute='_type_name', description='Type name'),
    'usage': fields.String(attribute='_type_usage', description='Type usage')
})

# ClothingItem Model
clothing_item = api.inherit('ClothingItem', bo, {
    'wardrobe_id': fields.Integer(attribute='_wardrobe_id', description='Wardrobe reference'),
    'type_id': fields.Integer(attribute='_clothing_type_id', description='Clothing type reference'),
    'name': fields.String(attribute='_clothing_item_name', description='Item name'),
    'color': fields.String(attribute='_color', description='Color'),
    'brand': fields.String(attribute='_brand', description='Brand'),
    'season': fields.String(attribute='_season', description='Season')
})

# Style Model
style = api.inherit('Style', bo, {
    'name': fields.String(attribute='_style_name', description='Style name'),
    'features': fields.String(attribute='_style_features', description='Style features'),
    'constraints': fields.String(attribute='_style_constraints', description='Style constraints')
})

# Outfit Model
outfit = api.inherit('Outfit', bo, {
    'name': fields.String(attribute='_outfit_name', description='Outfit name'),
    'style_id': fields.Integer(attribute='_style_id', description='Style reference'),
    'items': fields.List(fields.Integer, description='List of clothing item IDs')
})

# Constraint Models
constraint = api.inherit('Constraint', bo, {
    'style_id': fields.Integer(attribute='_style_id', description='Style reference'),
    'type': fields.String(attribute='_constraint_type', description='Constraint type'),
    'parameters': fields.Raw(attribute='_parameters', description='Constraint parameters')
})

# Additional Constraint Types
binary_constraint = api.inherit('BinaryConstraint', constraint, {
    'object1_id': fields.Integer(attribute='_object1_id', description='First object reference'),
    'object2_id': fields.Integer(attribute='_object2_id', description='Second object reference')
})

unary_constraint = api.inherit('UnaryConstraint', constraint, {
    'object_id': fields.Integer(attribute='_object_id', description='Object reference'),
    'condition': fields.String(attribute='_condition', description='Condition'),
    'value': fields.String(attribute='_value', description='Condition value')
})

cardinality_constraint = api.inherit('CardinalityConstraint', constraint, {
    'type_id': fields.Integer(attribute='_type_id', description='Clothing type reference'),
    'min_count': fields.Integer(attribute='_min_count', description='Minimum count'),
    'max_count': fields.Integer(attribute='_max_count', description='Maximum count')
})



# API Endpoints
@wardrobe_ns.route('/user')
@wardrobe_ns.response(500, 'Server-Error')
class UserListOperations(Resource):
    @wardrobe_ns.marshal_list_with(user)
    @secured
    def get(self):
        """Alle User abrufen"""
        try:
            adm = Administration()
            users = adm.get_all_users()
            return users
        except Exception as e:
            return {'error': 'Internal server error'}, 500

    @wardrobe_ns.marshal_with(user)
    @wardrobe_ns.expect(user)
    @secured
    def post(self):
        """Neuen User erstellen"""
        try:
            adm = Administration()
            user = User.from_dict(api.payload)
            result = adm.create_user(user)
            return result, 201
        except Exception as e:

            return {'error': 'Internal server error'}, 500

@wardrobe_ns.route('/user/<int:id>')
class UserOperations(Resource):
    @wardrobe_ns.marshal_with(user)
    @secured
    def get(self, id):
        """Spezifischen User abrufen"""
        try:
            adm = Administration()
            user = adm.get_user_by_id(id)
            if user:
                return user
            return {'message': 'User not found'}, 404
        except Exception as e:

            return {'error': 'Internal server error'}, 500

    @wardrobe_ns.marshal_with(user)
    @wardrobe_ns.expect(user)
    @secured
    def put(self, id):
        """User aktualisieren"""
        try:
            adm = Administration()
            updated_user = User.from_dict(api.payload)
            updated_user.set_id(id)
            result = adm.save_user(updated_user)
            return result
        except Exception as e:

            return {'error': 'Internal server error'}, 500

    @secured
    def delete(self, id):
        """User löschen"""
        try:
            adm = Administration()
            user = adm.get_user_by_id(id)
            if user:
                adm.delete_user(user)
                return '', 204
            return {'message': 'User not found'}, 404
        except Exception as e:

            return {'error': 'Internal server error'}, 500

# 2. Wardrobe Endpoints
@wardrobe_ns.route('/wardrobe')
class WardrobeListOperations(Resource):
    @wardrobe_ns.marshal_list_with(wardrobe)
    @secured
    def get(self):
        """Alle Kleiderschränke abrufen"""
        try:
            adm = Administration()
            wardrobes = adm.get_all_wardrobes()
            return wardrobes
        except Exception as e:

            return {'error': 'Internal server error'}, 500

    @wardrobe_ns.marshal_with(wardrobe)
    @wardrobe_ns.expect(wardrobe)
    @secured
    def post(self):
        """Neuen Kleiderschrank erstellen"""
        try:
            adm = Administration()
            wardrobe = Wardrobe.from_dict(api.payload)
            result = adm.create_wardrobe(wardrobe)
            return result, 201
        except Exception as e:

            return {'error': 'Internal server error'}, 500

@wardrobe_ns.route('/wardrobe/<int:id>')
class WardrobeOperations(Resource):
    @wardrobe_ns.marshal_with(wardrobe)
    @secured
    def get(self, id):
        """Spezifischen Kleiderschrank abrufen"""
        try:
            adm = Administration()
            wardrobe = adm.get_wardrobe_by_id(id)
            if wardrobe:
                return wardrobe
            return {'message': 'Wardrobe not found'}, 404
        except Exception as e:

            return {'error': 'Internal server error'}, 500

    @wardrobe_ns.marshal_with(wardrobe)
    @wardrobe_ns.expect(wardrobe)
    @secured
    def put(self, id):
        """Kleiderschrank aktualisieren"""
        try:
            adm = Administration()
            updated_wardrobe = Wardrobe.from_dict(api.payload)
            updated_wardrobe.set_id(id)
            result = adm.save_wardrobe(updated_wardrobe)
            return result
        except Exception as e:

            return {'error': 'Internal server error'}, 500

    @secured
    def delete(self, id):
        """Kleiderschrank löschen"""
        try:
            adm = Administration()
            wardrobe = adm.get_wardrobe_by_id(id)
            if wardrobe:
                adm.delete_wardrobe(wardrobe)
                return '', 204
            return {'message': 'Wardrobe not found'}, 404
        except Exception as e:

            return {'error': 'Internal server error'}, 500

# 3. ClothingItem Endpoints
@wardrobe_ns.route('/clothing-item')
class ClothingItemListOperations(Resource):
    @wardrobe_ns.marshal_list_with(clothing_item)
    @secured
    def get(self):
        """Alle Kleidungsstücke abrufen"""
        try:
            adm = Administration()
            items = adm.get_all_clothing_items()
            return items
        except Exception as e:

            return {'error': 'Internal server error'}, 500

    @wardrobe_ns.marshal_with(clothing_item)
    @wardrobe_ns.expect(clothing_item)
    @secured
    def post(self):
        """Neues Kleidungsstück erstellen"""
        try:
            adm = Administration()
            item = ClothingItem.from_dict(api.payload)
            result = adm.create_clothing_item(
                wardrobe_id=item.get_wardrobe_id(),
                clothing_type_id=item.get_clothing_type(),
                clothing_item_name=item.get_item_name()
            )
            return result, 201
        except Exception as e:

            return {'error': 'Internal server error'}, 500

@wardrobe_ns.route('/clothing-item/<int:id>')
class ClothingItemOperations(Resource):
    @wardrobe_ns.marshal_with(clothing_item)
    @secured
    def get(self, id):
        """Spezifisches Kleidungsstück abrufen"""
        try:
            adm = Administration()
            item = adm.get_clothing_item_by_id(id)
            if item:
                return item
            return {'message': 'Clothing item not found'}, 404
        except Exception as e:

            return {'error': 'Internal server error'}, 500

    @wardrobe_ns.marshal_with(clothing_item)
    @wardrobe_ns.expect(clothing_item)
    @secured
    def put(self, id):
        """Kleidungsstück aktualisieren"""
        try:
            adm = Administration()
            updated_item = ClothingItem.from_dict(api.payload)
            updated_item.set_id(id)
            result = adm.save_clothing_item(updated_item)
            return result
        except Exception as e:

            return {'error': 'Internal server error'}, 500

    @secured
    def delete(self, id):
        """Kleidungsstück löschen"""
        try:
            adm = Administration()
            item = adm.get_clothing_item_by_id(id)
            if item:
                adm.delete_clothing_item(item)
                return '', 204
            return {'message': 'Clothing item not found'}, 404
        except Exception as e:

            return {'error': 'Internal server error'}, 500

# 4. Style Endpoints
@wardrobe_ns.route('/style')
class StyleListOperations(Resource):
    @wardrobe_ns.marshal_list_with(style)
    @secured
    def get(self):
        """Alle Styles abrufen"""
        try:
            adm = Administration()
            styles = adm.get_all_styles()
            return styles
        except Exception as e:

            return {'error': 'Internal server error'}, 500

    @wardrobe_ns.marshal_with(style)
    @wardrobe_ns.expect(style)
    @secured
    def post(self):
        """Neuen Style erstellen"""
        try:
            adm = Administration()
            style_obj = Style.from_dict(api.payload)
            result = adm.create_style(
                style_features=style_obj.get_style_features(),
                style_constraints=style_obj.get_style_constraints()
            )
            return result, 201
        except Exception as e:

            return {'error': 'Internal server error'}, 500

@wardrobe_ns.route('/style/<int:id>')
class StyleOperations(Resource):
    @wardrobe_ns.marshal_with(style)
    @secured
    def get(self, id):
        """Spezifischen Style abrufen"""
        try:
            adm = Administration()
            style = adm.get_style_by_id(id)
            if style:
                return style
            return {'message': 'Style not found'}, 404
        except Exception as e:

            return {'error': 'Internal server error'}, 500

    @wardrobe_ns.marshal_with(style)
    @wardrobe_ns.expect(style)
    @secured
    def put(self, id):
        """Style aktualisieren"""
        try:
            adm = Administration()
            updated_style = Style.from_dict(api.payload)
            updated_style.set_id(id)
            result = adm.save_style(updated_style)
            return result
        except Exception as e:

            return {'error': 'Internal server error'}, 500

    @secured
    def delete(self, id):
        """Style löschen"""
        try:
            adm = Administration()
            style = adm.get_style_by_id(id)
            if style:
                adm.delete_style(style)
                return '', 204
            return {'message': 'Style not found'}, 404
        except Exception as e:

            return {'error': 'Internal server error'}, 500

# 5. Outfit Endpoints
@wardrobe_ns.route('/outfit')
class OutfitListOperations(Resource):
    @wardrobe_ns.marshal_list_with(outfit)
    @secured
    def get(self):
        """Alle Outfits abrufen"""
        try:
            adm = Administration()
            outfits = adm.get_all_outfits()
            return outfits
        except Exception as e:

            return {'error': 'Internal server error'}, 500

    @wardrobe_ns.marshal_with(outfit)
    @wardrobe_ns.expect(outfit)
    @secured
    def post(self):
        """Neues Outfit erstellen"""
        try:
            adm = Administration()
            outfit_obj = Outfit.from_dict(api.payload)
            result = adm.create_outfit(
                outfit_name=outfit_obj.get_outfit_name(),
                style_id=outfit_obj.get_style()
            )
            return result, 201
        except Exception as e:

            return {'error': 'Internal server error'}, 500

@wardrobe_ns.route('/outfit/<int:id>')
class OutfitOperations(Resource):
    @wardrobe_ns.marshal_with(outfit)
    @secured
    def get(self, id):
        """Spezifisches Outfit abrufen"""
        try:
            adm = Administration()
            outfit = adm.get_outfit_by_id(id)
            if outfit:
                return outfit
            return {'message': 'Outfit not found'}, 404
        except Exception as e:

            return {'error': 'Internal server error'}, 500

    @wardrobe_ns.marshal_with(outfit)
    @wardrobe_ns.expect(outfit)
    @secured
    def put(self, id):
        """Outfit aktualisieren"""
        try:
            adm = Administration()
            updated_outfit = Outfit.from_dict(api.payload)
            updated_outfit.set_id(id)
            result = adm.save_outfit(updated_outfit)
            return result
        except Exception as e:

            return {'error': 'Internal server error'}, 500

    @secured
    def delete(self, id):
        """Outfit löschen"""
        try:
            adm = Administration()
            outfit = adm.get_outfit_by_id(id)
            if outfit:
                adm.delete_outfit(outfit)
                return '', 204
            return {'message': 'Outfit not found'}, 404
        except Exception as e:

            return {'error': 'Internal server error'}, 500

if __name__ == '__main__':
    app.run(debug=True)