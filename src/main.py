import os
import sys

# src module not found workaround (failed)
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)



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

# from src.server.bo.Constraints.Unary import UnaryConstraint
# from src.server.bo.Constraints.Binary import BinaryConstraint
# from src.server.bo.Constraints.Implication import ImplicationConstraint
# from src.server.bo.Constraints.Cardinality import CardinalityConstraint
# from src.server.bo.Constraints.Mutex import MutexConstraint

from SecurityDecorator import secured

# Flask instanziieren
app = Flask(__name__)



# Cors insanziieren
CORS(app, resources={
    r"/*": {
        "origins": ["http://localhost:3000"],
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization", "Access-Control-Allow-Credentials"],
        "supports_credentials": True
    }
})

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    response.headers.add('Cross-Origin-Opener-Policy', 'same-origin')
    response.headers.add('Cross-Origin-Embedder-Policy', 'require-corp')
    return response

#CORS(app, resources=r'/wardrobe/*')

# API für Datenstruktur
api = Api(app, version='1.0', title='Digital Wardrobe',
          description='API für den digitalen Kleiderschrank')

# Namespace
wardrobe_ns = api.namespace('wardrobe', description='Funktionen des digitalen Kleiderschranks')

# Models for Flask-RestX
bo = api.model('BusinessObject', {
    'id': fields.Integer(attribute='_id', description='Unique identifier'),
})

user = api.inherit('User', bo, {
    # 'user_id': fields.String(attribute='_user_id', description='User ID'),
    'google_id': fields.String(attribute='_google_id', description='Google user ID'),
    'first_name': fields.String(attribute='_firstname', description='First name'),
    'last_name': fields.String(attribute='_lastname', description='Last name'),
    'nickname': fields.String(attribute='_nickname', description='Nickname'),
    'email': fields.String(attribute='_email', description='Email address')
})

wardrobe = api.inherit('Wardrobe', bo, {
    'wardrobe_owner': fields.Integer(attribute='_wardrobe_owner', description='ID of the owner'),
})

clothing_type = api.inherit('ClothingType', bo, {
    'name': fields.String(attribute='_name', description='Type name'),
    'usage': fields.String(attribute='_usage', description='Type usage'),
})

clothing_item = api.inherit('ClothingItem', bo, {
    'wardrobe_id': fields.Integer(attribute='_wardrobe_id', description='ID of the associated wardrobe'),
    'clothing_type': fields.Integer(attribute='_clothing_type', description='ID of the clothing type'),
    'item_name': fields.String(attribute='item_name', description='Name of the clothing item')
})

style = api.inherit('Style', bo, {
    'style_features': fields.String(attribute='_style_features', description='Style features'),
    'style_constraints': fields.List(fields.Raw, attribute='style_constraints', description='Style constraints'),
})

outfit = api.inherit('Outfit', bo, {
    'outfit_name': fields.String(attribute='_outfit_name', description='Name of the outfit'),
    'style': fields.Integer(attribute='style', description='ID of the associated style'),
})

constraint = api.model('Constraint', {
    'type': fields.String(description='Type of the constraint'),
    'details': fields.Raw(description='Details of the constraint')
})

'''
Nun ist die Frage, ob wir die einzelnen Constraints brauchen
'''

unary_constraint = api.inherit('UnaryConstraint', constraint, {
    'style': fields.Integer(attribute='style', description='ID of the reference style'),
})

binary_constraint = api.inherit('BinaryConstraint', constraint, {
    'item_1': fields.Integer(attribute='item_1', description='ID of the first reference object'),
    'item_2': fields.Integer(attribute='item_2', description='ID of the second reference object'),
})

implication_constraint = api.inherit('ImplicationConstraint', constraint, {
    'if_type': fields.Integer(attribute='if_type', description='ID of the "if" clothing type'),
    'then_type': fields.Integer(attribute='then_type', description='ID of the "then" clothing type'),
})

