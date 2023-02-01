#!/usr/bin/env python3
"""Flask app"""

from flask import Flask, request, render_template
from flask_babel import Babel, _


class Config(object):
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app, default_locale="en", default_timezone="UTC")


@babel.localeselector
def get_locale():
    """Returns current locale"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


babel.init_app(app, locale_selector=get_locale)


@app.route("/")
def index():
    """Index page"""
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run(debug=True)
