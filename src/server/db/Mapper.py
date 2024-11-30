import mysql.connector as connector
from mysql.connector import Error, errorcode
from abc import ABC, abstractmethod
from contextlib import contextmanager
import os
from dotenv import load_dotenv
import logging

# Laden von Umgebungsvariablen aus .env-Datei
load_dotenv()

# Logging konfigurieren
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class Mapper(ABC):
    """Abstrakte Basisklasse für Datenbank-Mapping.

    Diese Klasse implementiert grundlegende Funktionen für den Umgang mit der Datenbank.
    Sie dient als Basis für konkrete Mapper-Subklassen.
    """
    
    def __init__(self):
        """Initialisiert die Mapper-Klasse und bereitet die Verbindungskonfiguration vor."""
        self._connection = None

    def _get_connection(self):
        """Erstellt oder gibt eine bestehende Verbindung zur Datenbank zurück."""
        if not self._connection:
            try:
                self._connection = connector.connect(
                    host=os.getenv('DB_HOST', 'localhost'),
                    user=os.getenv('DB_USER', 'root'),
                    password=os.getenv('DB_PASSWORD', ''),
                    database=os.getenv('DB_NAME', 'digital_wardrobe'),
                    charset='utf8mb4',
                    collation='utf8mb4_unicode_ci'
                )
                logging.info("Datenbankverbindung erfolgreich hergestellt.")
            except Error as e:
                logging.error(f"Fehler bei der Datenbankverbindung: {e}")
                raise e
        return self._connection

    @contextmanager
    def _cursor(self):
        """Kontextmanager für Datenbank-Cursor."""
        connection = self._get_connection()
        cursor = connection.cursor(dictionary=True, buffered=True)
        try:
            yield cursor
        except Error as e:
            self._handle_error(e)
        finally:
            cursor.close()

    def _commit(self):
        """Bestätigt Änderungen in der Datenbank."""
        if self._connection:
            self._connection.commit()
            logging.info("Änderungen in der Datenbank bestätigt.")

    def _rollback(self):
        """Macht Änderungen in der Datenbank rückgängig."""
        if self._connection:
            self._connection.rollback()
            logging.warning("Transaktion wurde zurückgesetzt.")

    def _close(self):
        """Schließt die Datenbankverbindung."""
        if self._connection:
            self._connection.close()
            self._connection = None
            logging.info("Datenbankverbindung geschlossen.")

    def _handle_error(self, err):
        """Behandelt Datenbankfehler und loggt diese."""
        error_message = f"Datenbankfehler: {str(err)}"
        if isinstance(err, connector.Error):
            if err.errno == errorcode.ER_DUP_ENTRY:
                error_message = "Eintrag mit dieser ID existiert bereits."
            elif err.errno == errorcode.ER_BAD_NULL_ERROR:
                error_message = "Ein erforderliches Feld fehlt."
        logging.error(error_message)
        self._rollback()
        raise Exception(error_message)

    def find_all(self):
        """Liest alle Datensätze aus der entsprechenden Tabelle."""
        result = []
        with self._cursor() as cursor:
            command = f"SELECT * FROM {self.get_table_name()}"
            cursor.execute(command)
            tuples = cursor.fetchall()
            result = [self.tuple_to_object(t) for t in tuples]
        return result

    def find_by_key(self, key):
        """Sucht einen Datensatz anhand des Primärschlüssels."""
        with self._cursor() as cursor:
            command = f"SELECT * FROM {self.get_table_name()} WHERE id = %s"
            cursor.execute(command, (key,))
            result = cursor.fetchone()
            return self.tuple_to_object(result) if result else None

    def delete(self, obj):
        """Löscht einen Datensatz aus der Datenbank."""
        with self._cursor() as cursor:
            command = f"DELETE FROM {self.get_table_name()} WHERE id = %s"
            cursor.execute(command, (obj.get_id(),))
            self._commit()
            logging.info(f"Objekt mit ID {obj.get_id()} erfolgreich gelöscht.")
            return cursor.rowcount > 0

    @abstractmethod
    def insert(self, obj):
        """Fügt ein Objekt in die Datenbank ein."""
        pass

    @abstractmethod
    def update(self, obj):
        """Aktualisiert ein Objekt in der Datenbank."""
        pass

    @abstractmethod
    def tuple_to_object(self, tuple):
        """Konvertiert ein Datenbank-Tupel in ein Objekt."""
        pass

    @abstractmethod
    def get_table_name(self):
        """Gibt den Tabellennamen zurück."""
        pass
