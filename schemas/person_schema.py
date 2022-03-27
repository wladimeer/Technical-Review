from utils.marshmallow import marshmallow

class PersonSchema(marshmallow.Schema):
    class Meta: fields = (
        'id', 'identification', 'name', 'lastname'
    )

person_schema = PersonSchema()
people_schema = PersonSchema(many=True)

