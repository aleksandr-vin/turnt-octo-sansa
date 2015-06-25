from flask import Flask
from flask.ext import webcache

app = Flask(__name__)
app.config.from_object('config')

from app import views

#webcache.easy_setup(app)
