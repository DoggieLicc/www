from flask import Flask, request

application = Flask(__name__)

@application.route("/api/test")
def hello_world():
    return "<p>Hello, World!</p>"

@application.route("/api/ip")
def get_ip():
	return f"<h1>Your IP is: {request.remote_addr}</h1>"
