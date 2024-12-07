from flask import request
from flask_restx import Namespace, Resource
from server.services.ClothingItemsService import ClothingItemService

clothing_item_ns = Namespace('clothing_items')

@clothing_item_ns.route('/')
class ClothingItemList(Resource):
    @clothing_item_ns.doc('list_clothing_items')
    def get(self):
        """List all clothing items of a wardrobe"""
        wardrobe_id = request.args.get('wardrobe_id')
        service = ClothingItemService()
        if wardrobe_id:
            return [item.to_dict() for item in service.get_items_by_wardrobe(wardrobe_id)]
        return [], 200

    @clothing_item_ns.doc('create_clothing_item')
    def post(self):
        """Create a new clothing item"""
        data = request.get_json()
        service = ClothingItemService()
        item = service.create_clothing_item(
            data['product_name'],
            data['wardrobe_id'],
            data['clothing_type_id'],
            data.get('color'),
            data.get('brand'),
            data.get('season')
        )
        return item.to_dict(), 201

@clothing_item_ns.route('/<string:id>')
class ClothingItemOperations(Resource):
    @clothing_item_ns.doc('get_clothing_item')
    def get(self, id):
        """Get a clothing item by its ID"""
        service = ClothingItemService()
        item = service.get_clothing_item(id)
        return item.to_dict() if item else ('Clothing item not found', 404)

    @clothing_item_ns.doc('update_clothing_item')
    def put(self, id):
        """Update a clothing item"""
        data = request.get_json()
        service = ClothingItemService()
        item = service.get_clothing_item(id)
        if not item:
            return 'Clothing item not found', 404

        item.set_product_name(data.get('product_name', item.get_product_name()))
        item.set_color(data.get('color', item.get_color()))
        item.set_brand(data.get('brand', item.get_brand()))
        item.set_season(data.get('season', item.get_season()))

        updated_item = service.update_clothing_item(item)
        return updated_item.to_dict()

    @clothing_item_ns.doc('delete_clothing_item')
    def delete(self, id):
        """Delete a clothing item"""
        service = ClothingItemService()
        if service.delete_clothing_item(id):
            return '', 204
        return 'Clothing item not found', 404