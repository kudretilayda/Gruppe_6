from flask import request
from flask_restx import Namespace, Resource
from src.server.services.ImplicationConstraintService import ImplikationConstraintService

implication_constraint_ns = Namespace('implication-constraints')

@implication_constraint_ns.route('/')
class ImplikationConstraintList(Resource):
    @implication_constraint_ns.doc('list_implication_constraints')
    def get(self):
        """List implication constraints by style"""
        style_id = request.args.get('style_id')
        if not style_id:
            return 'style_id parameter is required', 400
            
        service = ImplikationConstraintService()
        constraints = service.get_constraints_by_style(style_id)
        return [constraint.to_dict() for constraint in constraints]

    @implication_constraint_ns.doc('create_implication_constraint')
    def post(self):
        """Create a new implication constraint"""
        data = request.get_json()
        service = ImplikationConstraintService()
        constraint = service.create_constraint(
            data['style_id'],
            data['if_type_id'],
            data['then_type_id']
        )
        return constraint.to_dict(), 201