# src/server/api/clothing.py

from flask import request
from flask_restx import Namespace, Resource, fields
from config.security_config import SecurityConfig
from admin.Admin import Administration

clothing_namespace = Namespace('clothing', description='Clothing operations')

# API Models
clothing_type_model = clothing_namespace.model('ClothingType', {
    'id': fields.String(readonly=True),
    'name': fields.String(required=True),
    'description': fields.String(required=True),
    'category': fields.String(required=True)
})

clothing_item_model = clothing_namespace.model('ClothingItem', {
    'id': fields.String(readonly=True),
    'wardrobe_id': fields.String(required=True),
    'type_id': fields.String(required=True),
    'product_name': fields.String(required=True),
    'color': fields.String(required=False),
    'brand': fields.String(required=False),
    'season': fields.String(required=False)
})

@clothing_namespace.route('/types')
class ClothingTypeListOperations(Resource):
    @clothing_namespace.marshal_list_with(clothing_type_model)
    @SecurityConfig.check_auth()
    def get(self):
        """Alle Kleidungstypen auflisten"""
        adm = Administration()
        return adm._clothing_type_mapper.find_all()

    @clothing_namespace.expect(clothing_type_model)
    @clothing_namespace.marshal_with(clothing_type_model)
    @SecurityConfig.check_auth()
    def post(self):
        """Neuen Kleidungstyp erstellen"""
        adm = Administration()
        type_data = request.json
        
        clothing_type = adm.create_clothing_type(
            type_data['name'],
            type_data['description'],
            type_data['category']
        )
        return clothing_type

@clothing_namespace.route('/types/category/<string:category>')
class ClothingTypeByCategoryOperations(Resource):
    @clothing_namespace.marshal_list_with(clothing_type_model)
    @SecurityConfig.check_auth()
    def get(self, category):
        """Kleidungstypen nach Kategorie auflisten"""
        adm = Administration()
        return adm._clothing_type_mapper.find_by_category(category)

@clothing_namespace.route('/items')
class ClothingItemListOperations(Resource):
    @clothing_namespace.marshal_list_with(clothing_item_model)
    @SecurityConfig.check_auth()
    def get(self):
        """Alle Kleidungsstücke auflisten"""
        adm = Administration()
        return adm._clothing_item_mapper.find_all()

    @clothing_namespace.expect(clothing_item_model)
    @clothing_namespace.marshal_with(clothing_item_model)
    @SecurityConfig.check_auth()
    def post(self):
        """Neues Kleidungsstück erstellen"""
        adm = Administration()
        item_data = request.json
        
        clothing_item = adm.create_clothing_item(
            item_data['wardrobe_id'],
            item_data['type_id'],
            item_data['product_name'],
            item_data.get('color'),
            item_data.get('brand'),
            item_data.get('season')
        )
        return clothing_item

@clothing_namespace.route('/items/wardrobe/<string:wardrobe_id>')
class ClothingItemByWardrobeOperations(Resource):
    @clothing_namespace.marshal_list_with(clothing_item_model)
    @SecurityConfig.check_auth()
    def get(self, wardrobe_id):
        """Kleidungsstücke nach Wardrobe auflisten"""
        adm = Administration()
        return adm._clothing_item_mapper.find_by_wardrobe(wardrobe_id)