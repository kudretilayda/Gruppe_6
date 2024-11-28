# src/server/db/mapper/Mapper.py

import mysql.connector as connector
import os
from abc import ABC, abstractmethod
from contextlib import contextmanager

class Mapper(ABC):
    """Abstrakte Basisklasse aller Mapper-Klassen"""

    def __init__(self):
        self._cnx = None

    def _get_connection(self):
        if self._cnx is None:
            self._cnx = connector.connect(
                user='root',
                password='root',
                host='localhost',
                database='digital_wardrobe',
                charset='utf8'
            )
        return self._cnx

    @contextmanager
    def _cursor(self):
        connection = self._get_connection()
        cursor = connection.cursor(dictionary=True)
        try:
            yield cursor
        finally:
            if cursor is not None:
                cursor.close()

    def _close(self):
        if self._cnx is not None:
            self._cnx.close()
            self._cnx = None