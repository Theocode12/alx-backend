#!/usr/bin/env python3
""" Flask App"""

from flask import Flask, request, render_template
from flask_babel import Babel


class Config(object):
    LANGUAGES = ["en", "fr"]


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route("/")
def index():
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(debug=True)