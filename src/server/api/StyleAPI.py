# server/api/StyleAPI.py
from flask import Flask, request
from flask_restx import Api, Resource, Namespace
from server.services.StyleService import StyleService

app = Flask(__name__)
api = Api(app)
style_ns = Namespace('styles')

@style_ns.route('/')
class StyleList(Resource):
    @style_ns.doc('list_styles')
    def get(self):
        service = StyleService()
        return [style.to_dict() for style in service.get_all_styles()]

    @style_ns.doc('create_style')
    def post(self):
        data = request.get_json()
        service = StyleService()
        style = service.create_style(
            data['name'],
            data['description'],
            data['created_by']
        )
        return style.to_dict(), 201

@style_ns.route('/<string:id>')
class StyleOperations(Resource):
    @style_ns.doc('get_style')
    def get(self, id):
        service = StyleService()
        style = service.get_style(id)
        return style.to_dict() if style else ('Style not found', 404)

    @style_ns.doc('delete_style')
    def delete(self, id):
        service = StyleService()
        if service.delete_style(id):
            return '', 204
        return 'Style not found', 404

api.add_namespace(style_ns)

if __name__ == '__main__':
    app.run(debug=True)
