# -*- coding: utf-8 -*-
# Written by Akshay Sharma, <akshay.sharma09695@gmail.com>


import uuid
from functools import wraps

from flask import request, jsonify

from flaskr.utils.check_signature import signature_verification


def validate_incoming_request(f):
    """
    Function to validate an incoming request to our web-hook, by processing the request signature

    :param f: Function to be called if the request is authenticated
    :return: Returns the respective response codes based on the authentication process.
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        signature = request.headers.get('X-Sqreen-Integrity', str(uuid.uuid4()))
        if not signature_verification.check_signature(signature, request.get_data()):
            response = {'error': 'You need to authenticated to access this API.'}
            return jsonify(response), 401

        # Valid Input is an array of events.
        if not request.get_json() or not type(request.get_json()) is list:
            response = {'error': 'Unprocessable Entity'}
            return jsonify(response), 422
        return f(*args, **kwargs)

    return decorated_function
