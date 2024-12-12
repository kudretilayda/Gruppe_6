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
from server.Constraints.Constraint import Constraint, BinaryConstraint, UnaryConstraint, CardinalityConstraint, MutexConstraint, ImplicationConstraint
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

user = api.inherit('User', bo, {
    'user_id': fields.String(attribute='_user_id', description='User ID'),
    'google_id': fields.String(attribute='_google_id', description='Google user ID'),
    'first_name': fields.String(attribute='_first_name', description='First name'),
    'last_name': fields.String(attribute='_last_name', description='Last name'),
    'nick_name': fields.String(attribute='_nick_name', description='Nickname'),
    'email': fields.String(attribute='_email', description='Email address')
})

wardrobe = api.inherit('Wardrobe', bo, {
    'user_id': fields.Integer(attribute='_user_id', description='ID des Besitzers'),
})

clothing_type = api.inherit('ClothingType', bo, {
    'type_name': fields.String(attribute='_type_name', description='Bezeichnung des Kleidungstyps'),
    'type_usage': fields.String(attribute='_type_usage', description='Verwendungszweck des Kleidungstyps'),
})

clothing_item = api.inherit('ClothingItem', bo, {
    'wardrobe_id': fields.Integer(attribute='_wardrobe_id', description='ID des zugehörigen Kleiderschranks'),
    'clothing_type_id': fields.Integer(attribute='_clothing_type_id', description='ID des Kleidungstyps'), 
    'clothing_item_name': fields.String(attribute='_clothing_item_name', description='Bezeichnung des Kleidungsstücks'),
    'color': fields.String(attribute='_color', description='Farbe des Kleidungsstücks'),
    'brand': fields.String(attribute='_brand', description='Marke des Kleidungsstücks'),
    'season': fields.String(attribute='_season', description='Saison für das Kleidungsstück'),
})

style = api.inherit('Style', bo, {
    'style_features': fields.String(attribute='_style_features', description='Merkmale des Stils'),
    'style_constraints': fields.String(attribute='_style_constraints', description='Beschränkungen des Stils'),
})

outfit = api.inherit('Outfit', bo, {
    'outfit_name': fields.String(attribute='_outfit_name', description='Name des Outfits'),
    'style_id': fields.Integer(attribute='_style_id', description='ID des zugehörigen Stils'),
})

constraint = api.inherit('Constraint', bo, {
    'style_id': fields.Integer(attribute='_style_id', description='ID des zugehörigen Stils'),
    'constraint_type': fields.String(attribute='_constraint_type', description='Art des Constraints'),
    'attribute': fields.String(attribute='_attribute', description='Betroffenes Attribut'),
    'constrain': fields.String(attribute='_constrain', description='Bedingung'),
    'val': fields.String(attribute='_val', description='Wert'),
})

unary_constraint = api.inherit('UnaryConstraint', constraint, {
    'reference_object_id': fields.Integer(attribute='_reference_object_id', description='ID des Referenzobjekts'),
})

binary_constraint = api.inherit('BinaryConstraint', constraint, {
    'reference_object1_id': fields.Integer(attribute='_reference_object1_id', description='ID des ersten Referenzobjekts'),
    'reference_object2_id': fields.Integer(attribute='_reference_object2_id', description='ID des zweiten Referenzobjekts'),
})

mutex_constraint = api.inherit('MutexConstraint', constraint, {
    'item_type_1': fields.Integer(attribute='_item_type_1', description='ID des ersten Kleidungstyps'),
    'item_type_2': fields.Integer(attribute='_item_type_2', description='ID des zweiten Kleidungstyps'),
})

implication_constraint = api.inherit('ImplicationConstraint', constraint, {
    'if_type': fields.Integer(attribute='_if_type', description='ID des "wenn" Kleidungstyps'),
    'then_type': fields.Integer(attribute='_then_type', description='ID des "dann" Kleidungstyps'),
})

cardinality_constraint = api.inherit('CardinalityConstraint', constraint, {
    'item_type': fields.Integer(attribute='_item_type', description='ID des betroffenen Kleidungstyps'),
    'min_count': fields.Integer(attribute='_min_count', description='Minimale Anzahl'),
    'max_count': fields.Integer(attribute='_max_count', description='Maximale Anzahl'),
})

#API Endpoints für User

@wardrobe_ns.route('/user')
@wardrobe_ns.response(500, 'Server-Error')
class UserListOperations(Resource):
    @wardrobe_ns.marshal_list_with(user)
    @secured
    def get(self):
        """Auslesen aller User"""
        adm = Admin()
        user = adm.get_all_user()
        return user
    
