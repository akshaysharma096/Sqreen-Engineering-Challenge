# -*- coding: utf-8 -*-
# Written by Akshay Sharma, <akshay.sharma09695@gmail.com>

import os
from flask import Flask
import sqreen
from flaskr.utils.logging import logger
from flaskr.config import SECURITY_HEADERS
from flaskr.v1.controller import v1


def create_app(test_config=None):
    """
        :param test_config: Config for the application
        :return: Instance of the flask app.
        """
    sqreen.start()
    app = Flask(__name__, instance_relative_config=True)
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

        # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def hello_world():
        return 'Hello World!'

    @app.after_request
    def apply_caching(response):

        """
        :param response: Incoming HTTP response for any of our incoming views/controllers
        :return: HTTP response with required headers added, for security.
        """
        for headers in SECURITY_HEADERS:
            header = headers['header']
            value = headers['value']
            response.headers[header] = value
        return response

    app.register_blueprint(v1, url_prefix='/v1')
    app.debug = False
    print(app.url_map)
    return app
