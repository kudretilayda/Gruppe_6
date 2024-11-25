import os
from dotenv import load_dotenv

load_dotenv()  # Lädt die Werte aus der .env-Datei

class Config:
    MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
    MYSQL_USER = os.getenv('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', 'kik2001duman123')
    MYSQL_DATABASE = os.getenv('MYSQL_DATABASE', 'digital_wardrobe')
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')


# src/db/database.py
import mysql.connector
from mysql.connector import Error
from contextlib import contextmanager
from src.config.config import Config

class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance.connection = None
        return cls._instance

    def connect(self):
        """Erstellt eine Datenbankverbindung"""
        if not self.connection:
            try:
                self.connection = mysql.connector.connect(
                    host=Config.MYSQL_HOST,
                    user=Config.MYSQL_USER,
                    password=Config.MYSQL_PASSWORD,
                    database=Config.MYSQL_DATABASE
                )
                print("Erfolgreich mit der Datenbank verbunden")
            except Error as e:
                print(f"Fehler beim Verbinden mit der Datenbank: {e}")
                raise

    @contextmanager
    def get_cursor(self):
        """Cursor Context Manager für sichere Datenbankoperationen"""
        cursor = None
        try:
            if not self.connection or not self.connection.is_connected():
                self.connect()
            cursor = self.connection.cursor(dictionary=True)
            yield cursor
            self.connection.commit()
        except Error as e:
            self.connection.rollback()
            print(f"Datenbankfehler: {e}")
            raise
        finally:
            if cursor:
                cursor.close()

    def close(self):
        """Schließt die Datenbankverbindung"""
        if self.connection and self.connection.is_connected():
            self.connection.close()