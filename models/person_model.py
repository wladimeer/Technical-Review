from utils.database import database

class Person(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    identification = database.Column(database.String(12))
    name = database.Column(database.String(25))
    lastname = database.Column(database.String(25))

    def __init__(self, identification, name, lastname):
        self.identification = identification
        self.name = name
        self.lastname = lastname

