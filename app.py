#!/home/maasaablog/.local/share/virtualenvs/tao-pypy-gEOT-sr7/bin/python3.10

from flask import Flask, jsonify

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False


@app.route("/", methods=["GET"])
def index():
    return jsonify({"recipe": "hoge"})


if __name__ == "__main__":
    app.run()
