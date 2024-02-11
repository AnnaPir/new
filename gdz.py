from flask import Flask, render_template, request, redirect, send_file
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.db"  # database configuration
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)  # binding DB and Flask App


class Student(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    points = db.Column(db.String(50), nullable=False)
    authorization = db.Column(db.String(40), nullable=False)


@app.route("/")
def index():
    students = Student.query.all()
    print(students)
    return render_template("home.html", students=students)


@app.route("/recall")
def recall1():
    return render_template("recall.html")


@app.route("/add_student", methods=["POST"])
def add_student():
    name = request.form["name"]
    surname = request.form["surname"]
    email = request.form["email"]
    points = request.form["points"]
    authorization = request.form["authorization"]
    new_student = Student(
        name=name,
        surname=surname,
        email=email,
        points=points,
        authorization=authorization
    )
    db.session.add(new_student)
    db.session.commit()
    return redirect("/")


@app.route("/del_st", methods=["POST"])
def del_st():
    student_id = int(request.form["student_id"])
    print(student_id)
    student = Student.query.get(student_id)
    message = f"Student with ID {student_id} wasn`t found"
    if student:
        db.session.delete(student)
        db.session.commit()
        message = f"Student with ID {student_id} has been removed"
    students = Student.query.all()
    return render_template("home.html",
                           students=students,
                           message=message)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Создаем таблицу в контексте приложения
    app.run(debug=True)