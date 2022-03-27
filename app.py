from flask import Flask, jsonify
from routes.review import review
from routes.vehicle import vehicle
from routes.inspection import inspection
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from utils.database import database
from operator import itemgetter
from flask_cors import CORS
from config import Config

config_object = itemgetter('development')(Config)

app = Flask(__name__)
app.config.from_object(config_object)
Marshmallow(app)
SQLAlchemy(app)
CORS(app)

def ResourceNotFound(self):
    return jsonify('Resource not found')

with app.app_context():
    database.create_all()

if __name__ == '__main__':
    app.register_error_handler(404, ResourceNotFound)
    app.register_blueprint(inspection)
    app.register_blueprint(vehicle)
    app.register_blueprint(review)
    app.run()

