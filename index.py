from flask import *

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("options.html")


if __name__ == "__main__":
    app.run()
