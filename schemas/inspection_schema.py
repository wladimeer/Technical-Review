from utils.marshmallow import marshmallow

class InspectionSchema(marshmallow.Schema):
    class Meta: fields = (
        'id', 'review', 'type', 'observations', 'state', 'manager'
    )

inspection_schema = InspectionSchema()
inspections_schema = InspectionSchema(many=True)