@wardrobe_ns.marshal_with(user, code=200)
@wardrobe_ns.expect(user)
@secured
def post(self):
        """Neuen User anlegen"""
        adm = Admin()
        proposal = User.from_dict(api.payload)
        if proposal is not None:
            p = adm.create_user(
                 proposal.get_google_id(),
                 proposal.get_first_name(),
                 proposal.get_last_name(),
                 proposal.get_nickname(),
                 proposal.get_email()
            )
            return p, 200
        else:
            return '', 500
         # 500: server-fehler

@wardrobe_ns.route('/user/<int:user_id>')
@wardrobe_ns.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@wardrobe_ns.param('user_id', 'Die ID des Person-Objekts')
class UserOperations(Resource):
    @wardrobe_ns.marshal_with(user)
    @secured
    def get(self, user_id):
        adm = Admin()
        pers = adm.get_user_by_id(user_id)
        return User

    @wardrobe_ns.marshal_with(user)
    @wardrobe_ns.expect(user, validate=True)
    @secured
    def put(self, user_id):
        adm = Admin()
        p = user.from_dict(api.payload)

        if p is not None:
            p.set_id(user_id)
            adm.save_user(p)
            return p, 200
        else:
            return '', 500

    @secured
    def delete(self, user_id):
        adm = Admin()
        pers = adm.get_user_by_id(user_id)
        adm.delete_user(User)
        return '', 200


@wardrobe_ns.route('/user/<int:user_id>/wardrobe')
@wardrobe_ns.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@wardrobe_ns.param('user_id', 'Die ID der Person')
class UserWardrobeOperations(Resource):
    @wardrobe_ns.marshal_with(wardrobe)
    @secured
    def get(self, user_id):
        adm = Admin()
        w = adm.get_wardrobe_by_person(user_id)
        return w

    @wardrobe_ns.marshal_with(wardrobe, code=200)
    @wardrobe_ns.expect(wardrobe)
    @secured
    def post(self, user_id):
        adm = Admin()
        proposal = Wardrobe.from_dict(api.payload)

        if proposal is not None:
            proposal.set_person_id(user_id)
            w = adm.create_wardrobe(proposal)
            return w, 200
        else:
            return '', 500


#API Endpoints für Wardrobe

@wardrobe_ns.route('/wardrobes/<int:wardrobe_id>')
@wardrobe_ns.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@wardrobe_ns.param('wardrobe_id', 'Die ID des Wardrobes')
class WardrobeOperations(Resource):
    @wardrobe_ns.marshal_with(wardrobe)
    @secured
    def get(self, wardrobe_id):
        adm = Admin()
        ward = adm.get_wardrobe_by_id(wardrobe_id)
        return ward

    @wardrobe_ns.marshal_with(wardrobe)
    @wardrobe_ns.expect(wardrobe, validate=True)
    @secured
    def put(self, wardrobe_id):
        adm = Admin()
        w = Wardrobe.from_dict(api.payload)

        if w is not None:
            w.set_id(wardrobe_id)
            adm.save_wardrobe(w)
            return w, 200
        else:
            return '', 500

    @secured
    def delete(self, wardrobe_id):
        adm = Admin()
        ward = adm.get_wardrobe_by_id(wardrobe_id)
        adm.delete_wardrobe(ward)
        return '', 200


#API Endpoints für ClothingItem

@wardrobe_ns.route('/clothing-items')
@wardrobe_ns.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class ClothingListOperations(Resource):
    @wardrobe_ns.marshal_list_with(clothing_item)
    @secured
    def get(self):
        """Auslesen aller Kleidungsstücke"""
        adm = Admin()
        items = adm.get_all_clothing_items()
        return items

    @wardrobe_ns.marshal_with(clothing_item, code=200)
    @wardrobe_ns.expect(clothing_item)
    @secured
    def post(self):
        """Anlegen eines neuen Kleidungsstücks"""
        adm = Admin()
        proposal = clothing_item.from_dict(api.payload)
        
        if proposal is not None:
            c = adm.create_clothing_item(proposal.get_type(), proposal.get_owner())
            return c, 200
        else:
            return '', 500


#API Endpoints für ClothingType

