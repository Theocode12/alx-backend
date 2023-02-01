#!/usr/bin/env python3
""" module's doc str """


from typing import List, Dict, Union, Sequence, Callable, Any
from flask_babel import Babel
from flask import Flask, render_template, g, request


app = Flask(__name__)
babel = Babel(app, default_locale='en', default_timezone='UTC')


class Config(object):
    """ config for babel """
    LANGUAGES = ['en', "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> Union[str, None]:
    """ override default fet_locale """
    locale = request.args.get('locale', None)
    if locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """ root path """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
    