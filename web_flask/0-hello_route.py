#!/usr/bin/python3
"""flask app hosts and ports"""
from flask import Flask


app = Flask(__name__)


@app.route("/airbnb-onepage/", strict_slashes=False)
def hello_hbnb():
    """hello hbnb func"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
