# https://flask.palletsprojects.com/en/2.2.x/quickstart/#a-minimal-application

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, Dit is van Orio!</p>"
