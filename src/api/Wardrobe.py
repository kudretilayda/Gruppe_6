# src/server/api/wardrobe.py

from flask import request
from flask_restx import Namespace, Resource, fields
from config.security_config import SecurityConfig
from admin.Administration import Administration

wardrobe_namespace = Namespace('wardrobes', description='Wardrobe operations')

# API Models
wardrobe_model = wardrobe_namespace.model('Wardrobe', {
    'id': fields.String(readonly=True),
    'person_id': fields.String(required=True),
    'owner_name': fields.String(required=True),
})

@wardrobe_namespace.route('/')
class WardrobeListOperations(Resource):
    @wardrobe_namespace.marshal_list_with(wardrobe_model)
    @SecurityConfig.check_auth()
    def get(self):
        """Alle Wardrobes auflisten"""
        adm = Administration()
        return adm._wardrobe_mapper.find_all()

    @wardrobe_namespace.expect(wardrobe_model)
    @wardrobe_namespace.marshal_with(wardrobe_model)
    @SecurityConfig.check_auth()
    def post(self):
        """Neue Wardrobe erstellen"""
        adm = Administration()
        wardrobe_data = request.json
        
        return adm.create_wardrobe(
            wardrobe_data['person_id'],
            wardrobe_data['owner_name']
        )

@wardrobe_namespace.route('/person/<string:person_id>')
class WardrobeByPersonOperations(Resource):
    @wardrobe_namespace.marshal_with(wardrobe_model)
    @SecurityConfig.check_auth()
    def get(self, person_id):
        """Wardrobe einer Person finden"""
        adm = Administration()
        return adm.get_wardrobe_by_person(person_id)