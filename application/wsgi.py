from flask import Flask

application = Flask(__name__)

@app.route("/api/")
def hello_world():
    return "<p>Hello, World!</p>"
