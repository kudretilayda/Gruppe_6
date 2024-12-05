from flask import Flask
from flask_restx import Api, Resource, fields
from flask_cors import CORS

from server.Admin import Admin
from server.bo.BinaryConstraint import BinaryConstraint
from server.bo.BusinessObject import BusinessObject
from server.bo.CardinalityConstraint import CardinalityConstraint
from server.bo.Constraint import Constraint
from server.bo.ImplicationConstraint import ImplicationConstraint
from server.bo.Kleiderschrank import Kleiderschrank
from server.bo.Kleidungsstueck import Kleidungsstueck
from server.bo.Kleidungstyp import Kleidungstyp
from server.bo.MutexConstraint import MutexConstraint
from server.bo.Outfit import Outfit
from server.bo.Style import Style
from server.bo.UnaryConstraint import UnaryConstraint
from server.bo.User import User


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



"""
Basisklassen und Modelle
"""

@matchmaker.route('/user')
@matchmaker.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class UserListOperations(Resource):
    """Auslesen aller User-Objekte."""
    
    @matchmaker.marshal_list_with(user)
    @secured
    def get(self):
        adm = Administration()
        users = adm.get_all_users()
        return users

    @matchmaker.marshal_with(user, code=200)
    @matchmaker.expect(user)
    @secured
    def post(self):
        """Anlegen eines neuen User-Objekts."""
        adm = Administration()
        pluser = User.from_dict(api.payload)
        
        if pluser is not None:
            new_user = adm.create_user(
                google_id=pluser.get_google_id(),
                email=pluser.get_email(),
                nachname=pluser.get_nachname(),
                vorname=pluser.get_vorname(),
                koerpergroesse=pluser.get_koerpergroesse(),
                genre=pluser.get_genre(),
                geburtsdatum=pluser.get_geburtsdatum(),
                religion=pluser.get_religion(),
                is_raucher=pluser.get_is_raucher(),
                haarfarbe=pluser.get_haarfarbe()
            )
            return new_user, 200
        else:
            return '', 500

@matchmaker.route('/user/<id>')
@matchmaker.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class UserOperations(Resource):
    @matchmaker.marshal_with(user)
    @secured
    def get(self, id):
        """Auslesen eines bestimmten User-Objekts anhand der ID."""
        adm = Administration()
        single_user = adm.get_user_by_id(id)
        return single_user

    @matchmaker.marshal_with(user)
    @matchmaker.expect(user, validate=True)
    @secured
    def put(self, id):
        """Update eines bestimmten User-Objekts anhand der ID."""
        adm = Administration()
        user = User.from_dict(api.payload)
        
        if user is not None:
            user.set_id(id)
            updated_user = adm.change_user(user)
            return updated_user, 200
        else:
            return '', 500

    @secured
    def delete(self, id):
        """Löschen eines bestimmten User-Objekts anhand der ID."""
        adm = Administration()
        user_to_delete = adm.get_user_by_id(id)
        adm.delete_user(user_to_delete)
        return '', 200

@matchmaker.route('/user-by-google-id/<string:google_id>')
@matchmaker.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class UserGoogleOperations(Resource):
    @matchmaker.marshal_with(user)
    @secured
    def get(self, google_id):
        """Auslesen eines bestimmten User-Objekts anhand der Google-ID."""
        adm = Administration()
        user = adm.get_user_by_google_id(google_id)
        return user


"""
Constraint Methoden
"""

@kleiderschrank.route('/constraint')
@kleiderschrank.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class ConstraintListOperations(Resource):
    """Auslesen von Constraint-Objekten."""

    @kleiderschrank.marshal_list_with(constraint)
    @secured
    def get(self):
        """Alle Constraints auslesen"""
        adm = Admin()
        data = adm.get_all_constraints()
        return data

@kleiderschrank.route('/constraint/<int:id>')
@kleiderschrank.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class ConstraintOperations(Resource):
    @kleiderschrank.marshal_with(constraint)
    @secured
    def get(self, id):
        """Ein bestimmtes Constraint-Objekt auslesen"""
        adm = Admin()
        data = adm.get_constraint_by_id(id)
        return data

@kleiderschrank.route('/constraint-by-user/<int:user_id>')
@kleiderschrank.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class ConstraintUserOperations(Resource):
    @kleiderschrank.marshal_list_with(constraint)
    @secured
    def get(self, user_id):
        """Alle Constraints eines Users auslesen"""
        adm = Admin()
        data = adm.get_constraints_by_user_id(user_id)
        return data

"""
Unary Constraint Methoden
"""

