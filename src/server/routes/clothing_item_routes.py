from flask import request
from flask_restx import Resource, fields
from main import api
from services.clothing_item_service import ClothingItemService
from utils.auth import require_auth

clothing_item_model = api.model('ClothingItem', {
    'id': fields.Integer(readonly=True),
    'type_id': fields.Integer(required=True)
})

@api.route('/api/clothing-items')
class ClothingItemListResource(Resource):
    @require_auth
    @api.marshal_list_with(clothing_item_model)
    def get(self):
        """Get all clothing items"""
        return ClothingItemService.get_all_items()

    @require_auth
    @api.expect(clothing_item_model)
    @api.marshal_with(clothing_item_model)
    def post(self):
        """Create a new clothing item"""
        return ClothingItemService.create_item(request.json), 201

@api.route('/api/clothing-items/<int:item_id>')
class ClothingItemResource(Resource):
    @require_auth
    @api.marshal_with(clothing_item_model)
    def get(self, item_id):
        """Get a specific clothing item"""
        item = ClothingItemService.get_item_by_id(item_id)
        if item:
            return item
        api.abort(404, f"Clothing item {item_id} not found")

    @require_auth
    def delete(self, item_id):
        """Delete a clothing item"""
        if ClothingItemService.delete_item(item_id):
            return {'message': 'Clothing item deleted'}, 200
        api.abort(404, f"Clothing item {item_id} not found")