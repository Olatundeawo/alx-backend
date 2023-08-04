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
def get_locale() -> str:
    """Getting the locale for a web page
    """
    query = request.query_string.decode('utf-8').split('&')
    query_table = dict(map(
        lambda x: (x if '=' in x else '{}='.format(x)).split('='), query
    ))
    if 'locale' in query_table:
        if query_table['locale'] in app.config['LANGUAGES']:
            return query_table['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def main() -> str:
    """ The home page
    """
    return (render_template('4-index.html'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)