@wardrobe_ns.route('/clothing-types')
class ClothingTypeListOperations(Resource):
    @wardrobe_ns.marshal_list_with(clothing_type)
    @secured
    def get(self):
        adm = Admin()
        types = adm.get_all_clothing_types()
        return types

    @wardrobe_ns.marshal_with(clothing_type, code=201)
    @wardrobe_ns.expect(clothing_type)
    @secured
    def post(self):
        adm = Admin()
        proposal = ClothingType.from_dict(api.payload)

        if proposal is not None:
            ctype = adm.create_clothing_type(proposal)
            return ctype, 200
        else:
            return '', 500


#API Endpoints für ClothingItem

@wardrobe_ns.route('/clothing-items/<int:item_id>')
@wardrobe_ns.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@wardrobe_ns.param('item_id', 'Die ID des Kleidungsstücks')
class ClothingItemOperations(Resource):
    @wardrobe_ns.marshal_with(clothing_item)
    @secured
    def get(self, item_id):
        adm = Admin()
        item = adm.get_clothing_item_by_id(item_id)
        return item

    @wardrobe_ns.marshal_with(clothing_item)
    @wardrobe_ns.expect(clothing_item, validate=True)
    @secured  
    def put(self, item_id):
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
        adm = Admin()
        item = adm.get_clothing_item_by_id(item_id)
        adm.delete_clothing_item(item)
        return '', 200


#API Endpoints für Styles

@wardrobe_ns.route('/styles')
@wardrobe_ns.response(500, 'Server-Error.')
class StyleListOperations(Resource):
    @wardrobe_ns.marshal_list_with(style)
    @secured
    def get(self):
        """Auslesen aller Styles"""
        adm = Admin()
        styles = adm.get_all_styles()
        return styles

    @wardrobe_ns.marshal_with(style, code=200)
    @wardrobe_ns.expect(style)
    @secured
    def post(self):
        """Anlegen eines neuen Styles"""
        adm = Admin()
        proposal = Style.from_dict(api.payload)
        
        if proposal is not None:
            s = adm.create_style(proposal.get_features(),
                                 proposal.get_constraints()
            )
            return s, 200
        else:
            return '', 500


#API Endpoints für Outfits

@wardrobe_ns.route('/outfits')
@wardrobe_ns.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class OutfitListOperations(Resource):
    @wardrobe_ns.marshal_list_with(outfit)
    @secured
    def get(self):
        """Auslesen aller Outfits"""
        adm = Admin()
        outfits = adm.get_all_outfits()
        return outfits

    @wardrobe_ns.marshal_with(outfit, code=200)
    @wardrobe_ns.expect(outfit)
    @secured
    def post(self):
        """Anlegen eines neuen Outfits"""
        adm = Admin()
        proposal = Outfit.from_dict(api.payload)
        
        if proposal is not None:
            o = adm.create_outfit(proposal.get_style(), proposal.get_items())
            return o, 200
        else:
            return '', 500
    @secured
    def delete(self, outfit_id):
        adm = Admin()
        outf = adm.get_outfit_by_id(outfit_id)
        adm.delete_outfit(outf)
        return '', 200


#API Endpoint für Kleidungsstücke einer Person
@wardrobe_ns.route('/persons/<int:id>/clothing-items')
@wardrobe_ns.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@wardrobe_ns.param('id', 'Die ID der Person')
class PersonClothingOperations(Resource):
    @wardrobe_ns.marshal_list_with(clothing_item)
    @secured
    def get(self, id):
        """Auslesen aller Kleidungsstücke einer bestimmten Person"""
        adm = Admin()
        person = adm.get_person_by_id(id)
        
        if person is not None:
            items = adm.get_clothing_items_by_person(user)
            return items
        else:
            return "Person not found", 500


#API Endpoint für Style-basierte Outfit-Vorschläge

@wardrobe_ns.route('/user/<int:id>/outfit-proposals/<int:style_id>')
@wardrobe_ns.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@wardrobe_ns.param('id', 'Die ID der Person')
@wardrobe_ns.param('style_id', 'Die ID des Styles')
class OutfitProposalOperations(Resource):
    @wardrobe_ns.marshal_with(outfit)
    @secured
    def get(self, id, style_id):
        """Generiert Outfit-Vorschläge basierend auf Style und verfügbarer Kleidung"""
        adm = Admin()
        person = adm.get_user_by_id(id)
        style = adm.get_style_by_id(style_id)
        
        if person is not None and style is not None:
            proposal = adm.generate_outfit_proposal(user, style)
            return proposal
        else:
            return "User or Style not found", 500


