from flask_restx import Resource, fields
from main import api
from services.person_service import PersonService
from utils.auth import require_auth

person_model = api.model('Person', {
    'nachname': fields.String(required=True),
    'vorname': fields.String(required=True),
    'nickname': fields.String(required=True),
    'google_id': fields.String(required=True)
})

@api.route('/api/person')
class PersonResource(Resource):
    @api.expect(person_model)
    @require_auth
    def post(self):
        """Create a new person"""
        data = api.payload
        person_id = PersonService.create_person(data)
        return {'id': person_id}, 201

    @require_auth
    def get(self):
        """Get current person details"""
        google_id = request.user['sub']
        person = PersonService.get_person_by_google_id(google_id)
        return person