# src/server/service/PersonService.py

from flask import request
from flask_restx import Namespace, Resource, fields
from Admin import WardrobeAdministration
from SecurityDecorator import SecurityDecorator

api = Namespace('person', description='Person related operations')

# API Models
person_model = api.model('Person', {
    'id': fields.String(readonly=True),
    'google_id': fields.String(required=True),
    'firstname': fields.String(required=True),
    'lastname': fields.String(required=True),
    'nickname': fields.String(required=False),
    'create_time': fields.DateTime(readonly=True)
})

@api.route('/')
class PersonListOperations(Resource):
    @SecurityDecorator.check_valid_token
    @api.marshal_list_with(person_model)
    def get(self):
        """Liste aller Personen"""
        adm = WardrobeAdministration()
        return adm.get_all_persons()

    @SecurityDecorator.check_valid_token
    @api.expect(person_model)
    @api.marshal_with(person_model, code=201)
    def post(self):
        """Person erstellen"""
        adm = WardrobeAdministration()
        data = api.payload
        return adm.create_person(
            data['google_id'],
            data['firstname'],
            data['lastname'],
            data.get('nickname')
        ), 201

@api.route('/<id>')
@api.response(404, 'Person nicht gefunden')
class PersonOperations(Resource):
    @SecurityDecorator.check_valid_token
    @api.marshal_with(person_model)
    def get(self, id):
        """Person by ID"""
        adm = WardrobeAdministration()
        result = adm.get_person_by_id(id)
        if result is not None:
            return result
        api.abort(404, f"Person {id} nicht gefunden")

    @SecurityDecorator.check_valid_token
    @api.expect(person_model)
    @api.marshal_with(person_model)
    def put(self, id):
        """Person aktualisieren"""
        adm = WardrobeAdministration()
        person = adm.get_person_by_id(id)
        if person is not None:
            data = api.payload
            person.set_firstname(data['firstname'])
            person.set_lastname(data['lastname'])
            person.set_nickname(data.get('nickname'))
            adm.update_person(person)
            return person
        api.abort(404, f"Person {id} nicht gefunden")

    @SecurityDecorator.check_valid_token
    def delete(self, id):
        """Person löschen"""
        adm = WardrobeAdministration()
        person = adm.get_person_by_id(id)
        if person is not None:
            adm.delete_person(person)
            return '', 204
        api.abort(404, f"Person {id} nicht gefunden")

@api.route('/google/<google_id>')
@api.response(404, 'Person nicht gefunden')
class PersonGoogleOperations(Resource):
    @SecurityDecorator.check_valid_token
    @api.marshal_with(person_model)
    def get(self, google_id):
        """Person by Google ID"""
        adm = WardrobeAdministration()
        result = adm.get_person_by_google_id(google_id)
        if result is not None:
            return result
        api.abort(404, f"Person mit Google ID {google_id} nicht gefunden")