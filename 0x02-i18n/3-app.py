#!/usr/bin/env python3
"""
Flask module
"""
from flask import request, Flask, render_template
from flask_babel import Babel
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def main() -> str:
    """ The home page
    """
    return (render_template('3-index.html'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
