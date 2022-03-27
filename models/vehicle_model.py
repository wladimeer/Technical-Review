from utils.database import database

class Vehicle(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    brand = database.Column(database.String(25))
    model = database.Column(database.String(25))
    patent = database.Column(database.String(12))
    year = database.Column(database.Integer)
    owner = database.Column(database.Integer, database.ForeignKey('person.id'))

    def __init__(self, brand, model, patent, year, owner):
        self.brand = brand
        self.model = model
        self.patent = patent
        self.year = year
        self.owner = owner

