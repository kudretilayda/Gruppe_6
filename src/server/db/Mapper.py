# src/server/db/mapper/mapper.py

import mysql.connector
from mysql.connector import Error
from config.config import get_db_connection

class Mapper:
    """Basis-Mapper-Klasse, von der alle anderen Mapper erben."""

    def __init__(self):
        self._cnx = None

    def _get_connection(self):
        """Datenbankverbindung herstellen"""
        if self._cnx is None:
            self._cnx = get_db_connection()
        return self._cnx

    def find_all(self):
        """Abstrakte Methode, die von Kindklassen implementiert werden muss"""
        raise NotImplementedError("Please implement this method")

    def find_by_id(self, key):
        """Abstrakte Methode, die von Kindklassen implementiert werden muss"""
        raise NotImplementedError("Please implement this method")

    def insert(self, object):
        """Abstrakte Methode, die von Kindklassen implementiert werden muss"""
        raise NotImplementedError("Please implement this method")

    def update(self, object):
        """Abstrakte Methode, die von Kindklassen implementiert werden muss"""
        raise NotImplementedError("Please implement this method")

    def delete(self, object):
        """Abstrakte Methode, die von Kindklassen implementiert werden muss"""
        raise NotImplementedError("Please implement this method")