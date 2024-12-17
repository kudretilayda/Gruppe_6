from flask import request # type: ignore
from flask_restx import Resource, fields # type: ignore
from main import api
from utils.auth import require_auth

# API Models
outfit_item = api.model('OutfitItem', {
    'item_id': fields.Integer(required=True),
})

outfit_create = api.model('OutfitCreate', {
    'name': fields.String(required=True),
    'style_id': fields.Integer(required=True),
    'items': fields.List(fields.Nested(outfit_item), required=True)
})

outfit_proposal_request = api.model('OutfitProposalRequest', {
    'style_id': fields.Integer(required=True),
    'wardrobe_id': fields.Integer(required=True),
    'preferred_items': fields.List(fields.Integer, required=False)
})

outfit_completion_request = api.model('OutfitCompletionRequest', {
    'partial_outfit_items': fields.List(fields.Integer, required=True),
    'style_id': fields.Integer(required=True),
    'wardrobe_id': fields.Integer(required=True)
})

@api.route('/api/outfits')
class OutfitResource(Resource):
    @require_auth
    @api.expect(outfit_create)
    def post(self):
        """Erstellt ein neues Outfit"""
        try:
            data = request.json
            outfit_service = outfit_service()
            
            outfit = outfit_service.create_outfit(
                name=data['name'],
                style_id=data['style_id'],
                items=[item['item_id'] for item in data['items']],
                created_by=request.user['id']  # From auth middleware
            )
            
            return {'id': outfit.get_id()}, 201
        except ValueError as e:
            return {'message': str(e)}, 400
        except Exception as e:
            return {'message': 'Internal server error'}, 500

@api.route('/api/outfits/propose')
class OutfitProposalResource(Resource):
    @require_auth
    @api.expect(outfit_proposal_request)
    def post(self):
        """Generiert Outfit-Vorschläge"""
        try:
            data = request.json
            outfit_service = outfit_service()
            
            proposals = outfit_service.generate_outfit_proposals(
                style_id=data['style_id'],
                wardrobe_id=data['wardrobe_id'],
                preferred_items=data.get('preferred_items')
            )
            
            return proposals, 200
        except Exception as e:
            return {'message': str(e)}, 500

@api.route('/api/outfits/complete')
class OutfitCompletionResource(Resource):
    @require_auth
    @api.expect(outfit_completion_request)
    def post(self):
        """Schlägt Vervollständigungen für ein teilweise gewähltes Outfit vor"""
        try:
            data = request.json
            outfit_service = outfit_service()
            
            suggestions = outfit_service.complete_partial_outfit(
                partial_outfit_items=data['partial_outfit_items'],
                style_id=data['style_id'],
                wardrobe_id=data['wardrobe_id']
            )
            
            return suggestions, 200
        except Exception as e:
            return {'message': str(e)}, 500

@api.route('/api/outfits/<int:outfit_id>')
class OutfitDetailResource(Resource):
    @require_auth
    def get(self, outfit_id):
        """Holt ein spezifisches Outfit"""
        try:
            outfit_service = outfit_service()
            outfit = outfit_service.get_outfit_by_id(outfit_id)
            
            if not outfit:
                return {'message': 'Outfit not found'}, 404
                
            return {
                'id': outfit.get_id(),
                'name': outfit.get_outfit_name(),
                'style_id': outfit.get_style_id(),
                'items': outfit.get_items()
            }, 200
        except Exception as e:
            return {'message': str(e)}, 500

    @require_auth
    def delete(self, outfit_id):
        """Löscht ein Outfit"""
        try:
            outfit_service = outfit_service()
            success = outfit_service.delete_outfit(outfit_id)
            
            if success:
                return {'message': 'Outfit deleted'}, 200
            return {'message': 'Outfit not found'}, 404
        except Exception as e:
            return {'message': str(e)}, 500