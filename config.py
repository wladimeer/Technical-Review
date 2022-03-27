import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class DevelopmentConfig:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    TESTING = False

Config = {"development": DevelopmentConfig}