cardinality_constraint = api.inherit('CardinalityConstraint', constraint, {
    'objects': fields.Boolean(attribute='objects', description='ID of the affected clothing type'),
    'min_count': fields.Integer(attribute='min_count', description='Minimum count'),
    'max_count': fields.Integer(attribute='max_count', description='Maximum count'),
})

mutex_constraint = api.inherit('MutexConstraint', constraint, {
    'mutex': fields.Raw(attribute='mutex', description='ID of the first clothing type'),
})

# API Endpoints for Users
@wardrobe_ns.route('/user')
@wardrobe_ns.response(500, 'Server-Error')
class UserListOperations(Resource):
    @wardrobe_ns.marshal_list_with(user)
    @secured
    def get(self):
        """Get all users"""
        adm = Admin()
        users = adm.get_all_users()
        return users

    @wardrobe_ns.marshal_with(user, code=200)
    @wardrobe_ns.expect(user)
    @secured
    def post(self):
        """Create a new user"""
        adm = Admin()
        proposal = User.from_dict(api.payload)
        if proposal is not None:
            c = adm.create_user(
                proposal.get_google_id(),
                proposal.get_first_name(),
                proposal.get_last_name(),
                proposal.get_nickname(),
                proposal.get_email()
            )
            return c, 200
        else:
            return '', 500

@wardrobe_ns.route('/user/<int:user_id>')
@wardrobe_ns.response(500, 'Server-Error')
@wardrobe_ns.param('user_id', 'ID of the user')
class UserOperations(Resource):
    @wardrobe_ns.marshal_with(user)
    @secured
    def get(self, user_id):
        """Get a user by ID"""
        adm = Admin()
        user = adm.get_user_by_id(user_id)
        return user

    @wardrobe_ns.marshal_with(user)
    @wardrobe_ns.expect(user, validate=True)
    @secured
    def put(self, user_id):
        """Update a user"""
        adm = Admin()
        user = User.from_dict(api.payload)
        if user is not None:
            user.set_id(user_id)
            adm.save_user(user)
            return user, 200
        else:
            return '', 500

    @secured
    def delete(self, user_id):
        """Delete a user"""
        adm = Admin()
        user = adm.get_user_by_id(user_id)
        adm.delete_user(user)
        return '', 200

@wardrobe_ns.route('/user/<int:user_id>/wardrobe')
@wardrobe_ns.response(500, 'Server-Error')
@wardrobe_ns.param('user_id', 'ID of the user')
class UserWardrobeOperations(Resource):
    @wardrobe_ns.marshal_with(wardrobe)
    @secured
    def get(self, user_id):
        """Get the wardrobe of a user"""
        adm = Admin()
        wardrobe = adm.get_wardrobe_by_user_id(user_id)
        return wardrobe

    @wardrobe_ns.marshal_with(wardrobe, code=200)
    @wardrobe_ns.expect(wardrobe)
    @secured
    def post(self, user_id):
        """Create a new wardrobe for a user"""
        adm = Admin()
        proposal = Wardrobe.from_dict()
#        proposal = Wardrobe.from_dict(api.payload) Dasselbe für Zeile 218
        if proposal is not None:
            proposal.set_user_id(user_id)
            wardrobe = adm.create_wardrobe(proposal)
            return wardrobe, 200
        else:
            return '', 500

# API Endpoints for Wardrobe

@wardrobe_ns.route('/wardrobes/<int:wardrobe_id>')
@wardrobe_ns.response(500, 'Server-Error')
@wardrobe_ns.param('wardrobe_id', 'ID of the wardrobe')
class WardrobeOperations(Resource):
    @wardrobe_ns.marshal_with(wardrobe)
    @secured
    def get(self, wardrobe_id):
        """Get a wardrobe by ID"""
        adm = Admin()
        wardrobe = adm.get_wardrobe_by_id(wardrobe_id)
        return wardrobe

    @wardrobe_ns.marshal_with(wardrobe)
    @wardrobe_ns.expect(wardrobe, validate=True)
    @secured
    def put(self, wardrobe_id):
        """Update a wardrobe"""
        adm = Admin()
        wardrobe = Wardrobe.from_dict()
        if wardrobe is not None:
            wardrobe.set_id(wardrobe_id)
            adm.save_wardrobe(wardrobe)
            return wardrobe, 200
        else:
            return '', 500

    @secured
    def delete(self, wardrobe_id):
        """Delete a wardrobe"""
        adm = Admin()
        wardrobe = adm.get_wardrobe_by_id(wardrobe_id)
        adm.delete_wardrobe(wardrobe)
        return '', 200

