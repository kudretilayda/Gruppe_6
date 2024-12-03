# src/server/service/OutfitService.py

from flask import request
from flask_restx import Namespace, Resource, fields
from admin.Administration import WardrobeAdministration
from SecurityDecorator import SecurityDecorator

api = Namespace('outfit', description='Outfit related operations')

# API Models
outfit_model = api.model('Outfit', {
    'id': fields.String(readonly=True),
    'style_id': fields.String(required=True),
    'name': fields.String(required=True),
    'items': fields.List(fields.String),
    'create_time': fields.DateTime(readonly=True)
})

outfit_suggestion_model = api.model('OutfitSuggestion', {
    'style_id': fields.String(required=True),
    'wardrobe_id': fields.String(required=True)
})

@api.route('/')
class OutfitListOperations(Resource):
    @SecurityDecorator.check_valid_token
    @api.marshal_list_with(outfit_model)
    def get(self):
        """Liste aller Outfits"""
        adm = WardrobeAdministration()
        return adm.get_all_outfits()

    @SecurityDecorator.check_valid_token
    @api.expect(outfit_model)
    @api.marshal_with(outfit_model, code=201)
    def post(self):
        """Outfit erstellen"""
        adm = WardrobeAdministration()
        data = api.payload
        return adm.create_outfit(
            data['style_id'],
            data['name'],
            data.get('items', [])
        ), 201

@api.route('/<id>')
@api.response(404, 'Outfit nicht gefunden')
class OutfitOperations(Resource):
    @SecurityDecorator.check_valid_token
    @api.marshal_with(outfit_model)
    def get(self, id):
        """Outfit by ID"""
        adm = WardrobeAdministration()
        result = adm.get_outfit_by_id(id)
        if result is not None:
            return result
        api.abort(404, f"Outfit {id} nicht gefunden")

    @SecurityDecorator.check_valid_token
    @api.expect(outfit_model)
    @api.marshal_with(outfit_model)
    def put(self, id):
        """Outfit aktualisieren"""
        adm = WardrobeAdministration()
        outfit = adm.get_outfit_by_id(id)
        if outfit is not None:
            data = api.payload
            outfit.set_name(data['name'])
            outfit.set_items(data.get('items', []))
            adm.update_outfit(outfit)
            return outfit
        api.abort(404, f"Outfit {id} nicht gefunden")

    @SecurityDecorator.check_valid_token
    def delete(self, id):
        """Outfit löschen"""
        adm = WardrobeAdministration()
        outfit = adm.get_outfit_by_id(id)
        if outfit is not None:
            adm.delete_outfit(outfit)
            return '', 204
        api.abort(404, f"Outfit {id} nicht gefunden")

@api.route('/suggest')
class OutfitSuggestionOperations(Resource):
    @SecurityDecorator.check_valid_token
    @api.expect(outfit_suggestion_model)
    @api.marshal_list_with(outfit_model)
    def post(self):
        """Outfit-Vorschläge generieren"""
        adm = WardrobeAdministration()
        data = api.payload
        suggestions = adm.generate_outfit_suggestions(
            data['style_id'],
            data['wardrobe_id']
        )
        return suggestions