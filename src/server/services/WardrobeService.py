# src/server/service/WardrobeService.py

from flask import request
from flask_restx import Namespace, Resource, fields
from admin.Administration import WardrobeAdministration
from SecurityDecorator import SecurityDecorator

api = Namespace('wardrobe', description='Wardrobe related operations')

# API Models
wardrobe_model = api.model('Wardrobe', {
    'id': fields.String(readonly=True),
    'person_id': fields.String(required=True),
    'create_time': fields.DateTime(readonly=True)
})

clothing_item_model = api.model('ClothingItem', {
    'id': fields.String(readonly=True),
    'wardrobe_id': fields.String(required=True),
    'type_id': fields.String(required=True),
    'name': fields.String(required=True),
    'create_time': fields.DateTime(readonly=True)
})

@api.route('/')
class WardrobeListOperations(Resource):
    @SecurityDecorator.check_valid_token
    @api.marshal_list_with(wardrobe_model)
    def get(self):
        """Liste aller Kleiderschränke"""
        adm = WardrobeAdministration()
        return adm.get_all_wardrobes()

@api.route('/<id>')
@api.response(404, 'Kleiderschrank nicht gefunden')
class WardrobeOperations(Resource):
    @SecurityDecorator.check_valid_token
    @api.marshal_with(wardrobe_model)
    def get(self, id):
        """Kleiderschrank by ID"""
        adm = WardrobeAdministration()
        result = adm.get_wardrobe_by_id(id)
        if result is not None:
            return result
        api.abort(404, f"Kleiderschrank {id} nicht gefunden")

    @SecurityDecorator.check_valid_token
    def delete(self, id):
        """Kleiderschrank löschen"""
        adm = WardrobeAdministration()
        wardrobe = adm.get_wardrobe_by_id(id)
        if wardrobe is not None:
            adm.delete_wardrobe(wardrobe)
            return '', 204
        api.abort(404, f"Kleiderschrank {id} nicht gefunden")

@api.route('/person/<person_id>')
@api.response(404, 'Kleiderschrank für Person nicht gefunden')
class WardrobePersonOperations(Resource):
    @SecurityDecorator.check_valid_token
    @api.marshal_with(wardrobe_model)
    def get(self, person_id):
        """Kleiderschrank einer Person"""
        adm = WardrobeAdministration()
        result = adm.get_wardrobe_by_person(person_id)
        if result is not None:
            return result
        api.abort(404, f"Kein Kleiderschrank für Person {person_id} gefunden")

@api.route('/<id>/items')
@api.response(404, 'Kleiderschrank nicht gefunden')
class WardrobeItemOperations(Resource):
    @SecurityDecorator.check_valid_token
    @api.marshal_list_with(clothing_item_model)
    def get(self, id):
        """Alle Kleidungsstücke eines Kleiderschranks"""
        adm = WardrobeAdministration()
        wardrobe = adm.get_wardrobe_by_id(id)
        if wardrobe is not None:
            return adm.get_items_of_wardrobe(id)
        api.abort(404, f"Kleiderschrank {id} nicht gefunden")

    @SecurityDecorator.check_valid_token
    @api.expect(clothing_item_model)
    @api.marshal_with(clothing_item_model, code=201)
    def post(self, id):
        """Kleidungsstück zu Kleiderschrank hinzufügen"""
        adm = WardrobeAdministration()
        wardrobe = adm.get_wardrobe_by_id(id)
        if wardrobe is not None:
            data = api.payload
            return adm.create_clothing_item(
                id,
                data['type_id'],
                data['name']
            ), 201
        api.abort(404, f"Kleiderschrank {id} nicht gefunden")