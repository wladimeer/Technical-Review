from utils.database import database
from models.review_model import Review
from schemas.review_schema import review_schema, reviews_schema
from schemas.review_vehicle_person_schema import reviews_vehicle_person_schema
from schemas.review_vehicle_person_schema import review_vehicle_person_schema
from flask import Blueprint, jsonify, request
from models.vehicle_model import Vehicle
from models.person_model import Person
from operator import itemgetter

review = Blueprint('review', __name__)

@review.route('/review-list', methods = ['GET'])
def ReviewList():
    try:
        query = Review.query.all()
        review_list = reviews_schema.dump(query)

        result = {'state': 1, 'message': 'Data obtained', 'data': review_list}
        return jsonify(result)

    except Exception as exception:
        result = {'state': 0, 'message': exception.args[0], 'data': None}
        return jsonify(result)

@review.route('/new-review', methods = ['POST'])
def NewReview():
    try:
        review = request.get_json()

        vehicle, approved, observations = itemgetter('vehicle', 'approved', 'observations')(review)
        manager, review_date = itemgetter('manager', 'review_date')(review)

        review_data = Review(vehicle, approved, observations, manager, review_date)

        database.session.add(review_data)
        database.session.commit()

        review['id'] = review_data.id

        result = {'state': 1, 'message': 'Added review', 'data': review}
        return jsonify(result)

    except Exception as exception:
        result = {'state': 0, 'message': exception.args[0], 'data': None}
        return jsonify(result)

@review.route('/find-reviews/<string:patent>', methods = ['GET'])
def FindReviews(patent):
    try:
        vehicle = Vehicle.query.filter_by(patent=patent).first()

        if None not in [vehicle]:
            query = (
                database.session.query(
                    Review.id,
                    Vehicle.brand,
                    Vehicle.model,
                    Vehicle.patent,
                    Review.approved,
                    Review.observations,
                    Person.identification,
                    Review.review_date,
                    Person.lastname,
                    Person.name
                )
                .select_from(Review).join(Vehicle).join(Person)
                .filter(Vehicle.patent==vehicle.patent).all()
            )

            review_vehicle_person_list = reviews_vehicle_person_schema.dump(query)
            result = {'state': 1, 'message': 'Data obtained', 'data': review_vehicle_person_list}

        else:
            result = {'state': 2, 'message': 'Vehicle not found', 'data': None}

        return jsonify(result)

    except Exception as exception:
        result = {'state': 0, 'message': exception.args[0], 'data': None}
        return jsonify(result)

