from flask import Flask
from flask_mongoengine import MongoEngine
from flask_login import LoginManager
import os


application = app = Flask(__name__)



@application.route('/')
def index():
    return 'hello world'
