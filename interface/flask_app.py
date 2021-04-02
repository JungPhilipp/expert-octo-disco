from flask import Flask, render_template, jsonify

from plz_utils import plz_lookup, city_to_plzs
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/plz/<plz>')
def center_on_plz(plz):
    try:
        res = plz_lookup[str(plz)]
    except KeyError:
        res = None
    return res


@app.route('/city/<city>')
def highlight_city(city: str):
    try:
        plzs = city_to_plzs[city.lower()]
        res = jsonify([plz_lookup[str(plz)] for plz in plzs])
    except KeyError:
        res = None
    return res
