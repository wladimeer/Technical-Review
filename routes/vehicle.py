from utils.database import database
from schemas.vehicle_schema import vehicle_schema, vehicles_schema
from flask import Blueprint, jsonify, request
from models.vehicle_model import Vehicle
from operator import itemgetter

vehicle = Blueprint('vehicle', __name__)

@vehicle.route('/')
def Principal():
    return VehicleList()

@vehicle.route('/vehicle-list', methods = ['GET'])
def VehicleList():
    try:
        query = Vehicle.query.all()
        vehicle_list = vehicles_schema.dump(query)

        result = {'state': 1, 'message': 'Data obtained', 'data': vehicle_list}
        return jsonify(result)

    except Exception as exception:
        result = {'state': 0, 'message': exception.args[0], 'data': None}
        return jsonify(result)

@vehicle.route('/new-vehicle', methods = ['POST'])
def NewVehicle():
    try:
        vehicle = request.get_json()

        brand, model, patent = itemgetter('brand', 'model', 'patent')(vehicle)
        year, owner = itemgetter('year', 'owner')(vehicle)

        vehicle_data = Vehicle(brand, model, patent, year, owner)

        database.session.add(vehicle_data)
        database.session.commit()

        vehicle['id'] = vehicle_data.id

        result = {'state': 1, 'message': 'Added vehicle', 'data': vehicle}
        return jsonify(result)

    except Exception as exception:
        result = {'state': 0, 'message': exception.args[0], 'data': None}
        return jsonify(result)

