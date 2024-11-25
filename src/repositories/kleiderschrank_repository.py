import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()

class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.connection = None
        return cls._instance

    def connect(self):
        """Stellt Verbindung zur Google Cloud SQL her (lokal MySQL für Entwicklung)"""
        if not self.connection or not self.connection.is_connected():
            try:
                # Für lokale Entwicklung
                if os.getenv('ENVIRONMENT') == 'development':
                    self.connection = mysql.connector.connect(
                        host='localhost',
                        user='root',
                        password=os.getenv('DB_PASSWORD'),
                        database='digital_wardrobe'
                    )
                else:
                    # Für Google Cloud SQL
                    self.connection = mysql.connector.connect(
                        host=os.getenv('CLOUD_SQL_HOST'),
                        user=os.getenv('CLOUD_SQL_USER'),
                        password=os.getenv('CLOUD_SQL_PASSWORD'),
                        database=os.getenv('CLOUD_SQL_DATABASE')
                    )
                print("Datenbankverbindung erfolgreich hergestellt")
            except Error as e:
                print(f"Fehler bei der Datenbankverbindung: {e}")
                raise

    def get_connection(self):
        """Gibt eine aktive Datenbankverbindung zurück"""
        if not self.connection or not self.connection.is_connected():
            self.connect()
        return self.connection

    def execute_query(self, query, params=None):
        """Führt eine Datenbankabfrage aus"""
        cursor = self.get_connection().cursor(dictionary=True)
        try:
            cursor.execute(query, params or ())
            self.connection.commit()
            return cursor
        except Error as e:
            print(f"Fehler bei der Ausführung der Query: {e}")
            self.connection.rollback()
            raise
        finally:
            cursor.close()