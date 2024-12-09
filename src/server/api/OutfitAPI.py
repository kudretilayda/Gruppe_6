# server/api/OutfitAPI.py
from flask import request
from flask_restx import Namespace, Resource
from server.services.OutfitService import OutfitService

outfit_ns = Namespace('outfits')

@outfit_ns.route('/')
class OutfitList(Resource):
    @outfit_ns.doc('list_outfits')
    def get(self):
        """List all outfits or filter by person"""
        person_id = request.args.get('person_id')
        service = OutfitService()
        if person_id:
            outfits = service.get_outfits_by_person(person_id)
        else:
            outfits = service.get_all_outfits()
        return [outfit.to_dict() for outfit in outfits]

    @outfit_ns.doc('create_outfit')
    def post(self):
        """Create a new outfit"""
        data = request.get_json()
        service = OutfitService()
        outfit = service.create_outfit(
            data['outfit_name'],
            data['style_id'],
            data['created_by'],
            data.get('items', [])
        )
        return outfit.to_dict(), 201

@outfit_ns.route('/<string:id>')
class OutfitOperations(Resource):
    @outfit_ns.doc('get_outfit')
    def get(self, id):
        """Get an outfit by its ID"""
        service = OutfitService()
        outfit = service.get_outfit(id)
        return outfit.to_dict() if outfit else ('Outfit not found', 404)

    @outfit_ns.doc('update_outfit')
    def put(self, id):
        """Update an outfit"""
        data = request.get_json()
        service = OutfitService()
        outfit = service.get_outfit(id)
        if not outfit:
            return 'Outfit not found', 404

        outfit.set_outfit_name(data.get('outfit_name', outfit.get_outfit_name()))
        outfit.set_style_id(data.get('style_id', outfit.get_style_id()))
        outfit.set_items(data.get('items', outfit.get_items()))
        
        updated_outfit = service.update_outfit(outfit)
        return updated_outfit.to_dict()

    @outfit_ns.doc('delete_outfit')
    def delete(self, id):
        """Delete an outfit"""
        service = OutfitService()
        if service.delete_outfit(id):
            return '', 204
        return 'Outfit not found', 404