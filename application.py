from flask import Flask
import os


application = Flask(__name__, static_folder='./flaskhello/static', template_folder='./flaskhello/templates')


from flaskhello import *
