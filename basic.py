from flask import request, render_template, Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello world %s" % request.method


@app.route("/<name>")
def basic(name):
    return render_template("basic.html", name=name)


@app.route("/pics")
def pics():
    return render_template("pics.html")

if __name__ =="main":
    app.run()
