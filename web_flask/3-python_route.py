#!/usr/bin/python3
"""
python3 flask run
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """return hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_v2():
    """return only HBNB"""
    return "HBNB"


@app.route("/C/<text>", strict_slashes=False)
def c_text():
    """return C followed by a stream"""
    return "C {}".format(text.replace('_', ' '))


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """return Python is <text>"""
    return "Python {}".format(text.replace('_', ' '))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
