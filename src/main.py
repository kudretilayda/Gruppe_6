from flask import Flask, request, g
from flask_cors import CORS
from flask_restx import Api, Resource, fields
from logging.handlers import RotatingFileHandler
from functools import wraps
import logging
import time
import os
import traceback

from src.server.Admin import Administration
from src.server.bo.User import User
from src.server.bo.Wardrobe import Wardrobe
from src.server.bo.Style import Style
from src.server.bo.Outfit import Outfit
from src.server.bo.ClothingItem import ClothingItem
from src.server.bo.ClothingType import ClothingType
from src.server.bo.Constraints import ConstraintRule, BinaryConstraint, UnaryConstraint,CardinalityConstraint, MutexConstraint, ImplicationConstraint
from src.SecurityDecorator import secured


# Logging Setup
def setup_logging():
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    logger = logging.getLogger('digital_wardrobe')
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        '%(asctime)s - [%(levelname)s] - %(message)s'
    )

    # App logs
    file_handler = RotatingFileHandler(
        os.path.join(log_dir, 'app.log'),
        maxBytes=1024 * 1024,
        backupCount=5
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


# Performance Monitoring Decorator
def monitor_performance(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        start_time = time.time()
        try:
            result = f(*args, **kwargs)
            duration = time.time() - start_time
            logging.getLogger('digital_wardrobe').info(
                f"Endpoint {f.__name__} completed in {duration:.2f}s"
            )
            return result
        except Exception as e:
            logging.getLogger('digital_wardrobe').error(
                f"Error in {f.__name__}: {str(e)}"
            )
            raise

    return decorated_function


# Initialize Flask app
app = Flask(__name__)
logger = setup_logging()

# Enable CORS
CORS(app, supports_credentials=True, resources=r'/wardrobe/*')

# Create API object
api = Api(app, version='1.0', title='Digital Wardrobe API',
          description='An API for managing a digital wardrobe.')

# Original namespace and models remain the same
wardrobe_ns = api.namespace('wardrobe', description='Digital Wardrobe functionalities')

# Original model definitions remain the same
bo = api.model('BusinessObject', {
    'id': fields.String(attribute='_id', description='Unique identifier'),
})


# [Rest of the model definitions remain the same...]

# Add request logging
@app.before_request
def before_request():
    g.start_time = time.time()
    logger.info(f"Request: {request.method} {request.url}")


@app.after_request
def after_request(response):
    duration = time.time() - g.start_time
    logger.info(f"Response: Status {response.status_code} in {duration:.2f}s")
    return response


# Example of adding monitoring to an endpoint while keeping original structure
@wardrobe_ns.route('/user')
@wardrobe_ns.response(500, 'Server-Error')
class UserListOperations(Resource):
    @wardrobe_ns.marshal_list_with(User)
    @secured
    @monitor_performance
    def get(self):
        """Get all users"""
        try:
            adm = Administration()
            users = adm.get_all_user()
            return users
        except Exception as e:
            logger.error(f"Error getting users: {str(e)}")
            return {'error': 'Internal server error'}, 500


# [Rest of the endpoints remain the same structure but with added monitoring decorator...]

if __name__ == '__main__':
    app.run(debug=True)