# src/server/config/config.py

import os
import json
import mysql.connector

class Config:
    """Konfigurationsklasse für die Datenbankverbindung."""
    
    def __init__(self):
        self._connection = None
        
    def db_connection(self):
        """Singleton für die Datenbankverbindung."""
        if self._connection is None:
            try:
                if os.getenv('GAE_ENV', '').startswith('standard'):
                    # Google Cloud SQL Konfiguration (Production)
                    self._connection = mysql.connector.connect(
                        user=os.getenv('DB_USER'),
                        password=os.getenv('DB_PASS'),
                        host=os.getenv('DB_HOST'),
                        database=os.getenv('DB_NAME'),
                        ssl_ca=os.getenv('SSL_CA_PATH')
                    )
                else:
                    # Lokale Entwicklungsumgebung
                    self._connection = mysql.connector.connect(
                        user='root',
                        password='root',
                        host='localhost',
                        database='digital_wardrobe'
                    )
                    
                print("DB connection successful")
            except mysql.connector.Error as err:
                print(f"Error: {err}")
                raise
                
        return self._connection

# Singleton-Instanz der Config-Klasse
config = Config()

def get_db_connection():
    """Globale Funktion zum Abrufen der Datenbankverbindung."""
    return config.db_connection()