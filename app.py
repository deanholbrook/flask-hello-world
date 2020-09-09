"""Minimalist web app. Respond to any request with a cheery 'Hello World!' """
from flask import Flask, send_file

app = Flask(__name__)


# @app.route("/")
# def home():
#    return send_file('index.html')


@app.route("/health")
def health():
    """Special route for health check"""
    return "All is well"


@app.route("/", defaults={'path': ''})
@app.route("/<path:path>")
def catch_all(path):
    """Respond with HTML page"""
    return send_file('response.html')


if __name__ == "__main__":
    # By default, runs on localhost, port 5000.
    # Host and port can be modified with command line arguments.
    app.run()
