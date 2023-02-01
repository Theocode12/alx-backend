#!/usr/bin/env python3
"""Flask app"""

from flask import Flask, request, render_template
from flask_babel import Babel


class Config(object):
    """config class"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app, default_locale="en", default_timezone="UTC")


@babel.localeselector
def get_locale() -> str:
    """gets current locale"""
    return request.accept_language.best_match(app.config["LANGUAGES"])


@app.route("/", strict_slashes=True)
def index() -> str:
    """Index page"""
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run(debug=True)
