# src/server/service/StyleService.py

from flask import request
from flask_restx import Namespace, Resource, fields
from Admin import WardrobeAdministration
from SecurityDecorator import SecurityDecorator

api = Namespace('style', description='Style related operations')

# API Models
style_model = api.model('Style', {
    'id': fields.String(readonly=True),
    'name': fields.String(required=True),
    'features': fields.String(required=True),
    'create_time': fields.DateTime(readonly=True)
})

@api.route('/')
class StyleListOperations(Resource):
    @SecurityDecorator.check_valid_token
    @api.marshal_list_with(style_model)
    def get(self):
        """Liste aller Styles"""
        adm = WardrobeAdministration()
        return adm.get_all_styles()

    @SecurityDecorator.check_valid_token
    @api.expect(style_model)
    @api.marshal_with(style_model, code=201)
    def post(self):
        """Style erstellen"""
        adm = WardrobeAdministration()
        data = api.payload
        return adm.create_style(
            data['name'],
            data['features']
        ), 201

@api.route('/<id>')
@api.response(404, 'Style nicht gefunden')
class StyleOperations(Resource):
    @SecurityDecorator.check_valid_token
    @api.marshal_with(style_model)
    def get(self, id):
        """Style by ID"""
        adm = WardrobeAdministration()
        result = adm.get_style_by_id(id)
        if result is not None:
            return result
        api.abort(404, f"Style {id} nicht gefunden")

    @SecurityDecorator.check_valid_token
    @api.expect(style_model)
    @api.marshal_with(style_model)
    def put(self, id):
        """Style aktualisieren"""
        adm = WardrobeAdministration()
        style = adm.get_style_by_id(id)
        if style is not None:
            data = api.payload
            style.set_name(data['name'])
            style.set_features(data['features'])
            adm.update_style(style)
            return style
        api.abort(404, f"Style {id} nicht gefunden")

    @SecurityDecorator.check_valid_token
    def delete(self, id):
        """Style löschen"""
        adm = WardrobeAdministration()
        style = adm.get_style_by_id(id)
        if style is not None:
            adm.delete_style(style)
            return '', 204
        api.abort(404, f"Style {id} nicht gefunden")

@api.route('/<id>/check/<wardrobe_id>')
@api.response(404, 'Style oder Wardrobe nicht gefunden')
class StyleCheckOperations(Resource):
    @SecurityDecorator.check_valid_token
    def get(self, id, wardrobe_id):
        """Prüft, ob ein Style mit dem Inhalt eines Kleiderschranks möglich ist"""
        adm = WardrobeAdministration()
        style = adm.get_style_by_id(id)
        wardrobe = adm.get_wardrobe_by_id(wardrobe_id)
        
        if style is None:
            api.abort(404, f"Style {id} nicht gefunden")
        if wardrobe is None:
            api.abort(404, f"Wardrobe {wardrobe_id} nicht gefunden")
            
        return {
            'possible': adm.check_style_possible(style, wardrobe),
            'missing_items': adm.get_missing_items_for_style(style, wardrobe)
        }