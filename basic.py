from flask import render_template, Flask


app = Flask(__name__)


@app.route("/home")
def home():
    return "Hello world"


@app.route("/<name>")
def basic(name):
    return render_template("basic.html", name=name)


@app.route("/pics")
@app.route("/")
def pics():
    pics = ["dropsCity.jpg", "kart.jpg", "splash.jpg"]
    return render_template("pics.html", pics=pics)


if __name__ == "main":
    app.run()
