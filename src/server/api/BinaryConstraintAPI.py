from flask import request
from flask_restx import Namespace, Resource
from server.services.BinaryConstraintService import BinaryConstraintService

binary_constraint_ns = Namespace('binary-constraints')

@binary_constraint_ns.route('/')
class BinaryConstraintList(Resource):
    @binary_constraint_ns.doc('list_binary_constraints')
    def get(self):
        """List binary constraints by style"""
        style_id = request.args.get('style_id')
        if not style_id:
            return 'style_id parameter is required', 400
            
        service = BinaryConstraintService()
        constraints = service.get_constraints_by_style(style_id)
        return [constraint.to_dict() for constraint in constraints]

    @binary_constraint_ns.doc('create_binary_constraint')
    def post(self):
        """Create a new binary constraint"""
        data = request.get_json()
        service = BinaryConstraintService()
        constraint = service.create_constraint(
            data['style_id'],
            data['reference_object1_id'],
            data['reference_object2_id']
        )
        return constraint.to_dict(), 201

@binary_constraint_ns.route('/<string:id>')
class BinaryConstraintOperations(Resource):
    @binary_constraint_ns.doc('get_binary_constraint')
    def get(self, id):
        """Get a binary constraint by its ID"""
        service = BinaryConstraintService()
        constraint = service.get_constraint(id)
        return constraint.to_dict() if constraint else ('Binary constraint not found', 404)

    @binary_constraint_ns.doc('update_binary_constraint')
    def put(self, id):
        """Update a binary constraint"""
        data = request.get_json()
        service = BinaryConstraintService()
        constraint = service.get_constraint(id)
        if not constraint:
            return 'Binary constraint not found', 404

        if 'reference_object1_id' in data:
            constraint.set_reference_object1_id(data['reference_object1_id'])
        if 'reference_object2_id' in data:
            constraint.set_reference_object2_id(data['reference_object2_id'])
        
        updated_constraint = service.update_constraint(constraint)
        return updated_constraint.to_dict()

    @binary_constraint_ns.doc('delete_binary_constraint')
    def delete(self, id):
        """Delete a binary constraint"""
        service = BinaryConstraintService()
        if service.delete_constraint(id):
            return '', 204
        return 'Binary constraint not found', 404