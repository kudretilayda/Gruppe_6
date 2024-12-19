from flask import request
from flask_restx import Namespace, Resource
from server.services.UnaryConstraintService import UnaryConstraintService

unary_constraint_ns = Namespace('unary-constraints')

@unary_constraint_ns.route('/')
class UnaryConstraintList(Resource):
    @unary_constraint_ns.doc('list_unary_constraints')
    def get(self):
        """List unary constraints by style"""
        style_id = request.args.get('style_id')
        if not style_id:
            return 'style_id parameter is required', 400
            
        service = UnaryConstraintService()
        constraints = service.get_constraints_by_style(style_id)
        return [constraint.to_dict() for constraint in constraints]

    @unary_constraint_ns.doc('create_unary_constraint')
    def post(self):
        """Create a new unary constraint"""
        data = request.get_json()
        service = UnaryConstraintService()
        constraint = service.create_constraint(
            data['style_id'],
            data['reference_object_id']
        )
        return constraint.to_dict(), 201

@unary_constraint_ns.route('/<string:id>')
class UnaryConstraintOperations(Resource):
    @unary_constraint_ns.doc('get_unary_constraint')
    def get(self, id):
        """Get a unary constraint by its ID"""
        service = UnaryConstraintService()
        constraint = service.get_constraint(id)
        return constraint.to_dict() if constraint else ('Unary constraint not found', 404)

    @unary_constraint_ns.doc('update_unary_constraint')
    def put(self, id):
        """Update a unary constraint"""
        data = request.get_json()
        service = UnaryConstraintService()
        constraint = service.get_constraint(id)
        if not constraint:
            return 'Unary constraint not found', 404

        if 'reference_object_id' in data:
            constraint.set_reference_object_id(data['reference_object_id'])
        
        updated_constraint = service.update_constraint(constraint)
        return updated_constraint.to_dict()

    @unary_constraint_ns.doc('delete_unary_constraint')
    def delete(self, id):
        """Delete a unary constraint"""
        service = UnaryConstraintService()
        if service.delete_constraint(id):
            return '', 204
        return 'Unary constraint not found', 404