from flask import Flask
from flask_mongoengine import MongoEngine
from flask_login import LoginManager
import os

import sys
sys.path.append('..')

from application import application

#app = application.application
@application.route('/')
def h():
    return 'hello'


#import server