@kleiderschrank.route('/unary-constraint')
@kleiderschrank.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class UnaryConstraintListOperations(Resource):
    """Auslesen und Erstellen von UnaryConstraint-Objekten."""

    @kleiderschrank.marshal_list_with(unary_constraint)
    @secured
    def get(self):
        """Alle UnaryConstraints auslesen"""
        adm = Admin()
        data = adm.get_all_unary_constraints()
        return data

    @kleiderschrank.marshal_with(unary_constraint, code=200)
    @kleiderschrank.expect(unary_constraint)
    @secured
    def post(self):
        """Neues UnaryConstraint anlegen"""
        adm = Admin()
        pl_constraint = UnaryConstraint.from_dict(api.payload)
        
        if pl_constraint is not None:
            constraint = adm.create_unary_constraint(
                bezugsobjekt=pl_constraint.get_bezugsobjekt(),
                bedingung=pl_constraint.get_bedingung()
            )
            return constraint, 200
        else:
            return '', 500

@kleiderschrank.route('/unary-constraint/<int:id>')
@kleiderschrank.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class UnaryConstraintOperations(Resource):
    @kleiderschrank.marshal_with(unary_constraint)
    @secured
    def get(self, id):
        """Einzelnes UnaryConstraint auslesen"""
        adm = Admin()
        data = adm.get_unary_constraint_by_id(id)
        return data

    @kleiderschrank.marshal_with(unary_constraint)
    @kleiderschrank.expect(unary_constraint, validate=True)
    @secured
    def put(self, id):
        """UnaryConstraint aktualisieren"""
        adm = Admin()
        constraint = UnaryConstraint.from_dict(api.payload)
        
        if constraint is not None:
            constraint.set_id(id)
            data = adm.update_unary_constraint(constraint)
            return data, 200
        else:
            return '', 500

    @secured
    def delete(self, id):
        """UnaryConstraint löschen"""
        adm = Admin()
        constraint = adm.get_unary_constraint_by_id(id)
        adm.delete_unary_constraint(constraint)
        return '', 200

@kleiderschrank.route('/unary-constraint-by-user/<int:user_id>')
@kleiderschrank.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class UnaryConstraintUserOperations(Resource):
    @kleiderschrank.marshal_list_with(unary_constraint)
    @secured
    def get(self, user_id):
        """Alle UnaryConstraints eines Users auslesen"""
        adm = Admin()
        data = adm.get_unary_constraints_by_user_id(user_id)
        return data

"""
UnaryConstraint Kleidungsstück Operationen
"""
@kleiderschrank.route('/unary-constraint/<int:constraint_id>/kleidungsstueck/<int:kleidungsstueck_id>')
@kleiderschrank.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class UnaryConstraintKleidungsstueckeManagementOperations(Resource):
    @kleiderschrank.marshal_list_with(kleidungsstueck)
    @secured
    def get(self, constraint_id):
        """Alle Kleidungsstücke eines UnaryConstraints auslesen"""
        adm = Admin()
        data = adm.get_kleidungsstuecke_by_unary_constraint_id(constraint_id)
        return data

    @secured
    def post(self, constraint_id, kleidungsstueck_id):
        """Kleidungsstück zu UnaryConstraint hinzufügen"""
        adm = Admin()
        result = adm.add_kleidungsstueck_to_unary_constraint(constraint_id, kleidungsstueck_id)
        if result:
            return '', 200
        else:
            return '', 500

    @secured
    def delete(self, constraint_id, kleidungsstueck_id):
        """Kleidungsstück aus UnaryConstraint entfernen"""
        adm = Admin()
        result = adm.remove_kleidungsstueck_from_unary_constraint(constraint_id, kleidungsstueck_id)
        if result:
            return '', 200
        else:
            return '', 500

"""
Binary Constraint Methoden
"""
    
@kleiderschrank.route('/binary-constraint')
@kleiderschrank.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class BinaryConstraintListOperations(Resource):
    """Auslesen und Erstellen von BinaryConstraint-Objekten."""

    @kleiderschrank.marshal_list_with(binary_constraint)
    @secured
    def get(self):
        """Alle BinaryConstraints auslesen"""
        adm = Admin()
        data = adm.get_all_binary_constraints()
        return data

    @kleiderschrank.marshal_with(binary_constraint, code=200)
    @kleiderschrank.expect(binary_constraint)
    @secured
    def post(self):
        """Neues BinaryConstraint anlegen"""
        adm = Admin()
        pl_constraint = BinaryConstraint.from_dict(api.payload)
        
        if pl_constraint is not None:
            constraint = adm.create_binary_constraint(
                obj1=pl_constraint.get_obj1(),
                obj2=pl_constraint.get_obj2(),
                bedingung=pl_constraint.get_bedingung()
            )
            return constraint, 200
        else:
            return '', 500

@kleiderschrank.route('/binary-constraint/<int:id>')
@kleiderschrank.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class BinaryConstraintOperations(Resource):
    @kleiderschrank.marshal_with(binary_constraint)
    @secured
    def get(self, id):
        """Einzelnes BinaryConstraint auslesen"""
        adm = Admin()
        data = adm.get_binary_constraint_by_id(id)
        return data

    @kleiderschrank.marshal_with(binary_constraint)
    @kleiderschrank.expect(binary_constraint, validate=True)
    @secured
    def put(self, id):
        """BinaryConstraint aktualisieren"""
        adm = Admin()
        constraint = BinaryConstraint.from_dict(api.payload)
        
        if constraint is not None:
            constraint.set_id(id)
            data = adm.update_binary_constraint(constraint)
            return data, 200
        else:
            return '', 500

    @secured
    def delete(self, id):
        """BinaryConstraint löschen"""
        adm = Admin()
        constraint = adm.get_binary_constraint_by_id(id)
        adm.delete_binary_constraint(constraint)
        return '', 200

