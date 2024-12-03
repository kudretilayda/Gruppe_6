# src/server/api/outfit.py

from flask import request
from flask_restx import Namespace, Resource, fields
from config.security_config import SecurityConfig
from admin.Administration import Administration

outfit_namespace = Namespace('outfits', description='Outfit operations')

# API Models
outfit_model = outfit_namespace.model('Outfit', {
    'id': fields.String(readonly=True),
    'name': fields.String(required=True),
    'style_id': fields.String(required=True),
    'created_by': fields.String(required=True),
    'items': fields.List(fields.String)
})

outfit_check_result = outfit_namespace.model('OutfitCheckResult', {
    'valid': fields.Boolean,
    'violations': fields.List(fields.String)
})

@outfit_namespace.route('/')
class OutfitListOperations(Resource):
    @outfit_namespace.marshal_list_with(outfit_model)
    @SecurityConfig.check_auth()
    def get(self):
        """Alle Outfits auflisten"""
        adm = Administration()
        return adm._outfit_mapper.find_all()

    @outfit_namespace.expect(outfit_model)
    @outfit_namespace.marshal_with(outfit_model)
    @SecurityConfig.check_auth()
    def post(self):
        """Neues Outfit erstellen"""
        adm = Administration()
        outfit_data = request.json
        
        outfit = adm.create_outfit(
            outfit_data['name'],
            outfit_data['style_id'],
            outfit_data['created_by']
        )
        
        # Kleidungsstücke hinzufügen, falls vorhanden
        if 'items' in outfit_data:
            for item_id in outfit_data['items']:
                adm.add_item_to_outfit(outfit.get_id(), item_id)
        
        return outfit

@outfit_namespace.route('/<string:outfit_id>/check')
class OutfitCheckOperations(Resource):
    @outfit_namespace.marshal_with(outfit_check_result)
    @SecurityConfig.check_auth()
    def get(self, outfit_id):
        """Outfit auf Constraint-Verletzungen prüfen"""
        adm = Administration()
        valid, violations = adm.check_outfit_constraints(outfit_id)
        return {'valid': valid, 'violations': violations}

@outfit_namespace.route('/<string:outfit_id>/items/<string:item_id>')
class OutfitItemOperations(Resource):
    @SecurityConfig.check_auth()
    def post(self, outfit_id, item_id):
        """Kleidungsstück zu Outfit hinzufügen"""
        adm = Administration()
        adm.add_item_to_outfit(outfit_id, item_id)
        return '', 201

    @SecurityConfig.check_auth()
    def delete(self, outfit_id, item_id):
        """Kleidungsstück aus Outfit entfernen"""
        adm = Administration()
        adm._outfit_mapper.remove_item_from_outfit(outfit_id, item_id)
        return '', 204