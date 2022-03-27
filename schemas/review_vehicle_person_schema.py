from utils.marshmallow import marshmallow

class ReviewVehiclePersonSchema(marshmallow.Schema):
    class Meta: fields = (
        'id', 'brand', 'model', 'patent', 'approved',
        'observations', 'identification', 'review_date',
        'lastname', 'name'
    )

review_vehicle_person_schema = ReviewVehiclePersonSchema()
reviews_vehicle_person_schema = ReviewVehiclePersonSchema(many=True)