@kleiderschrank.route('/binary-constraint-by-user/<int:user_id>')
@kleiderschrank.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class BinaryConstraintUserOperations(Resource):
    @kleiderschrank.marshal_list_with(binary_constraint)
    @secured
    def get(self, user_id):
        """Alle BinaryConstraints eines Users auslesen"""
        adm = Admin()
        data = adm.get_binary_constraints_by_user_id(user_id)
        return data

"""
BinaryConstraint Kleidungsstück Operationen
"""
@kleiderschrank.route('/binary-constraint/<int:constraint_id>/kleidungsstueck/<int:kleidungsstueck_id>')
@kleiderschrank.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class BinaryConstraintKleidungsstueckeManagementOperations(Resource):
    @kleiderschrank.marshal_list_with(kleidungsstueck)
    @secured
    def get(self, constraint_id):
        """Alle Kleidungsstücke eines BinaryConstraints auslesen"""
        adm = Admin()
        data = adm.get_kleidungsstuecke_by_binary_constraint_id(constraint_id)
        return data

    @secured
    def post(self, constraint_id, kleidungsstueck_id):
        """Kleidungsstück zu BinaryConstraint hinzufügen"""
        adm = Admin()
        result = adm.add_kleidungsstueck_to_binary_constraint(constraint_id, kleidungsstueck_id)
        if result:
            return '', 200
        else:
            return '', 500

    @secured
    def delete(self, constraint_id, kleidungsstueck_id):
        """Kleidungsstück aus BinaryConstraint entfernen"""
        adm = Admin()
        result = adm.remove_kleidungsstueck_from_binary_constraint(constraint_id, kleidungsstueck_id)
        if result:
            return '', 200
        else:
            return '', 500

"""
Cardinality Constraint Methoden
"""

@kleiderschrank.route('/cardinality-constraint')
@kleiderschrank.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class CardinalityConstraintListOperations(Resource):
    """Auslesen und Erstellen von CardinalityConstraint-Objekten."""

    @kleiderschrank.marshal_list_with(cardinality_constraint)
    @secured
    def get(self):
        """Alle CardinalityConstraints auslesen"""
        adm = Admin()
        data = adm.get_all_cardinality_constraints()
        return data

    @kleiderschrank.marshal_with(cardinality_constraint, code=200)
    @kleiderschrank.expect(cardinality_constraint)
    @secured
    def post(self):
        """Neues CardinalityConstraint anlegen"""
        adm = Admin()
        pl_constraint = CardinalityConstraint.from_dict(api.payload)
        
        if pl_constraint is not None:
            constraint = adm.create_cardinality_constraint(
                min_count=pl_constraint.get_min_count(),
                max_count=pl_constraint.get_max_count(),
                obj1=pl_constraint.get_obj1(),
                obj2=pl_constraint.get_obj2()
            )
            return constraint, 200
        else:
            return '', 500

@kleiderschrank.route('/cardinality-constraint/<int:id>')
@kleiderschrank.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class CardinalityConstraintOperations(Resource):
    @kleiderschrank.marshal_with(cardinality_constraint)
    @secured
    def get(self, id):
        """Einzelnes CardinalityConstraint auslesen"""
        adm = Admin()
        data = adm.get_cardinality_constraint_by_id(id)
        return data

    @kleiderschrank.marshal_with(cardinality_constraint)
    @kleiderschrank.expect(cardinality_constraint, validate=True)
    @secured
    def put(self, id):
        """CardinalityConstraint aktualisieren"""
        adm = Admin()
        constraint = CardinalityConstraint.from_dict(api.payload)
        
        if constraint is not None:
            constraint.set_id(id)
            data = adm.update_cardinality_constraint(constraint)
            return data, 200
        else:
            return '', 500

    @secured
    def delete(self, id):
        """CardinalityConstraint löschen"""
        adm = Admin()
        constraint = adm.get_cardinality_constraint_by_id(id)
        adm.delete_cardinality_constraint(constraint)
        return '', 200

@kleiderschrank.route('/cardinality-constraint-by-user/<int:user_id>')
@kleiderschrank.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class CardinalityConstraintUserOperations(Resource):
    @kleiderschrank.marshal_list_with(cardinality_constraint)
    @secured
    def get(self, user_id):
        """Alle CardinalityConstraints eines Users auslesen"""
        adm = Admin()
        data = adm.get_cardinality_constraints_by_user_id(user_id)
        return data

