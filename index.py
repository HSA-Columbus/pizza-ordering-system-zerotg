import sqlite3

from flask import *

app = Flask(__name__)


@app.route('/home', methods=('GET', 'POST'))
def home():
    if request.method == "POST":
        with sqlite3.connect("data") as conn:
            command = "INSERT INTO orders VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            list = []
            list.append(request.form['name'])
            list.append(request.form['address'])
            list.append(request.form['pizzatype'])
            list.append(request.form['pepper'])
            list.append(request.form['tomato'])
            list.append(request.form['pickle'])
            list.append(request.form['mushroom'])
            list.append(request.form['olive'])
            list.append(request.form['price'])
            list.append(request.form['quantity'])
            list.append(request.form['total'])
            list.append(request.form['calories'])
            conn.execute(command, list)
            conn.commit()

    return render_template("options.html")


@app.route('/check')
def check():
    return render_template("check.html")


@app.route('/')
def main():
    return render_template("home.html")


if __name__ == "__main__":
    app.run()
