from flask import *

app = Flask(__name__)


@app.route('/home')
def home():
    return render_template("options.html")


@app.route('/check')
def check():
    return render_template("check.html")


@app.route('/')
def main():
    return render_template("home.html")


if __name__ == "__main__":
    app.run()
