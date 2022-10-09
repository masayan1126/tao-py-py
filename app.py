from flask import Flask

app = Flask(__name__)


@app.route("/tweet", methods=["GET"])
def get_tweet():
    return "Success a Tweet!\n"


if __name__ == "__main__":
    app.run()
