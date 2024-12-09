# src/server/service/ConstraintService.py

from flask import request
from flask_restx import Namespace, Resource, fields
from server.Administration import WardrobeAdministration
from SecurityDecorator import SecurityDecorator

api = Namespace('constraint', description='Constraint related operations')

# API Models
constraint_model = api.model('Constraint', {
    'id': fields.String(readonly=True),
    'style_id': fields.String(required=True),
    'constraint_type': fields.String(required=True, enum=['binary', 'unary', 'implikation', 'mutex', 'kardinalitaet']),
    'parameters': fields.Raw(required=True),
    'create_time': fields.DateTime(readonly=True)
})

@api.route('/')
class ConstraintListOperations(Resource):
    @SecurityDecorator.check_valid_token
    @api.marshal_list_with(constraint_model)
    def get(self):
        """Liste aller Constraints"""
        adm = WardrobeAdministration()
        return adm.get_all_constraints()

    @SecurityDecorator.check_valid_token
    @api.expect(constraint_model)
    @api.marshal_with(constraint_model, code=201)
    def post(self):
        """Constraint erstellen"""
        adm = WardrobeAdministration()
        data = api.payload
        return adm.create_constraint(
            data['style_id'],
            data['constraint_type'],
            data['parameters']
        ), 201

@api.route('/<id>')
@api.response(404, 'Constraint nicht gefunden')
class ConstraintOperations(Resource):
    @SecurityDecorator.check_valid_token
    @api.marshal_with(constraint_model)
    def get(self, id):
        """Constraint by ID"""
        adm = WardrobeAdministration()
        result = adm.get_constraint_by_id(id)
        if result is not None:
            return result
        api.abort(404, f"Constraint {id} nicht gefunden")

    @SecurityDecorator.check_valid_token
    @api.expect(constraint_model)
    @api.marshal_with(constraint_model)
    def put(self, id):
        """Constraint aktualisieren"""
        adm = WardrobeAdministration()
        constraint = adm.get_constraint_by_id(id)
        if constraint is not None:
            data = api.payload
            constraint.set_parameters(data['parameters'])
            adm.update_constraint(constraint)
            return constraint
        api.abort(404, f"Constraint {id} nicht gefunden")

    @SecurityDecorator.check_valid_token
    def delete(self, id):
        """Constraint löschen"""
        adm = WardrobeAdministration()
        constraint = adm.get_constraint_by_id(id)
        if constraint is not None:
            adm.delete_constraint(constraint)
            return '', 204
        api.abort(404, f"Constraint {id} nicht gefunden")

@api.route('/style/<style_id>')
class StyleConstraintOperations(Resource):
    @SecurityDecorator.check_valid_token
    @api.marshal_list_with(constraint_model)
    def get(self, style_id):
        """Alle Constraints eines Styles"""
        adm = WardrobeAdministration()
        return adm.get_constraints_by_style(style_id)

@api.route('/check')
class ConstraintCheckOperations(Resource):
    @SecurityDecorator.check_valid_token
    def post(self):
        """Prüft ob ein Outfit alle Constraints erfüllt"""
        data = request.json
        adm = WardrobeAdministration()
        validation_result = adm.validate_outfit_constraints(
            data['outfit_id'],
            data.get('items', [])
        )
        return {
            'valid': validation_result['valid'],
            'violations': validation_result.get('violations', [])
        }