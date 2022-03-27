from utils.marshmallow import marshmallow

class ReviewSchema(marshmallow.Schema):
    class Meta: fields = (
        'id', 'vehicle', 'approved', 'observations', 'manager', 'review_date'
    )

review_schema = ReviewSchema()
reviews_schema = ReviewSchema(many=True)

