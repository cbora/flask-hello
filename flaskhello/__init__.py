from flask import Flask
from flask_mongoengine import MongoEngine
from flask_login import LoginManager
import os

import sys
sys.path.append('..')

from application import application

#app = application.application
app = application

#app.config[''] = os.path.abspath(os.path.dirname(__file__))
#app.config['APPLICATION_ROOT'] = './flaskhello/'

import server
