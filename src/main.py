from flask import Flask, jsonify, request
from flask_restx import Api, Resource, fields
from flask_cors import CORS
import mysql.connector
import os

app = Flask(__name__)

# CORS aktivieren (so dass Frontend und Backend kommunizieren können)
CORS(app)

# Flask-RESTX API erstellen
api = Api(app, version='1.0', title='Digital Wardrobe API',
          description='API für das Management eines digitalen Kleiderschranks')

# Setze Umgebungsvariablen (die Verbindung zur DB)
app.config.from_object('config.Config')

# MySQL-Verbindung (Datenbankinformationen werden aus der Konfiguration geladen)
def get_db_connection():
    connection = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )
    return connection

# Modell für die API (Kleidungsstücke)
kleidungsstueck_model = api.model('Kleidungsstück', {
    'id': fields.Integer('ID des Kleidungsstücks'),
    'bezeichnung': fields.String('Bezeichnung des Kleidungsstücks'),
    'typ_id': fields.Integer('Kleidungsstück-Typ ID'),
    'kleiderschrank_id': fields.Integer('Kleiderschrank ID'),
    'created_at': fields.DateTime('Erstellungsdatum'),
    'updated_at': fields.DateTime('Änderungsdatum')
})

# Route zum Abrufen von Kleidungsstücken
@api.route('/kleidung')
class KleidungList(Resource):
    def get(self):
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute('SELECT * FROM Kleidungsstueck')  # Hole alle Kleidungsstücke
        kleidung = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(kleidung)

# Route zum Hinzufügen eines Kleidungsstücks
@api.route('/kleidung/add')
class KleidungAdd(Resource):
    @api.expect(kleidungsstueck_model)  # Erwartetes JSON-Datenmodell
    def post(self):
        new_kleidung = request.json
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO Kleidungsstueck (kleiderschrank_id, typ_id, bezeichnung)
            VALUES (%s, %s, %s)
        ''', (new_kleidung['kleiderschrank_id'], new_kleidung['typ_id'], new_kleidung['bezeichnung']))
        connection.commit()
        cursor.close()
        connection.close()
        return {'message': 'Kleidungsstück erfolgreich hinzugefügt'}, 201

# Route zum Abrufen von Kleiderschränken
@api.route('/kleiderschrank')
class KleiderschrankList(Resource):
    def get(self):
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute('SELECT * FROM Kleiderschrank')  # Hole alle Kleiderschränke
        kleiderschrank = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(kleiderschrank)

# Route zum Abrufen von Personen
@api.route('/personen')
class PersonenList(Resource):
    def get(self):
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute('SELECT * FROM Person')  # Hole alle Personen
        personen = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(personen)

if __name__ == '__main__':
    app.run(debug=True)

