from utils.marshmallow import marshmallow

class ReviewTypeSchema(marshmallow.Schema):
    class Meta: fields = (
        'id', 'name'
    )

review_type_schema = ReviewTypeSchema()
review_types_schema = ReviewTypeSchema(many=True)