"""
CardinalityConstraint Kleidungsstück Operationen
"""
@kleiderschrank.route('/cardinality-constraint/<int:constraint_id>/kleidungsstueck/<int:kleidungsstueck_id>')
@kleiderschrank.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class CardinalityConstraintKleidungsstueckeManagementOperations(Resource):
    @kleiderschrank.marshal_list_with(kleidungsstueck)
    @secured
    def get(self, constraint_id):
        """Alle Kleidungsstücke eines CardinalityConstraints auslesen"""
        adm = Admin()
        data = adm.get_kleidungsstuecke_by_cardinality_constraint_id(constraint_id)
        return data

    @secured
    def post(self, constraint_id, kleidungsstueck_id):
        """Kleidungsstück zu CardinalityConstraint hinzufügen"""
        adm = Admin()
        result = adm.add_kleidungsstueck_to_cardinality_constraint(constraint_id, kleidungsstueck_id)
        if result:
            return '', 200
        else:
            return '', 500

    @secured
    def delete(self, constraint_id, kleidungsstueck_id):
        """Kleidungsstück aus CardinalityConstraint entfernen"""
        adm = Admin()
        result = adm.remove_kleidungsstueck_from_cardinality_constraint(constraint_id, kleidungsstueck_id)
        if result:
            return '', 200
        else:
            return '', 500

"""
Mutex Constraint Methoden
"""

@kleiderschrank.route('/mutex-constraint')
@kleiderschrank.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class MutexConstraintListOperations(Resource):
    """Auslesen und Erstellen von MutexConstraint-Objekten."""

    @kleiderschrank.marshal_list_with(mutex_constraint)
    @secured
    def get(self):
        """Alle MutexConstraints auslesen"""
        adm = Admin()
        data = adm.get_all_mutex_constraints()
        return data

    @kleiderschrank.marshal_with(mutex_constraint, code=200)
    @kleiderschrank.expect(mutex_constraint)
    @secured
    def post(self):
        """Neues MutexConstraint anlegen"""
        adm = Admin()
        pl_constraint = MutexConstraint.from_dict(api.payload)
        
        if pl_constraint is not None:
            constraint = adm.create_mutex_constraint(
                obj1=pl_constraint.get_obj1(),
                obj2=pl_constraint.get_obj2()
            )
            return constraint, 200
        else:
            return '', 500

@kleiderschrank.route('/mutex-constraint/<int:id>')
@kleiderschrank.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class MutexConstraintOperations(Resource):
    @kleiderschrank.marshal_with(mutex_constraint)
    @secured
    def get(self, id):
        """Einzelnes MutexConstraint auslesen"""
        adm = Admin()
        data = adm.get_mutex_constraint_by_id(id)
        return data

    @kleiderschrank.marshal_with(mutex_constraint)
    @kleiderschrank.expect(mutex_constraint, validate=True)
    @secured
    def put(self, id):
        """MutexConstraint aktualisieren"""
        adm = Admin()
        constraint = MutexConstraint.from_dict(api.payload)
        
        if constraint is not None:
            constraint.set_id(id)
            data = adm.update_mutex_constraint(constraint)
            return data, 200
        else:
            return '', 500

    @secured
    def delete(self, id):
        """MutexConstraint löschen"""
        adm = Admin()
        constraint = adm.get_mutex_constraint_by_id(id)
        adm.delete_mutex_constraint(constraint)
        return '', 200

@kleiderschrank.route('/mutex-constraint-by-user/<int:user_id>')
@kleiderschrank.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class MutexConstraintUserOperations(Resource):
    @kleiderschrank.marshal_list_with(mutex_constraint)
    @secured
    def get(self, user_id):
        """Alle MutexConstraints eines Users auslesen"""
        adm = Admin()
        data = adm.get_mutex_constraints_by_user_id(user_id)
        return data

"""
MutexConstraint Kleidungsstück Operationen
"""
@kleiderschrank.route('/mutex-constraint/<int:constraint_id>/kleidungsstueck/<int:kleidungsstueck_id>')
@kleiderschrank.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class MutexConstraintKleidungsstueckeManagementOperations(Resource):
    @kleiderschrank.marshal_list_with(kleidungsstueck)
    @secured
    def get(self, constraint_id):
        """Alle Kleidungsstücke eines MutexConstraints auslesen"""
        adm = Admin()
        data = adm.get_kleidungsstuecke_by_mutex_constraint_id(constraint_id)
        return data

    @secured
    def post(self, constraint_id, kleidungsstueck_id):
        """Kleidungsstück zu MutexConstraint hinzufügen"""
        adm = Admin()
        result = adm.add_kleidungsstueck_to_mutex_constraint(constraint_id, kleidungsstueck_id)
        if result:
            return '', 200
        else:
            return '', 500

    @secured
    def delete(self, constraint_id, kleidungsstueck_id):
        """Kleidungsstück aus MutexConstraint entfernen"""
        adm = Admin()
        result = adm.remove_kleidungsstueck_from_mutex_constraint(constraint_id, kleidungsstueck_id)
        if result:
            return '', 200
        else:
            return '', 500

