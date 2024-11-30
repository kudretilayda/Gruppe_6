import mysql.connector
import os

class DBConnector:
    """Database connector class for managing database connections"""
    
    @staticmethod
    def get_connection():
        """
        Creates and returns a database connection based on the environment
        Returns:
            mysql.connector.connection.MySQLConnection: Database connection object
        """
        try:
            # Check if running on Google App Engine
            if os.getenv('GAE_ENV', '').startswith('standard'):
                # Production environment (Google Cloud SQL)
                connection = mysql.connector.connect(
                    user=os.getenv('DB_USER'),
                    password=os.getenv('DB_PASS'),
                    host=os.getenv('DB_HOST'),
                    database=os.getenv('DB_NAME')
                )
            else:
                # Local development environment
                connection = mysql.connector.connect(
                    user='root',
                    password='root',
                    host='localhost',
                    database='digital_wardrobe'
                )
            return connection
        except mysql.connector.Error as error:
            print(f"Failed to connect to database: {error}")
            raise error