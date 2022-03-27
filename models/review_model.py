from utils.database import database

class Review(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    vehicle = database.Column(database.Integer, database.ForeignKey('vehicle.id'))
    approved = database.Column(database.Integer)
    observations = database.Column(database.String(100))
    manager = database.Column(database.Integer, database.ForeignKey('person.id'))
    review_date = database.Column(database.Date)

    def __init__(self, vehicle, approved, observations, manager, review_date):
        self.vehicle = vehicle
        self.approved = approved
        self.observations = observations
        self.manager = manager
        self.review_date = review_date

