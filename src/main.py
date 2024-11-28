from server.Admin import Administration
#from SecurityDecorator import secured
from server.bo.User import User

from flask import Flask
from flask_restx import Api, Resource, fields
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/kleiderschrank/*": {"origins": "*"}})

api = Api(app, version='1.0', title='Digitaler Kleiderschrank API',
          description='API für den digitalen Kleiderschrank')

kleiderschrank = api.namespace('kleiderschrank', description='Digitaler Kleiderschrank Funktionen')

# Business Object Basismodell
bo = api.model('BusinessObject', {
    'id': fields.Integer(attribute='_id', description='Der Unique Identifier eines BusinessObject')
})

# User Modell
user = api.inherit('User', bo, {
    'user_id': fields.Integer(attribute='_user_id', description='User ID'),
    'nachname': fields.String(attribute='_nachname', description='Nachname des Users'),
    'vorname': fields.String(attribute='_vorname', description='Vorname des Users'),
    'nickname': fields.String(attribute='_nickname', description='Nickname des Users'),
    'google_id': fields.String(attribute='_google_id', description='Google ID des Users'),
    'email': fields.String(attribute='_email', description='Email des Users')
})

# Constraint Modell
constraint = api.inherit('Constraint', bo, {
    'name': fields.String(attribute='_name', description='Name des Constraints'),
    'beschreibung': fields.String(attribute='_beschreibung', description='Beschreibung des Constraints')
})

# UnaryConstraint Modell
unary_constraint = api.inherit('UnaryConstraint', constraint, {
    'bezugsobjekt': fields.String(attribute='_bezugsobjekt', description='Bezugsobjekt des UnaryConstraints'),
    'bedingung': fields.String(attribute='_bedingung', description='Bedingung des UnaryConstraints')
})

# BinaryConstraint Modell
binary_constraint = api.inherit('BinaryConstraint', constraint, {
    'obj1': fields.String(attribute='_obj1', description='Bezugsobjekt 1'),
    'obj2': fields.String(attribute='_obj2', description='Bezugsobjekt 2'),
    'bedingung': fields.String(attribute='_bedingung', description='Bedingung des BinaryConstraints')
})

# CardinalityConstraint Modell
cardinality_constraint = api.inherit('CardinalityConstraint', constraint, {
    'min_count': fields.Integer(attribute='_min_count', description='Minimale Kardinalität'),
    'max_count': fields.Integer(attribute='_max_count', description='Maximale Kardinalität'),
    'obj1_attribute': fields.String(attribute='_obj1_attribute', description='Attribut des ersten Objekts'),
    'obj1_value': fields.String(attribute='_obj1_value', description='Wert des Attributs des ersten Objekts'),
    'obj2_attribute': fields.String(attribute='_obj2_attribute', description='Attribut des zweiten Objekts'),
    'obj2_value': fields.String(attribute='_obj2_value', description='Wert des Attributs des zweiten Objekts')
})

# ImplicationConstraint Modell
implication_constraint = api.inherit('ImplicationConstraint', constraint, {
    'condition_attribute': fields.String(attribute='_condition_attribute', description='Bedingungsattribut'),
    'condition_value': fields.String(attribute='_condition_value', description='Bedingungswert'),
    'implication_attribute': fields.String(attribute='_implication_attribute', description='Implikationsattribut'),
    'implication_value': fields.String(attribute='_implication_value', description='Implikationswert')
})

# MutexConstraint Modell
mutex_constraint = api.inherit('MutexConstraint', constraint, {
    'obj1_attribute': fields.String(attribute='_obj1_attribute', description='Attribut des ersten Objekts'),
    'obj1_value': fields.String(attribute='_obj1_value', description='Wert des Attributs des ersten Objekts'),
    'obj2_attribute': fields.String(attribute='_obj2_attribute', description='Attribut des zweiten Objekts'),
    'obj2_value': fields.String(attribute='_obj2_value', description='Wert des Attributs des zweiten Objekts')
})

@kleiderschrank.route('/user')
class UserListOperations(Resource):
    @kleiderschrank.marshal_list_with(user)
    def get(self):
        """Alle User auslesen"""
        return []  # Zunächst leere Liste zurückgeben
    
@kleiderschrank.route('/constraint')
class ConstraintListOperations(Resource):
    @kleiderschrank.marshal_list_with(constraint)
    def get(self):
        """Alle Constraints auslesen"""
        return []  # Zunächst leere Liste zurückgeben
    
@kleiderschrank.route('/unary-constraint')
class UnaryConstraintListOperations(Resource):
    @kleiderschrank.marshal_list_with(unary_constraint)
    def get(self):
        """Alle UnaryConstraints auslesen"""
        return []

@kleiderschrank.route('/binary-constraint')
class BinaryConstraintListOperations(Resource):
    @kleiderschrank.marshal_list_with(binary_constraint)
    def get(self):
        """Alle BinaryConstraints auslesen"""
        return []

@kleiderschrank.route('/cardinality-constraint')
class CardinalityConstraintListOperations(Resource):
    @kleiderschrank.marshal_list_with(cardinality_constraint)
    def get(self):
        """Alle CardinalityConstraints auslesen"""
        return []

@kleiderschrank.route('/implication-constraint')
class ImplicationConstraintListOperations(Resource):
    @kleiderschrank.marshal_list_with(implication_constraint)
    def get(self):
        """Alle ImplicationConstraints auslesen"""
        return []

@kleiderschrank.route('/mutex-constraint')
class MutexConstraintListOperations(Resource):
    @kleiderschrank.marshal_list_with(mutex_constraint)
    def get(self):
        """Alle MutexConstraints auslesen"""
        return []

if __name__ == '__main__':
    app.run(debug=True)