from utils.database import database
from models.inspection_model import Inspection
from schemas.inspection_schema import inspection_schema, inspections_schema
from models.review_type_model import ReviewType
from flask import Blueprint, jsonify, request
from operator import itemgetter

inspection = Blueprint('inspection', __name__)

@inspection.route('/inspection-list', methods = ['GET'])
def Inspections():
    try:
        query = Inspection.query.all()
        inspection_list = inspections_schema.dump(query)

        result = {'state': 1, 'message': 'Data obtained', 'data': inspection_list}
        return jsonify(result)

    except Exception as exception:
        result = {'state': 0, 'message': exception.args[0], 'data': None}
        return jsonify(result)

@inspection.route('/new-inspection', methods = ['POST'])
def NewInspection():
    try:
        inspection = request.get_json()

        review, type, observations = itemgetter('review', 'type', 'observations')(inspection)
        state, manager = itemgetter('state', 'manager')(inspection)

        inspection_data = Inspection(review, type, observations, state, manager)

        database.session.add(inspection_data)
        database.session.commit()

        inspection['id'] = inspection_data.id

        result = {'state': 1, 'message': 'Added inspection', 'data': inspection}
        return jsonify(result)

    except Exception as exception:
        result = {'state': 0, 'message': exception.args[0], 'data': None}
        return jsonify(result)

@inspection.route('/delete-inspection/<int:id>', methods = ['DELETE'])
def DeleteInspection(id):
    try:
        inspection = Inspection.query.filter_by(id=id).first()

        if None not in [inspection]:
            database.session.delete(inspection)
            database.session.commit()

            inspection = inspection_schema.dump(inspection)

            result = {'state': 1, 'message': 'Deleted inspection', 'data': inspection}

        else:
            result = {'state': 2, 'message': 'Inspection not found', 'data': None}

        return jsonify(result)

    except Exception as exception:
        result = {'state': 0, 'message': exception.args[0], 'data': None}
        return jsonify(result)