# API Endpoints for ClothingItem

@wardrobe_ns.route('/clothing-items')
@wardrobe_ns.response(500, 'Server-Error')
class ClothingListOperations(Resource):
    @wardrobe_ns.marshal_list_with(clothing_item)
    @secured
    def get(self):
        """Get all clothing items"""
        adm = Admin()
        items = adm.get_all_clothing_items()
        return items

    @wardrobe_ns.marshal_with(clothing_item, code=200)
    @wardrobe_ns.expect(clothing_item)
    @secured
    def post(self):
        """Create a new clothing item"""
        adm = Admin()
        proposal = ClothingItem.from_dict(api.payload)
        if proposal is not None:
            item = adm.create_clothing_item(proposal.get_wardrobe_id(), proposal.get_clothing_type_id(),
                                            proposal.get_clothing_item_name())
            return item, 200
        else:
            return '', 500

@wardrobe_ns.route('/clothing-items/<int:item_id>')
@wardrobe_ns.response(500, 'Server-Error')
@wardrobe_ns.param('item_id', 'ID of the clothing item')
class ClothingItemOperations(Resource):
    @wardrobe_ns.marshal_with(clothing_item)
    @secured
    def get(self, item_id):
        """Get a clothing item by ID"""
        adm = Admin()
        item = adm.get_clothing_item_by_id(item_id)
        return item

    @wardrobe_ns.marshal_with(clothing_item)
    @wardrobe_ns.expect(clothing_item, validate=True)
    @secured
    def put(self, item_id):
        """Update a clothing item"""
        adm = Admin()
        item = ClothingItem.from_dict(api.payload)
        if item is not None:
            item.set_id(item_id)
            adm.save_clothing_item(item)
            return item, 200
        else:
            return '', 500

    @secured
    def delete(self, item_id):
        """Delete a clothing item"""
        adm = Admin()
        item = adm.get_clothing_item_by_id(item_id)
        adm.delete_clothing_item(item)
        return '', 200

# API Endpoints for ClothingType

@wardrobe_ns.route('/clothing-types')
class ClothingTypeListOperations(Resource):
    @wardrobe_ns.marshal_list_with(clothing_type)
    @secured
    def get(self):
        """Get all clothing types"""
        adm = Admin()
        types = adm.get_all_clothing_types()
        return types

    @wardrobe_ns.marshal_with(clothing_type, code=201)
    @wardrobe_ns.expect(clothing_type)
    @secured
    def post(self):
        """Create a new clothing type"""
        adm = Admin()
        proposal = ClothingType.from_dict(api.payload)
        if proposal is not None:
            ctype = adm.create_clothing_type(proposal.get_type_name(), proposal.get_type_usage())
            return ctype, 201
        else:
            return '', 500

# API Endpoints for Styles

@wardrobe_ns.route('/styles')
@wardrobe_ns.response(500, 'Server-Error')
class StyleListOperations(Resource):
    @wardrobe_ns.marshal_list_with(style)
    @secured
    def get(self):
        """Get all styles"""
        adm = Admin()
        styles = adm.get_all_styles()
        return styles

    @wardrobe_ns.marshal_with(style, code=200)
    @wardrobe_ns.expect(style)
    @secured
    def post(self):
        """Create a new style"""
        adm = Admin()
        proposal = Style.from_dict(api.payload)
        if proposal is not None:
            style = adm.create_style(proposal.get_style_features(), proposal.get_style_constraints())
            return style, 200
        else:
            return '', 500

