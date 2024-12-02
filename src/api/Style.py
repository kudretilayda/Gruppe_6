# src/server/api/style.py

from flask import request
from flask_restx import Namespace, Resource, fields
from config.security_config import SecurityConfig
from admin.Admin import Administration

style_namespace = Namespace('styles', description='Style operations')

# API Models
constraint_model = style_namespace.model('Constraint', {
    'constraint_type': fields.String(required=True, enum=['binary', 'unary', 'implikation', 'mutex', 'kardinalitaet']),
    'reference_object1_id': fields.String(required=False),
    'reference_object2_id': fields.String(required=False),
    'min_value': fields.Integer(required=False),
    'max_value': fields.Integer(required=False)
})

style_model = style_namespace.model('Style', {
    'id': fields.String(readonly=True),
    'name': fields.String(required=True),
    'description': fields.String(required=True),
    'created_by': fields.String(required=True),
    'constraints': fields.List(fields.Nested(constraint_model))
})

@style_namespace.route('/')
class StyleListOperations(Resource):
    @style_namespace.marshal_list_with(style_model)
    @SecurityConfig.check_auth()
    def get(self):
        """Alle Styles auflisten"""
        adm = Administration()
        return adm._style_mapper.find_all()

    @style_namespace.expect(style_model)
    @style_namespace.marshal_with(style_model)
    @SecurityConfig.check_auth()
    def post(self):
        """Neuen Style erstellen"""
        adm = Administration()
        style_data = request.json
        
        style = adm.create_style(
            style_data['name'],
            style_data['description'],
            style_data['created_by']
        )
        
        # Constraints hinzufügen, falls vorhanden
        if 'constraints' in style_data:
            for constraint_data in style_data['constraints']:
                adm.add_constraint_to_style(
                    style.get_id(),
                    constraint_data['constraint_type'],
                    constraint_data.get('reference_object1_id'),
                    constraint_data.get('reference_object2_id'),
                    constraint_data.get('min_value'),
                    constraint_data.get('max_value')
                )
        
        return style

@style_namespace.route('/<string:style_id>/constraints')
class StyleConstraintOperations(Resource):
    @style_namespace.expect(constraint_model)
    @SecurityConfig.check_auth()
    def post(self, style_id):
        """Constraint zu Style hinzufügen"""
        adm = Administration()
        constraint_data = request.json
        
        constraint = adm.add_constraint_to_style(
            style_id,
            constraint_data['constraint_type'],
            constraint_data.get('reference_object1_id'),
            constraint_data.get('reference_object2_id'),
            constraint_data.get('min_value'),
            constraint_data.get('max_value')
        )
        return constraint.to_dict(), 201