from utils.database import database

class Inspection(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    review = database.Column(database.Integer, database.ForeignKey('review.id'))
    type = database.Column(database.Integer, database.ForeignKey('review_type.id'))
    observations = database.Column(database.String(100))
    state = database.Column(database.Integer)
    manager = database.Column(database.Integer, database.ForeignKey('person.id'))

    def __init__(self, review, type, observations, state, manager):
        self.review = review
        self.type = type
        self.observations = observations
        self.state = state
        self.manager = manager

