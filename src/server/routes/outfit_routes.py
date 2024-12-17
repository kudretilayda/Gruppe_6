from flask import request
from flask_restx import Resource, fields
from main import api
from services.style_service import StyleService
from utils.auth import require_auth

# API Models for request/response validation
style_model = api.model('Style', {
    'id': fields.Integer(readonly=True),
    'features': fields.String(required=True),
})

constraint_model = api.model('Constraint', {
    'type': fields.String(required=True, enum=['unary', 'binary', 'mutex', 'implication', 'cardinality']),
    'reference_object1': fields.Integer(required=False),
    'reference_object2': fields.Integer(required=False),
    'min_count': fields.Integer(required=False),
    'max_count': fields.Integer(required=False)
})

style_creation_model = api.model('StyleCreation', {
    'features': fields.String(required=True),
    'constraints': fields.List(fields.Nested(constraint_model))
})

@api.route('/api/styles')
class StyleListResource(Resource):
    @require_auth
    @api.marshal_list_with(style_model)
    def get(self):
        """Get all styles"""
        return StyleService.get_all_styles()

    @require_auth
    @api.expect(style_creation_model)
    @api.marshal_with(style_model)
    def post(self):
        """Create a new style with constraints"""
        data = request.json
        return StyleService.create_style(data), 201

@api.route('/api/styles/<int:style_id>')
class StyleResource(Resource):
    @require_auth
    @api.marshal_with(style_model)
    def get(self, style_id):
        """Get a specific style by ID"""
        style = StyleService.get_style_by_id(style_id)
        if style:
            return style
        api.abort(404, f"Style {style_id} not found")

    @require_auth
    @api.expect(style_model)
    @api.marshal_with(style_model)
    def put(self, style_id):
        """Update a specific style"""
        data = request.json
        style = StyleService.update_style(style_id, data)
        if style:
            return style
        api.abort(404, f"Style {style_id} not found")

    @require_auth
    def delete(self, style_id):
        """Delete a specific style"""
        success = StyleService.delete_style(style_id)
        if success:
            return {'message': 'Style deleted successfully'}, 200
        api.abort(404, f"Style {style_id} not found")