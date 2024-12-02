# src/server/api/person.py

from flask import request
from flask_restx import Namespace, Resource, fields
from config.security_config import SecurityConfig
from admin.Admin import Administration

person_namespace = Namespace('persons', description='Person operations')

# API Models
person_model = person_namespace.model('Person', {
    'id': fields.String(readonly=True),
    'google_id': fields.String(required=True),
    'firstname': fields.String(required=True),
    'lastname': fields.String(required=True),
    'nickname': fields.String(required=False)
})

@person_namespace.route('/')
class PersonListOperations(Resource):
    @person_namespace.marshal_list_with(person_model)
    @SecurityConfig.check_auth()
    def get(self):
        """Alle Personen auflisten"""
        adm = Administration()
        return adm._person_mapper.find_all()

    @person_namespace.expect(person_model)
    @person_namespace.marshal_with(person_model)
    def post(self):
        """Neue Person erstellen"""
        adm = Administration()
        person_data = request.json
        
        return adm.create_person(
            person_data['google_id'],
            person_data['firstname'],
            person_data['lastname'],
            person_data.get('nickname')
        )

@person_namespace.route('/<string:person_id>')
class PersonOperations(Resource):
    @person_namespace.marshal_with(person_model)
    @SecurityConfig.check_auth()
    def get(self, person_id):
        """Person nach ID finden"""
        adm = Administration()
        return adm.get_person_by_id(person_id)

    @person_namespace.expect(person_model)
    @person_namespace.marshal_with(person_model)
    @SecurityConfig.check_auth()
    def put(self, person_id):
        """Person aktualisieren"""
        adm = Administration()
        person = adm.get_person_by_id(person_id)
        person_data = request.json
        
        person.set_firstname(person_data['firstname'])
        person.set_lastname(person_data['lastname'])
        person.set_nickname(person_data.get('nickname'))
        
        adm._person_mapper.update(person)
        return person

    @SecurityConfig.check_auth()
    def delete(self, person_id):
        """Person löschen"""
        adm = Administration()
        person = adm.get_person_by_id(person_id)
        adm._person_mapper.delete(person)
        return '', 204