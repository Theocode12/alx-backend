#!/usr/bin/env python3
"""Flask app"""

from flask import Flask, request, render_template
from flask_babel import Babel, _


class Config(object):
    LANGUAGES = ["en", "fr"]


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_locale():
    lang = request.args.get("locale")
    if lang and lang in Config.LANGUAGES:
        return lang
    return request.accept_languages.best_match(app.config["LANGUAGES"])


babel.init_app(app, locale_selector=get_locale)


@app.route("/")
def index():
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(debug=True)