"""
Implication Constraint Methoden
"""

@kleiderschrank.route('/implication-constraint')
@kleiderschrank.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class ImplicationConstraintListOperations(Resource):
    """Auslesen und Erstellen von ImplicationConstraint-Objekten."""

    @kleiderschrank.marshal_list_with(implication_constraint)
    @secured
    def get(self):
        """Alle ImplicationConstraints auslesen"""
        adm = Admin()
        data = adm.get_all_implication_constraints()
        return data

    @kleiderschrank.marshal_with(implication_constraint, code=200)
    @kleiderschrank.expect(implication_constraint)
    @secured
    def post(self):
        """Neues ImplicationConstraint anlegen"""
        adm = Admin()
        pl_constraint = ImplicationConstraint.from_dict(api.payload)
        
        if pl_constraint is not None:
            constraint = adm.create_implication_constraint(
                condition=pl_constraint.get_condition(),
                implication=pl_constraint.get_implication()
            )
            return constraint, 200
        else:
            return '', 500

@kleiderschrank.route('/implication-constraint/<int:id>')
@kleiderschrank.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class ImplicationConstraintOperations(Resource):
    @kleiderschrank.marshal_with(implication_constraint)
    @secured
    def get(self, id):
        """Einzelnes ImplicationConstraint auslesen"""
        adm = Admin()
        data = adm.get_implication_constraint_by_id(id)
        return data

    @kleiderschrank.marshal_with(implication_constraint)
    @kleiderschrank.expect(implication_constraint, validate=True)
    @secured
    def put(self, id):
        """ImplicationConstraint aktualisieren"""
        adm = Admin()
        constraint = ImplicationConstraint.from_dict(api.payload)
        
        if constraint is not None:
            constraint.set_id(id)
            data = adm.update_implication_constraint(constraint)
            return data, 200
        else:
            return '', 500

    @secured
    def delete(self, id):
        """ImplicationConstraint löschen"""
        adm = Admin()
        constraint = adm.get_implication_constraint_by_id(id)
        adm.delete_implication_constraint(constraint)
        return '', 200

@kleiderschrank.route('/implication-constraint-by-user/<int:user_id>')
@kleiderschrank.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class ImplicationConstraintUserOperations(Resource):
    @kleiderschrank.marshal_list_with(implication_constraint)
    @secured
    def get(self, user_id):
        """Alle ImplicationConstraints eines Users auslesen"""
        adm = Admin()
        data = adm.get_implication_constraints_by_user_id(user_id)
        return data

"""
ImplicationConstraint Kleidungsstück Operationen
"""
@kleiderschrank.route('/implication-constraint/<int:constraint_id>/kleidungsstueck/<int:kleidungsstueck_id>')
@kleiderschrank.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class ImplicationConstraintKleidungsstueckeManagementOperations(Resource):
    @kleiderschrank.marshal_list_with(kleidungsstueck)
    @secured
    def get(self, constraint_id):
        """Alle Kleidungsstücke eines ImplicationConstraints auslesen"""
        adm = Admin()
        data = adm.get_kleidungsstuecke_by_implication_constraint_id(constraint_id)
        return data

    @secured
    def post(self, constraint_id, kleidungsstueck_id):
        """Kleidungsstück zu ImplicationConstraint hinzufügen"""
        adm = Admin()
        result = adm.add_kleidungsstueck_to_implication_constraint(constraint_id, kleidungsstueck_id)
        if result:
            return '', 200
        else:
            return '', 500

    @secured
    def delete(self, constraint_id, kleidungsstueck_id):
        """Kleidungsstück aus ImplicationConstraint entfernen"""
        adm = Admin()
        result = adm.remove_kleidungsstueck_from_implication_constraint(constraint_id, kleidungsstueck_id)
        if result:
            return '', 200
        else:
            return '', 500


"""
Style Methoden
"""

@kleiderschrank.route('/style')
@kleiderschrank.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class StyleListOperations(Resource):
    """Auslesen und Erstellen von Style-Objekten."""

    @kleiderschrank.marshal_list_with(style)
    @secured
    def get(self):
        """Alle Styles auslesen"""
        adm = Admin()
        data = adm.get_all_styles()
        return data

    @kleiderschrank.marshal_with(style, code=200)
    @kleiderschrank.expect(style)
    @secured
    def post(self):
        """Neuen Style anlegen"""
        adm = Admin()
        pl_style = Style.from_dict(api.payload)
        
        if pl_style is not None:
            style = adm.create_style(
                features=pl_style.get_features(),
                constraints=pl_style.get_constraints(),
                bezeichnung=pl_style.get_bezeichnung()
            )
            return style, 200
        else:
            return '', 500

