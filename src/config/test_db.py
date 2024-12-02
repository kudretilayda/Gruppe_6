# src/server/utils/db_test.py

from src.config import get_db_connection

def test_db_connection():
    """Test der Datenbankverbindung."""
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        
        # Testabfrage
        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()
        print(f"Database version: {version[0]}")
        
        # Test-Selects für jede Tabelle
        tables = [
            'person', 'wardrobe', 'clothing_type', 'clothing_item',
            'outfit', 'outfit_items', 'style', 'constraint_rule',
            'binary_constraint', 'unary_constraint'
        ]
        
        for table in tables:
            try:
                cursor.execute(f"SELECT COUNT(*) FROM {table}")
                count = cursor.fetchone()[0]
                print(f"Table {table}: {count} records")
            except Exception as e:
                print(f"Error accessing table {table}: {e}")
        
        cursor.close()
        return True, "Database connection test successful"
        
    except Exception as e:
        return False, f"Database connection test failed: {e}"