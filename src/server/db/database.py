import mysql.connector
from mysql.connector import Error, pooling
from typing import Optional, Dict, Any
from config.config import Config
import logging

class DatabaseConnection:
    """Database connection handler with connection pooling"""
    
    _instance: Optional['DatabaseConnection'] = None
    _pool: Optional[pooling.MySQLConnectionPool] = None

    def __init__(self):
        """Initialize the database connection pool"""
        if not DatabaseConnection._pool:
            try:
                pool_config = {
                    **Config.get_database_config(),
                    'pool_name': 'digital_wardrobe_pool',
                    'pool_size': 5,
                    'pool_reset_session': True
                }
                DatabaseConnection._pool = mysql.connector.pooling.MySQLConnectionPool(**pool_config)
                logging.info("Database connection pool created successfully")
            except Error as e:
                logging.error(f"Error creating database connection pool: {e}")
                raise

    @classmethod
    def get_instance(cls) -> 'DatabaseConnection':
        """Get singleton instance of DatabaseConnection"""
        if not cls._instance:
            cls._instance = DatabaseConnection()
        return cls._instance

    def get_connection(self):
        """Get a connection from the pool with context manager support"""
        class ConnectionContextManager:
            def __init__(self, pool):
                self.pool = pool
                self.conn = None
                self.cursor = None

            def __enter__(self):
                self.conn = self.pool.get_connection()
                self.cursor = self.conn.cursor(dictionary=True)
                return self.conn, self.cursor

            def __exit__(self, exc_type, exc_val, exc_tb):
                if self.cursor:
                    self.cursor.close()
                if self.conn:
                    self.conn.close()

        return ConnectionContextManager(DatabaseConnection._pool)

    def execute_query(self, query: str, params: tuple = None) -> Dict[str, Any]:
        """Execute a query and return results"""
        with self.get_connection() as (conn, cursor):
            try:
                cursor.execute(query, params or ())
                if cursor.with_rows:
                    result = cursor.fetchall()
                else:
                    result = {"affected_rows": cursor.rowcount}
                conn.commit()
                return result
            except Error as e:
                conn.rollback()
                logging.error(f"Error executing query: {e}")
                raise

    def execute_many(self, query: str, params: list) -> Dict[str, Any]:
        """Execute multiple queries with different parameters"""
        with self.get_connection() as (conn, cursor):
            try:
                cursor.executemany(query, params)
                conn.commit()
                return {"affected_rows": cursor.rowcount}
            except Error as e:
                conn.rollback()
                logging.error(f"Error executing multiple queries: {e}")
                raise