@kleiderschrank.route('/style/<int:id>')
@kleiderschrank.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class StyleOperations(Resource):
    @kleiderschrank.marshal_with(style)
    @secured
    def get(self, id):
        """Einzelnen Style auslesen"""
        adm = Admin()
        data = adm.get_style_by_id(id)
        return data

    @kleiderschrank.marshal_with(style)
    @kleiderschrank.expect(style, validate=True)
    @secured
    def put(self, id):
        """Style aktualisieren"""
        adm = Admin()
        style = Style.from_dict(api.payload)
        
        if style is not None:
            style.set_id(id)
            data = adm.update_style(style)
            return data, 200
        else:
            return '', 500

    @secured
    def delete(self, id):
        """Style löschen"""
        adm = Admin()
        style = adm.get_style_by_id(id)
        adm.delete_style(style)
        return '', 200

@kleiderschrank.route('/style-by-user/<int:user_id>')
@kleiderschrank.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class StyleUserOperations(Resource):
    @kleiderschrank.marshal_list_with(style)
    @secured
    def get(self, user_id):
        """Alle Styles eines Users auslesen"""
        adm = Admin()
        data = adm.get_styles_by_user_id(user_id)
        return data
    
@kleiderschrank.route('/style/<int:id>/constraints')
@kleiderschrank.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class StyleConstraintOperations(Resource):
    @kleiderschrank.marshal_list_with(constraint)
    @secured
    def get(self, id):
        """Alle Constraints eines Styles auslesen"""
        adm = Admin()
        data = adm.get_constraints_by_style_id(id)
        return data

@kleiderschrank.route('/style/<int:id>/unary-constraints')
@kleiderschrank.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class StyleUnaryConstraintOperations(Resource):
    @kleiderschrank.marshal_list_with(unary_constraint)
    @secured
    def get(self, id):
        """Alle UnaryConstraints eines Styles auslesen"""
        adm = Admin()
        data = adm.get_unary_constraints_by_style_id(id)
        return data

@kleiderschrank.route('/style/<int:id>/binary-constraints')
@kleiderschrank.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class StyleBinaryConstraintOperations(Resource):
    @kleiderschrank.marshal_list_with(binary_constraint)
    @secured
    def get(self, id):
        """Alle BinaryConstraints eines Styles auslesen"""
        adm = Admin()
        data = adm.get_binary_constraints_by_style_id(id)
        return data

@kleiderschrank.route('/style/<int:id>/cardinality-constraints')
@kleiderschrank.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class StyleCardinalityConstraintOperations(Resource):
    @kleiderschrank.marshal_list_with(cardinality_constraint)
    @secured
    def get(self, id):
        """Alle CardinalityConstraints eines Styles auslesen"""
        adm = Admin()
        data = adm.get_cardinality_constraints_by_style_id(id)
        return data

@kleiderschrank.route('/style/<int:id>/mutex-constraints')
@kleiderschrank.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class StyleMutexConstraintOperations(Resource):
    @kleiderschrank.marshal_list_with(mutex_constraint)
    @secured
    def get(self, id):
        """Alle MutexConstraints eines Styles auslesen"""
        adm = Admin()
        data = adm.get_mutex_constraints_by_style_id(id)
        return data

@kleiderschrank.route('/style/<int:id>/implication-constraints')
@kleiderschrank.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class StyleImplicationConstraintOperations(Resource):
    @kleiderschrank.marshal_list_with(implication_constraint)
    @secured
    def get(self, id):
        """Alle ImplicationConstraints eines Styles auslesen"""
        adm = Admin()
        data = adm.get_implication_constraints_by_style_id(id)
        return data

"""
Kleiderschrank Methoden
"""

@kleiderschrank.route('/kleiderschrank')
@kleiderschrank.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class KleiderschrankListOperations(Resource):
    """Auslesen und Erstellen von Kleiderschrank-Objekten."""

    @kleiderschrank.marshal_list_with(kleiderschrank)
    @secured
    def get(self):
        """Alle Kleiderschränke auslesen"""
        adm = Admin()
        data = adm.get_all_kleiderschraenke()
        return data

    @kleiderschrank.marshal_with(kleiderschrank, code=200)
    @kleiderschrank.expect(kleiderschrank)
    @secured
    def post(self):
        """Neuen Kleiderschrank anlegen"""
        adm = Admin()
        pl_kleiderschrank = Kleiderschrank.from_dict(api.payload)
        
        if pl_kleiderschrank is not None:
            neuer_kleiderschrank = adm.create_kleiderschrank(
                name=pl_kleiderschrank.get_name(),
                beschreibung=pl_kleiderschrank.get_beschreibung()
            )
            return neuer_kleiderschrank, 200
        else:
            return '', 500

