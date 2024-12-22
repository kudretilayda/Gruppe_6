from flask import request
from flask_restx import Namespace, Resource
from server.services.WardrobeService import WardrobeService

wardrobe_ns = Namespace('wardrobes')

@wardrobe_ns.route('/')
class WardrobeList(Resource):
    @wardrobe_ns.doc('create_wardrobe')
    def post(self):
        """Create a new wardrobe"""
        data = request.get_json()
        service = WardrobeService()
        wardrobe = service.create_wardrobe(
            data['owner_name'],
            data['person_id']
        )
        return wardrobe.to_dict(), 201

@wardrobe_ns.route('/<string:id>')
class WardrobeOperations(Resource):
    @wardrobe_ns.doc('get_wardrobe')
    def get(self, id):
        """Get a wardrobe by its ID"""
        service = WardrobeService()
        wardrobe = service.get_wardrobe(id)
        return wardrobe.to_dict() if wardrobe else ('Wardrobe not found', 404)

    @wardrobe_ns.doc('update_wardrobe')
    def put(self, id):
        """Update a wardrobe"""
        data = request.get_json()
        service = WardrobeService()
        wardrobe = service.get_wardrobe(id)
        if not wardrobe:
            return 'Wardrobe not found', 404

        wardrobe.set_owner_name(data.get('owner_name', wardrobe.get_owner_name()))
        updated_wardrobe = service.update_wardrobe(wardrobe)
        return updated_wardrobe.to_dict()

    @wardrobe_ns.doc('delete_wardrobe')
    def delete(self, id):
        """Delete a wardrobe"""
        service = WardrobeService()
        if service.delete_wardrobe(id):
            return '', 204
        return 'Wardrobe not found', 404

@wardrobe_ns.route('/person/<string:person_id>')
class WardrobeByPerson(Resource):
    @wardrobe_ns.doc('get_wardrobe_by_person')
    def get(self, person_id):
        """Get a person's wardrobe"""
        service = WardrobeService()
        wardrobe = service.get_wardrobe_by_person(person_id)
        return wardrobe.to_dict() if wardrobe else ('Wardrobe not found', 404)