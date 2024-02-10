from flask import Flask, render_template, request, redirect, send_file
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.db"  # database configuration
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)  # binding DB and Flask App


class User(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    points = db.Column(db.String(50), nullable=False)
    authorization = db.Column(db.String(40), nullable=False)


@app.route("/")
def index():
    users = User.query.all()
    print(users)
    return render_template("home.html", users=users)


@app.route("/recall")
def recall1():
    return render_template("recall.html")


@app.route("/add_user", methods=["POST"])
def add_user():
    name = request.form["name"]
    surname = request.form["surname"]
    email = request.form["email"]
    points = request.form["points"]
    authorization = request.form["authorization"]
    new_user = User(
        name=name,
        surname=surname,
        email=email,
        points=points,
        authorization=authorization
    )
    db.session.add(new_user)
    db.session.commit()
    return redirect("/")


@app.route("/del_st", methods=["POST"])
def del_st():
    delnum = request.form["delnum"]
    print(delnum)
    db.session.delete(delnum)
    db.session.commit()
    return redirect("/")


def rec(rec):
    return rec


if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Создаем таблицу в контексте приложения
    app.run(debug=True)