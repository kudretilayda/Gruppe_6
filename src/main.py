from flask import Flask, jsonify, request
from flask_cors import CORS
from mysql.connector import get_db_connection

app = Flask(__name__)
CORS(app)

# Route um alle Kleidungsstücke aus einem Kleiderschrank zu holen
@app.route('/wardrobe/<wardrobe_id>/items', methods=['GET'])
def get_wardrobe_items(wardrobe_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    try:
        cursor.execute("SELECT * FROM clothing_item WHERE wardrobe_id = %s", (wardrobe_id,))
        items = cursor.fetchall()
        return jsonify(items)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

# Route um ein neues Kleidungsstück hinzuzufügen
@app.route('/wardrobe/<wardrobe_id>/items', methods=['POST'])
def add_clothing_item(wardrobe_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        data = request.json
        query = """
        INSERT INTO clothing_item (wardrobe_id, type_id, name, color, brand, season)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (
            wardrobe_id,
            data['type_id'],
            data['name'],
            data.get('color'),
            data.get('brand'),
            data.get('season')
        )
        
        cursor.execute(query, values)
        conn.commit()
        
        return jsonify({"message": "Item erfolgreich hinzugefügt", "id": cursor.lastrowid}), 201
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

# Route um einen Style abzurufen
@app.route('/styles/<style_id>', methods=['GET'])
def get_style(style_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    try:
        # Hole Style-Informationen
        cursor.execute("SELECT * FROM style WHERE id = %s", (style_id,))
        style = cursor.fetchone()
        
        if style:
            # Hole zugehörige Constraints
            cursor.execute("SELECT * FROM style_constraint WHERE style_id = %s", (style_id,))
            constraints = cursor.fetchall()
            style['constraints'] = constraints
            
        return jsonify(style if style else {})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)