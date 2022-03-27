from utils.marshmallow import marshmallow

class VehicleSchema(marshmallow.Schema):
    class Meta: fields = (
        'id', 'brand', 'model', 'patent', 'year', 'owner'
    )

vehicle_schema = VehicleSchema()
vehicles_schema = VehicleSchema(many=True)

