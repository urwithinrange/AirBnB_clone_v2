#!/usr/bin/python3
"""start a Flask web application"""

from flask import Flask
from models import storage
from flask import render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """return hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_v2():
    """return only HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """return C followed by a stream"""
    return "C {}".format(text.replace('_', ' '))


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """return Python is <text>"""
    return "Python {}".format(text.replace('_', ' '))


@app.route("/number/<int:n>", strict_slashes=False)
def gimmenumbers(n):
    """return number only if an int"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def gimmenumtemplate(n):
    """return HTML only if n is an integer"""
    return render_template("5-number.html", number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    """
    return HTML display when n is integer and define odd or even
    """
    return render_template('6-number_odd_or_even.html', number=n)


@app.teardown_appcontext
def td_app(exception=None):
    """
    After each request
    remove the current SQLAlchemy Session
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """display a HTML page"""
    states = list(storage.all('State').values())
    st_list = []
    for k, v in states:
        st_list.append((parse_id(k), v.name))
    st_list.sort(key=lambda tup: tup[0])
    return render_template("7-states_list.html", state_dict=result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
