import sqlite3

from flask import *

app = Flask(__name__)


@app.route('/home', methods=('GET', 'POST'))
def home():
    if request.method == "POST":
        with sqlite3.connect("data") as conn:
            command = "INSERT INTO orders VALUES(?, ?, ?, ?, ?, ?, ?, ?)"
            list = []
            additions = ""

            list.append(request.form['name'])
            list.append(request.form['address'])
            list.append(request.form['pizzatype'])

            additions += "Green Pepper, " if request.form.get("pepper", None) is not None else ""
            additions += "Tomato, " if request.form.get("tomato", None) is not None else ""
            additions += "Pickle, " if request.form.get("pickle", None) is not None else ""
            additions += "Mushroom, " if request.form.get("mushroom", None) is not None else ""
            additions += "Olive, " if request.form.get("olive", None) is not None else ""

            list.append(additions)
            list.append(request.form['quantity'])
            list.append(request.form['price'])
            list.append(request.form['calories'])
            list.append(request.form['total'])
            conn.execute(command, list)
            conn.commit()

    return render_template("options.html")


@app.route('/check')
def check():
    with sqlite3.connect("data") as conn:
        command = "SELECT * FROM orders"
        table = conn.execute(command)
        list = table.fetchall()
        return render_template("check.html", list=list)


@app.route('/')
def main():
    return render_template("home.html")


if __name__ == "__main__":
    app.run()
