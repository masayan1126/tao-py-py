#!/home/maasaablog/.local/share/virtualenvs/tao-pypy-gEOT-sr7/bin/python3.10

from flask import Flask, jsonify
from flask_cors import CORS
from packages.api.dataset import datasetfunc

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

CORS(app, resources={r"/tao-py-py/api/v1/*": {"origins": "*"}})


@app.route("/tao-py-py/api/v1/recipes", methods=["GET"])
def recipes1():
    recipes = datasetfunc()
    return jsonify({"recipe": recipes})


@app.route("/tao-py-py/api/v2/recipes", methods=["GET"])
def recipes2():
    recipes = datasetfunc()
    return jsonify({"recipe": recipes})


if __name__ == "__main__":
    app.run()
