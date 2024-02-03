from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def index():
    return render_template("home.html")


@app.route("/merzlyak")
def merzlyak():
    return render_template("merzlyak.html")


@app.route("/zabolotnio")
def zabolotnio():
    return render_template("zabolotnio.html")


if __name__ == "__main__":
    app.run(debug=True)