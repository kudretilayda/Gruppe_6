import mysql.connector as connector
import os
from contextlib import AbstractContextManager
from abc import ABC, abstractmethod


class Mapper(AbstractContextManager, ABC):
    def __init__(self):
        self._cnx = None

    def __enter__(self):

        if os.getenv('DATABASE_URL', '').startswith(''):
            self._cnx = connector.connect(user='demo', password='demo',
                                          unix_socket='/cloudsql/<your-connection-string>',
                                          database='<your-database>')   # Unsere Daten

        else:
            self._cnx = connector.connect(user='demo', password='demo',
                                          host='localhost',
                                          database='<your>')            # Unsere Daten
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._cnx.close()

    @abstractmethod
    def find_all(self):             # Liest Tupel aus und gibt sie als Objekte zurück
        pass

    @abstractmethod
    def find_by_key(self, key):     # Liest Tupel mit ID aus
        pass

    @abstractmethod
    def insert(self, obj):          # Fügt Objekt in die DB ein
        pass

    @abstractmethod
    def update(self, obj):          # Objekt wird auf einen bereits in der DB enthaltenen Datensatz abgebildet
        pass

    @abstractmethod
    def delete(self, obj):          # Objekt in der DB wird gelöscht
        pass
