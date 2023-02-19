from flask import Flask

application = Flask(__name__)

@application.route("/api/")
def hello_world():
    return "<p>Hello, World!</p>"