@kleiderschrank.route('/kleiderschrank/<int:id>')
@kleiderschrank.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class KleiderschrankOperations(Resource):
    @kleiderschrank.marshal_with(kleiderschrank)
    @secured
    def get(self, id):
        """Einzelnen Kleiderschrank auslesen"""
        adm = Admin()
        data = adm.get_kleiderschrank_by_id(id)
        return data

    @kleiderschrank.marshal_with(kleiderschrank)
    @kleiderschrank.expect(kleiderschrank, validate=True)
    @secured
    def put(self, id):
        """Kleiderschrank aktualisieren"""
        adm = Admin()
        kleiderschrank = Kleiderschrank.from_dict(api.payload)
        
        if kleiderschrank is not None:
            kleiderschrank.set_id(id)
            data = adm.update_kleiderschrank(kleiderschrank)
            return data, 200
        else:
            return '', 500

    @secured
    def delete(self, id):
        """Kleiderschrank löschen"""
        adm = Admin()
        kleiderschrank = adm.get_kleiderschrank_by_id(id)
        adm.delete_kleiderschrank(kleiderschrank)
        return '', 200

@kleiderschrank.route('/kleiderschrank-by-user/<int:user_id>')
@kleiderschrank.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class KleiderschrankUserOperations(Resource):
    @kleiderschrank.marshal_list_with(kleiderschrank)
    @secured
    def get(self, user_id):
        """Alle Kleiderschränke eines Users auslesen"""
        adm = Admin()
        data = adm.get_kleiderschraenke_by_user_id(user_id)
        return data


"""
Kleidungsstück Methoden
"""

@kleiderschrank.route('/kleidungsstueck')
@kleiderschrank.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class KleidungsstueckListOperations(Resource):
    """Auslesen und Erstellen von Kleidungsstueck-Objekten."""

    @kleiderschrank.marshal_list_with(kleidungsstueck)
    @secured
    def get(self):
        """Alle Kleidungsstücke auslesen"""
        adm = Admin()
        data = adm.get_all_kleidungsstuecke()
        return data

    @kleiderschrank.marshal_with(kleidungsstueck, code=200)
    @kleiderschrank.expect(kleidungsstueck)
    @secured
    def post(self):
        """Neues Kleidungsstück anlegen"""
        adm = Admin()
        pl_kleidungsstueck = Kleidungsstueck.from_dict(api.payload)
        
        if pl_kleidungsstueck is not None:
            kleidungsstueck = adm.create_kleidungsstueck(
                kleidungstyp=pl_kleidungsstueck.get_kleidungstyp(),
                name=pl_kleidungsstueck.get_name()
            )
            return kleidungsstueck, 200
        else:
            return '', 500

@kleiderschrank.route('/kleidungsstueck/<int:id>')
@kleiderschrank.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class KleidungsstueckOperations(Resource):
    @kleiderschrank.marshal_with(kleidungsstueck)
    @secured
    def get(self, id):
        """Einzelnes Kleidungsstück auslesen"""
        adm = Admin()
        data = adm.get_kleidungsstueck_by_id(id)
        return data

    @kleiderschrank.marshal_with(kleidungsstueck)
    @kleiderschrank.expect(kleidungsstueck, validate=True)
    @secured
    def put(self, id):
        """Kleidungsstück aktualisieren"""
        adm = Admin()
        kleidungsstueck = Kleidungsstueck.from_dict(api.payload)
        
        if kleidungsstueck is not None:
            kleidungsstueck.set_id(id)
            data = adm.update_kleidungsstueck(kleidungsstueck)
            return data, 200
        else:
            return '', 500

    @secured
    def delete(self, id):
        """Kleidungsstück löschen"""
        adm = Admin()
        kleidungsstueck = adm.get_kleidungsstueck_by_id(id)
        adm.delete_kleidungsstueck(kleidungsstueck)
        return '', 200

@kleiderschrank.route('/kleidungsstueck-by-user/<int:user_id>')
@kleiderschrank.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class KleidungsstueckUserOperations(Resource):
    @kleiderschrank.marshal_list_with(kleidungsstueck)
    @secured
    def get(self, user_id):
        """Alle Kleidungsstücke eines Users auslesen"""
        adm = Admin()
        data = adm.get_kleidungsstuecke_by_user_id(user_id)
        return data
    
"""
Kleidungstyp Methoden
"""
    
@kleiderschrank.route('/kleidungstyp')
@kleiderschrank.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class KleidungstypListOperations(Resource):
    """Auslesen und Erstellen von Kleidungstyp-Objekten."""

    @kleiderschrank.marshal_list_with(kleidungstyp)
    @secured
    def get(self):
        """Alle Kleidungstypen auslesen"""
        adm = Admin()
        data = adm.get_all_kleidungstypen()
        return data

    @kleiderschrank.marshal_with(kleidungstyp, code=200)
    @kleiderschrank.expect(kleidungstyp)
    @secured
    def post(self):
        """Neuen Kleidungstyp anlegen"""
        adm = Admin()
        pl_kleidungstyp = Kleidungstyp.from_dict(api.payload)
        
        if pl_kleidungstyp is not None:
            kleidungstyp = adm.create_kleidungstyp(
                bezeichnung=pl_kleidungstyp.get_bezeichnung(),
                verwendung=pl_kleidungstyp.get_verwendung()
            )
            return kleidungstyp, 200
        else:
            return '', 500

