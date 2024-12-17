from flask import request
from google.auth.transport import requests
import google.oauth2.id_token

from src.server.Admin import Administration

def secured(function):
    firebase_request_adapter = requests.Request()
    