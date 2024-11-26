# src/db/mapper/mapper.py
from abc import ABC, abstractmethod
import mysql.connector
from ...config import Config

class Mapper(ABC):
    """Base mapper class that handles database connection"""
    
    def __init__(self):
        self._cnx = None

    def _get_connection(self):
        if self._cnx is None:
            self._cnx = mysql.connector.connect(
                host=Config.MYSQL_HOST,
                user=Config.MYSQL_USER,
                password=Config.MYSQL_PASSWORD,
                database=Config.MYSQL_DB
            )
        return self._cnx

    def _close_connection(self):
        if self._cnx is not None:
            self._cnx.close()
            self._cnx = None