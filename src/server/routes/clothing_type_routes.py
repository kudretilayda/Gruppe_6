from flask import request # type: ignore
from flask_restx import Resource, fields # type: ignore
from main import api
from services.clothing_type_service import ClothingTypeService
from utils.auth import require_auth

clothing_type_model = api.model('ClothingType', {
    'id': fields.Integer(readonly=True),
    'name': fields.String(required=True),
    'usage': fields.String(required=True)
})

@api.route('/api/clothing-types')
class ClothingTypeListResource(Resource):
    @require_auth
    @api.marshal_list_with(clothing_type_model)
    def get(self):
        """Get all clothing types"""
        return ClothingTypeService.get_all_types()

    @require_auth
    @api.expect(clothing_type_model)
    @api.marshal_with(clothing_type_model)
    def post(self):
        """Create a new clothing type"""
        return ClothingTypeService.create_type(request.json), 201

@api.route('/api/clothing-types/<int:type_id>')
class ClothingTypeResource(Resource):
    @require_auth
    @api.marshal_with(clothing_type_model)
    def get(self, type_id):
        """Get a specific clothing type"""
        type = ClothingTypeService.get_type_by_id(type_id)
        if type:
            return type
        api.abort(404, f"Clothing type {type_id} not found")

    @require_auth
    def delete(self, type_id):
        """Delete a clothing type"""
        if ClothingTypeService.delete_type(type_id):
            return {'message': 'Clothing type deleted'}, 200
        api.abort(404, f"Clothing type {type_id} not found")