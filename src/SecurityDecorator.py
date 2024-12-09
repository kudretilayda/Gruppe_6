from flask import request
from google.auth.transport import requests
import google.oauth2.id_token

from server.Administration import Administration

def secured(funkction):
    firebase_request_adapter = requests.Request()
    