@kleiderschrank.route('/kleidungstyp/<int:id>')
@kleiderschrank.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class KleidungstypOperations(Resource):
    @kleiderschrank.marshal_with(kleidungstyp)
    @secured
    def get(self, id):
        """Einzelnen Kleidungstyp auslesen"""
        adm = Admin()
        data = adm.get_kleidungstyp_by_id(id)
        return data

    @kleiderschrank.marshal_with(kleidungstyp)
    @kleiderschrank.expect(kleidungstyp, validate=True)
    @secured
    def put(self, id):
        """Kleidungstyp aktualisieren"""
        adm = Admin()
        kleidungstyp = Kleidungstyp.from_dict(api.payload)
        
        if kleidungstyp is not None:
            kleidungstyp.set_id(id)
            data = adm.update_kleidungstyp(kleidungstyp)
            return data, 200
        else:
            return '', 500

    @secured
    def delete(self, id):
        """Kleidungstyp löschen"""
        adm = Admin()
        kleidungstyp = adm.get_kleidungstyp_by_id(id)
        adm.delete_kleidungstyp(kleidungstyp)
        return '', 200

@kleiderschrank.route('/kleidungstyp-by-user/<int:user_id>')
@kleiderschrank.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class KleidungstypUserOperations(Resource):
    @kleiderschrank.marshal_list_with(kleidungstyp)
    @secured
    def get(self, user_id):
        """Alle Kleidungstypen eines Users auslesen"""
        adm = Admin()
        data = adm.get_kleidungstypen_by_user_id(user_id)
        return data

"""
Outfit Methoden
"""

@kleiderschrank.route('/outfit')
@kleiderschrank.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class OutfitListOperations(Resource):
    @kleiderschrank.marshal_list_with(outfit)
    @secured
    def get(self):
        """Alle Outfits auslesen"""
        adm = Admin()
        data = adm.get_all_outfits()
        return data

    @kleiderschrank.marshal_with(outfit, code=200)
    @kleiderschrank.expect(outfit)
    @secured
    def post(self):
        """Neues Outfit anlegen"""
        adm = Admin()
        pl_outfit = Outfit.from_dict(api.payload)
        
        if pl_outfit is not None:
            outfit = adm.create_outfit(
                name=pl_outfit.get_name()
            )
            return outfit, 200
        else:
            return '', 500

@kleiderschrank.route('/outfit/<int:id>')
@kleiderschrank.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class OutfitOperations(Resource):
    @kleiderschrank.marshal_with(outfit)
    @secured
    def get(self, id):
        """Einzelnes Outfit auslesen"""
        adm = Admin()
        data = adm.get_outfit_by_id(id)
        return data

    @kleiderschrank.marshal_with(outfit)
    @kleiderschrank.expect(outfit, validate=True)
    @secured
    def put(self, id):
        """Outfit aktualisieren"""
        adm = Admin()
        outfit = Outfit.from_dict(api.payload)
        
        if outfit is not None:
            outfit.set_id(id)
            data = adm.update_outfit(outfit)
            return data, 200
        else:
            return '', 500

    @secured
    def delete(self, id):
        """Outfit löschen"""
        adm = Admin()
        outfit = adm.get_outfit_by_id(id)
        adm.delete_outfit(outfit)
        return '', 200

@kleiderschrank.route('/outfit-by-user/<int:user_id>')
@kleiderschrank.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class OutfitUserOperations(Resource):
    @kleiderschrank.marshal_list_with(outfit)
    @secured
    def get(self, user_id):
        """Alle Outfits eines Users auslesen"""
        adm = Admin()
        data = adm.get_outfits_by_user_id(user_id)
        return data

@kleiderschrank.route('/outfit/<int:id>/kleidungsstuecke')
@kleiderschrank.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class OutfitKleidungsstueckeOperations(Resource):
    @kleiderschrank.marshal_list_with(kleidungsstueck)
    @secured
    def get(self, id):
        """Alle Kleidungsstücke eines Outfits auslesen"""
        adm = Admin()
        data = adm.get_kleidungsstuecke_by_outfit_id(id)
        return data
    
@kleiderschrank.route('/outfit/<int:outfit_id>/kleidungsstueck/<int:kleidungsstueck_id>')
@kleiderschrank.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class OutfitKleidungsstueckManagementOperations(Resource):
    @secured
    def post(self, outfit_id, kleidungsstueck_id):
        """Kleidungsstück zu einem Outfit hinzufügen"""
        adm = Admin()
        result = adm.add_kleidungsstueck_to_outfit(outfit_id, kleidungsstueck_id)
        if result:
            return '', 200
        else:
            return '', 500

    @secured
    def delete(self, outfit_id, kleidungsstueck_id):
        """Kleidungsstück aus einem Outfit entfernen"""
        adm = Admin()
        result = adm.remove_kleidungsstueck_from_outfit(outfit_id, kleidungsstueck_id)
        if result:
            return '', 200
        else:
            return '', 500

if __name__ == '__main__':
    app.run(debug=True)