@wardrobe_ns.route('/styles/<int:style_id>')
@wardrobe_ns.response(500, 'Server-Error')
@wardrobe_ns.param('style_id', 'ID of the style')
class StyleOperations(Resource):
    @wardrobe_ns.marshal_with(style)
    @secured
    def get(self, style_id):
        """Get a style by ID"""
        adm = Admin()
        style = adm.get_style_by_id(style_id)
        return style

    @wardrobe_ns.marshal_with(style)
    @wardrobe_ns.expect(style, validate=True)
    @secured
    def put(self, style_id):
        """Update a style"""
        adm = Admin()
        style = Style.from_dict(api.payload)
        if style is not None:
            style.set_id(style_id)
            adm.save_style(style)
            return style, 200
        else:
            return '', 500

    @secured
    def delete(self, style_id):

        adm = Admin()
        style = adm.get_style_by_id(style_id)
        adm.delete_style(style)
        return '', 200

# API Endpoints for Outfits

@wardrobe_ns.route('/outfits')
@wardrobe_ns.response(500, 'Server-Error')
class OutfitListOperations(Resource):
    @wardrobe_ns.marshal_list_with(outfit)
    @secured
    def get(self):
        """Get all outfits"""
        adm = Admin()
        outfits = adm.get_all_outfits()
        return outfits

    @wardrobe_ns.marshal_with(outfit, code=200)
    @wardrobe_ns.expect(outfit)
    @secured
    def post(self):
        """Create a new outfit"""
        adm = Admin()
        proposal = Outfit.from_dict(api.payload)
        if proposal is not None:
            outfit = adm.create_outfit(proposal.get_outfit_name(), proposal.get_style_id())
            return outfit, 200
        else:
            return '', 500

@wardrobe_ns.route('/outfits/<int:outfit_id>')
@wardrobe_ns.response(500, 'Server-Error')
@wardrobe_ns.param('outfit_id', 'ID of the outfit')
class OutfitOperations(Resource):
    @wardrobe_ns.marshal_with(outfit)
    @secured
    def get(self, outfit_id):
        """Get an outfit by ID"""
        adm = Admin()
        outfit = adm.get_outfit_by_id(outfit_id)
        return outfit

    @wardrobe_ns.marshal_with(outfit)
    @wardrobe_ns.expect(outfit, validate=True)
    @secured
    def put(self, outfit_id):
        """Update an outfit"""
        adm = Admin()
        outfit = Outfit.from_dict(api.payload)
        if outfit is not None:
            outfit.set_id(outfit_id)
            adm.save_outfit(outfit)
            return outfit, 200
        else:
            return '', 500

    @secured
    def delete(self, outfit_id):
        """Delete an outfit"""
        adm = Admin()
        outfit = adm.get_outfit_by_id(outfit_id)
        adm.delete_outfit(outfit)
        return '', 200

# API Endpoints for Clothing Items of a User

@wardrobe_ns.route('/user/<int:user_id>/clothing-items')
@wardrobe_ns.response(500, 'Server-Error')
@wardrobe_ns.param('user_id', 'ID of the user')
class UserClothingItemsOperations(Resource):
    @wardrobe_ns.marshal_list_with(clothing_item)
    @secured
    def get(self, user_id):
        """Get all clothing items of a user"""
        adm = Admin()
        user = adm.get_user_by_id(user_id)
        if user is not None:
            items = adm.get_clothing_type_by_id(user)
            return items
        else:
            return "User not found", 500

# API Endpoints for Style-based Outfit Proposals

@wardrobe_ns.route('/user/<int:user_id>/outfit-proposals/<int:style_id>')
@wardrobe_ns.response(500, 'Server-Error')
@wardrobe_ns.param('user_id', 'ID of the user')
@wardrobe_ns.param('style_id', 'ID of the style')
class OutfitProposalOperations(Resource):
    @wardrobe_ns.marshal_with(outfit)
    @secured
    def get(self, user_id, style_id):
        """Generate outfit proposals based on style and available clothing items"""
        adm = Admin()
        user = adm.get_user_by_id(user_id)
        style = adm.get_style_by_id(style_id)
        if user is not None and style is not None:
            proposal = adm.generate_outfit_for_style(style.get_id())
            return proposal
        else:
            return "User or Style not found", 500

