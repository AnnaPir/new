from flask import Flask, render_template, request
import re
"""
Розробити фласк додаток, що містить одну сторінку-шаблон.
На цьому шаблоні має бути поле для введеня номеру телефону у
форматі +ХХХ YY NNNNNNN де Х- код країни, Y - код мобільного
оператора, N- номер абонента.

Після відправки номеру додаток має проаналізувати номер і на
цьому ж шаблоні відобразити наступне повідмлення:
Телефон (номер телефону) країна - (назва країни).

Країну визначати за кодом із номеру. Додаток повинен розрізняти мінімум 5 країн.
"""
app = Flask(__name__)


@app.route("/")
@app.route("/main", methods=["GET", "POST"])
def num_add():
    location = ""
    if request.method == "POST":
        num = request.form.get("Number")
        search = re.findall(r"[0-9]{1,3} \d\d \d{7}", num)
        if search:
            addres = "".join(search)
            addres = addres[0:3]
            number = "".join(search)
            number = number[6:15]
            print(number)
            location = "не визначена"
            if addres == "380":
                location = "Україна"
                print(f"Телефон {number} країна - Україна.")
            elif addres == "213":
                location = "Алжир"
                print(f"Телефон {number} країна - Алжир.")
            elif addres == "994":
                location = "Азербайджан"
                print(f"Телефон {number} країна - Азербайджан.")
            elif addres == "374":
                location = "Арменія"
                print(f"Телефон {number} країна - Арменія.")
            elif addres == "229":
                location = "Бенин"
                print(f"Телефон {number} країна - Бенин.")
            else:
                print("Такого региону не існує.")
        else:
            print("Не дійсний номер.")
    return render_template("index.html", location=location)


if __name__ == "__main__":
    app.run(debug=True)