# src/server/service/ClothingService.py

from flask import request
from flask_restx import Namespace, Resource, fields
from src.admin.Admin import WardrobeAdministration
from SecurityDecorator import SecurityDecorator

api = Namespace('clothing', description='Clothing related operations')

# API Models
clothing_type_model = api.model('ClothingType', {
    'id': fields.String(readonly=True),
    'name': fields.String(required=True),
    'usage': fields.String(required=True),
    'create_time': fields.DateTime(readonly=True)
})

clothing_item_model = api.model('ClothingItem', {
    'id': fields.String(readonly=True),
    'wardrobe_id': fields.String(required=True),
    'type_id': fields.String(required=True),
    'name': fields.String(required=True),
    'create_time': fields.DateTime(readonly=True)
})

# Clothing Type Routes
@api.route('/types')
class ClothingTypeListOperations(Resource):
    @SecurityDecorator.check_valid_token
    @api.marshal_list_with(clothing_type_model)
    def get(self):
        """Liste aller Kleidungstypen"""
        adm = WardrobeAdministration()
        return adm.get_all_clothing_types()

    @SecurityDecorator.check_valid_token
    @api.expect(clothing_type_model)
    @api.marshal_with(clothing_type_model, code=201)
    def post(self):
        """Kleidungstyp erstellen"""
        adm = WardrobeAdministration()
        data = api.payload
        return adm.create_clothing_type(
            data['name'],
            data['usage']
        ), 201

@api.route('/types/<id>')
@api.response(404, 'Kleidungstyp nicht gefunden')
class ClothingTypeOperations(Resource):
    @SecurityDecorator.check_valid_token
    @api.marshal_with(clothing_type_model)
    def get(self, id):
        """Kleidungstyp by ID"""
        adm = WardrobeAdministration()
        result = adm.get_clothing_type_by_id(id)
        if result is not None:
            return result
        api.abort(404, f"Kleidungstyp {id} nicht gefunden")

    @SecurityDecorator.check_valid_token
    @api.expect(clothing_type_model)
    @api.marshal_with(clothing_type_model)
    def put(self, id):
        """Kleidungstyp aktualisieren"""
        adm = WardrobeAdministration()
        type = adm.get_clothing_type_by_id(id)
        if type is not None:
            data = api.payload
            type.set_name(data['name'])
            type.set_usage(data['usage'])
            adm.update_clothing_type(type)
            return type
        api.abort(404, f"Kleidungstyp {id} nicht gefunden")

    @SecurityDecorator.check_valid_token
    def delete(self, id):
        """Kleidungstyp löschen"""
        adm = WardrobeAdministration()
        type = adm.get_clothing_type_by_id(id)
        if type is not None:
            adm.delete_clothing_type(type)
            return '', 204
        api.abort(404, f"Kleidungstyp {id} nicht gefunden")

# Clothing Item Routes
@api.route('/items')
class ClothingItemListOperations(Resource):
    @SecurityDecorator.check_valid_token
    @api.marshal_list_with(clothing_item_model)
    def get(self):
        """Liste aller Kleidungsstücke"""
        adm = WardrobeAdministration()
        return adm.get_all_clothing_items()

@api.route('/items/<id>')
@api.response(404, 'Kleidungsstück nicht gefunden')
class ClothingItemOperations(Resource):
    @SecurityDecorator.check_valid_token
    @api.marshal_with(clothing_item_model)
    def get(self, id):
        """Kleidungsstück by ID"""
        adm = WardrobeAdministration()
        result = adm.get_clothing_item_by_id(id)
        if result is not None:
            return result
        api.abort(404, f"Kleidungsstück {id} nicht gefunden")

    @SecurityDecorator.check_valid_token
    @api.expect(clothing_item_model)
    @api.marshal_with(clothing_item_model)
    def put(self, id):
        """Kleidungsstück aktualisieren"""
        adm = WardrobeAdministration()
        item = adm.get_clothing_item_by_id(id)
        if item is not None:
            data = api.payload
            item.set_name(data['name'])
            item.set_type_id(data['type_id'])
            adm.update_clothing_item(item)
            return item
        api.abort(404, f"Kleidungsstück {id} nicht gefunden")

    @SecurityDecorator.check_valid_token
    def delete(self, id):
        """Kleidungsstück löschen"""
        adm = WardrobeAdministration()
        item = adm.get_clothing_item_by_id(id)
        if item is not None:
            adm.delete_clothing_item(item)
            return '', 204
        api.abort(404, f"Kleidungsstück {id} nicht gefunden")