# API Endpoints for Constraints

@wardrobe_ns.route('/constraints')
class ConstraintListOperations(Resource):
    @wardrobe_ns.marshal_list_with(constraint)
    @secured
    def get(self):
        """Get all constraints"""
        adm = Admin()
        constraints = adm.get_all_constraints()
        return constraints

@wardrobe_ns.route('/unary-constraints')
class UnaryConstraintOperations(Resource):
    @wardrobe_ns.marshal_with(unary_constraint, code=201)
    @wardrobe_ns.expect(unary_constraint)
    @secured
    def post(self):
        """Create a new unary constraint"""
        adm = Admin()
        payload = api.payload
        style_id = payload.get('style_id')
        if style_id is not None:
            constraint = adm.create_unary_constraint(style_id)
            return constraint, 201
        else:
            return '', 500

@wardrobe_ns.route('/binary-constraints')
class BinaryConstraintOperations(Resource):
    @wardrobe_ns.marshal_with(binary_constraint, code=201)
    @wardrobe_ns.expect(binary_constraint)
    @secured
    def post(self):
        """Create a new binary constraint"""
        adm = Admin()
        payload = api.payload
        item_1_id = payload.get('item_1_id')
        item_2_id = payload.get('item_2_id')

        if item_1_id and item_2_id is not None:
            constraint = adm.create_binary_constraint(item_1_id, item_2_id)
            return constraint, 201
        else:
            return '', 500

@wardrobe_ns.route('/cardinality-constraints')
class CardinalityConstraintOperations(Resource):
    @wardrobe_ns.marshal_with(cardinality_constraint, code=201)
    @wardrobe_ns.expect(cardinality_constraint)
    @secured
    def post(self):
        """Create a new cardinality constraint"""
        adm = Admin()
        payload = api.payload
        objects = payload.get('objects')
        min_count = payload.get('min_count')
        max_count = payload.get('max_count')
        if (objects is not None
                and min_count is not None
                and max_count is not None):
            constraint = adm.create_cardinality_constraint(objects, min_count, max_count)
            return constraint, 201
        else:
            return '', 500

@wardrobe_ns.route('/mutex-constraints')
class MutexConstraintOperations(Resource):
    """
    @wardrobe_ns.marshal_list_with(mutex_constraint)
    @secured
    def get(self):
        Get all mutex constraints
        adm = Admin()
        constraints = adm.get_all()
        return constraints"""

    @wardrobe_ns.marshal_with(mutex_constraint, code=201)
    @wardrobe_ns.expect(mutex_constraint)
    @secured
    def post(self):
        """Create a new mutex constraint"""
        adm = Admin()
        payload = api.payload
        mutex_pairs = payload.get('mutex_pairs')
        if mutex_pairs is not None:
            constraint = adm.create_mutex_constraint(mutex_pairs)
            return constraint, 201
        else:
            return '', 500

@wardrobe_ns.route('/implication-constraints')
class ImplicationConstraintOperations(Resource):
    """@wardrobe_ns.marshal_list_with(implication_constraint)
    @secured
    def get(self):
        Get all implication constraints
        adm = Admin()
        constraints = adm.get_all_implication_constraints()
        return constraints"""

    @wardrobe_ns.marshal_with(implication_constraint, code=201)
    @wardrobe_ns.expect(implication_constraint)
    @secured
    def post(self):
        """Create a new implication constraint"""
        adm = Admin()
        payload = api.payload
        if_type = payload.get('if_type')
        then_type = payload.get('then_type')
        if if_type is not None and then_type is not None:
            constraint = adm.create_implication_constraint(if_type, then_type)
            return constraint, 201
        else:
            return '', 500

if __name__ == '__main__':
    app.run(debug=True)