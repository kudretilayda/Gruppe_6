import os
from dotenv import load_dotenv

load_dotenv()  # Lädt die Werte aus der .env-Datei

class Config:
    MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
    MYSQL_USER = os.getenv('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', 'kik2001duman123')
    MYSQL_DATABASE = os.getenv('MYSQL_DATABASE', 'digital_wardrobe')
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')


