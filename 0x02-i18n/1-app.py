#!/usr/bin/env python3
"""
Flask module
"""
from flask_babel import Babel
from config import Config
from flask import render_template

app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@app.route('/')
def main() -> str:
    """ The home page
    """
    return (render_template('0-index.html'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)