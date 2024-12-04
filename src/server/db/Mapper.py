from abc import ABC, abstractmethod
import os
from server.db.database import MySQLConnector
from typing import List, Optional
import mysql.connector as connector

class Mapper(ABC):
    def __init__(self):
        self._cnx = None


        """Wenn wir uns in der Cloud befinden, wird diese Verbindung genutzt"""
        if os.getenv('GAE_ENV', '').startswith('standard'):
            self._cnx = connector.connect(user='demo', password='demo',
                                          unix_socket='/cloudsql/smartfridge-app-428309:europe-west3:smartfridge',
                                          database='Sopra')

        else:
            """Sollten wir uns Lokal aufhalten, wird diese Verbindung genutzt"""
            self._cnx = connector.connect(user='root', password='9902',
                              host='localhost',
                              database='sopra')


        return self



    def __exit__(self, exc_type, exc_val, exc_tb):
        """Verbindung mit der Datenbank trennen"""
        if exc_type or exc_val or exc_tb:
            self._cnx.rollback()
        else:
            self._cnx.commit()
        self._cnx.close()