@wardrobe_ns.route('/styles')
class StyleListOperations(Resource):
    @wardrobe_ns.marshal_list_with(style) 
    @secured
    def get(self):
        adm = Admin()
        styles = adm.get_all_styles()
        return styles

    @wardrobe_ns.marshal_with(style, code=200)
    @wardrobe_ns.expect(style)
    @secured
    def post(self):
        adm = Admin()
        proposal = Style.from_dict(api.payload)
        if proposal is not None:
            s = adm.create_style(proposal)
            return s, 200
        else:
            return '', 500

@wardrobe_ns.route('/styles/<int:style_id>')
@wardrobe_ns.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.') 
@wardrobe_ns.param('style_id', 'Die ID des Stils')
class StyleOperations(Resource):
    @wardrobe_ns.marshal_with(style)
    @secured
    def get(self, style_id):
        adm = Admin()
        s = adm.get_style_by_id(style_id)
        return s

    @wardrobe_ns.marshal_with(style)
    @wardrobe_ns.expect(style, validate=True)
    @secured
    def put(self, style_id):
        adm = Admin()
        s = Style.from_dict(api.payload)

        if s is not None:
            s.set_id(style_id)
            adm.save_style(s)
            return s, 200
        else:
            return '', 500

    @secured
    def delete(self, style_id):
        adm = Admin()
        s = adm.get_style_by_id(style_id)
        adm.delete_style(s)
        return '', 200


#API Endpoint für Constraints


@wardrobe_ns.route('/constraints')
class ConstraintListOperations(Resource):
    @wardrobe_ns.marshal_list_with(constraint)
    @secured
    def get(self):
        adm = Admin()
        constraints = adm.get_all_constraints()
        return constraints

@wardrobe_ns.route('/binary-constraints')
class BinaryConstraintOperations(Resource):
    @wardrobe_ns.marshal_with(binary_constraint, code=201)
    @wardrobe_ns.expect(binary_constraint)
    @secured
    def post(self):
        adm = Admin()
        proposal = BinaryConstraint.from_dict(api.payload)
        if proposal is not None:
            bc = adm.create_binary_constraint(proposal)
            return bc, 201
        else:
            return '', 500

@wardrobe_ns.route('/unary-constraints')
class UnaryConstraintOperations(Resource):
    @wardrobe_ns.marshal_with(unary_constraint, code=201)
    @wardrobe_ns.expect(unary_constraint)  
    @secured
    def post(self):
        adm = Admin()
        proposal = UnaryConstraint.from_dict(api.payload)
        if proposal is not None:
            uc = adm.create_unary_constraint(proposal)
            return uc, 201
        else:
            return '', 500

@wardrobe_ns.route('/cardinality-constraints')
class CardinalityConstraintOperations(Resource):
    @wardrobe_ns.marshal_with(cardinality_constraint, code=201)
    @wardrobe_ns.expect(cardinality_constraint)
    @secured 
    def post(self):
        adm = Admin()
        proposal = CardinalityConstraint.from_dict(api.payload)
        if proposal is not None:
            cc = adm.create_cardinality_constraint(proposal)
            return cc, 201
        else:
            return '', 500

@wardrobe_ns.route('/mutex-constraints')  
class MutexConstraintOperations(Resource):
    @wardrobe_ns.marshal_list_with(mutex_constraint)
    @secured
    def get(self):
        adm = Admin()
        constraints = adm.get_all_mutex_constraints()
        return constraints

    @wardrobe_ns.marshal_with(mutex_constraint, code=201)
    @wardrobe_ns.expect(mutex_constraint) 
    @secured
    def post(self):
        adm = Admin()
        proposal = MutexConstraint.from_dict(api.payload)
        if proposal is not None:
            mc = adm.create_mutex_constraint(proposal)
            return mc, 201
        else:
            return '', 500

@wardrobe_ns.route('/implication-constraints')
class ImplicationConstraintOperations(Resource):  
    @wardrobe_ns.marshal_list_with(implication_constraint)
    @secured  
    def get(self):
        adm = Admin()
        constraints = adm.get_all_implication_constraints()
        return constraints

    @wardrobe_ns.marshal_with(implication_constraint, code=201)
    @wardrobe_ns.expect(implication_constraint)
    @secured
    def post(self):  
        adm = Admin()
        proposal = ImplicationConstraint.from_dict(api.payload)
        if proposal is not None:
            ic = adm.create_implication_constraint(proposal)
            return ic, 201
        else:  
            return '', 500
            
if __name__ == '__main__':
    app.run(debug=True)












