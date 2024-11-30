from flask import Flask
from flask_restx import Api, Resource, fields
from flask_cors import CORS

from server.bo.Constraint import Constraint
from server.bo.BinaryConstraint import BinaryConstraint
from server.bo.CardinalityConstraint import CardinalityConstraint
from server.bo.UnaryConstraint import UnaryConstraint
from server.bo.ImplicationConstraint import ImplicationConstraint
from server.bo.MutexConstraint import MutexConstraint


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
    'object1': fields.String(attribute='_object1', description='Bezugsobjekt 1'),
    'object2': fields.String(attribute='_object2', description='Bezugsobjekt 2'),
    'bedingung': fields.String(attribute='_bedingung', description='Bedingung des BinaryConstraints')
})

# CardinalityConstraint Modell
cardinality_constraint = api.inherit('CardinalityConstraint', constraint, {
    'min_count': fields.Integer(attribute='_min_count', description='Minimale Kardinalität'),
    'max_count': fields.Integer(attribute='_max_count', description='Maximale Kardinalität'),
    'object1': fields.String(attribute='_object1', description='Erstes Objekt'),
    'object2': fields.String(attribute='_object2', description='Zweites Objekt')
})

# ImplicationConstraint Modell
implication_constraint = api.inherit('ImplicationConstraint', constraint, {
    'condition': fields.String(attribute='_condition', description='Bedingung'),
    'implication': fields.String(attribute='_implication', description='Implikation')
})

# MutexConstraint Modell
mutex_constraint = api.inherit('MutexConstraint', constraint, {
    'object1': fields.String(attribute='_object1', description='Erstes Objekt'),
    'object2': fields.String(attribute='_object2', description='Zweites Objekt')
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

if __name__ == '__main__':
    app.run(debug=True)