from utils.database import database

class ReviewType(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(25))

    def __init__(self, name):
        self.name = name

