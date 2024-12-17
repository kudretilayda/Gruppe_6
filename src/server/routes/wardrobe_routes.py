from flask_restx import Resource
from main import api
from services.wardrobe_service import WardrobeService
from utils.auth import require_auth

@api.route('/api/wardrobe')
class WardrobeResource(Resource):
    @require_auth
    def post(self):
        """Create a new wardrobe"""
        google_id = request.user['sub']
        person = PersonService.get_person_by_google_id(google_id)
        wardrobe_id = WardrobeService.create_wardrobe(person['id'])
        return {'id': wardrobe_id}, 201

    @require_auth
    def get(self):
        """Get current user's wardrobe"""
        google_id = request.user['sub']
        person = PersonService.get_person_by_google_id(google_id)
        wardrobe = WardrobeService.get_wardrobe(person['id'])
        return wardrobe