# -*- coding: utf-8 -*-
# Written by Akshay Sharma, <akshay.sharma09695@gmail.com>

import hashlib
import hmac
import json
import os


def sign_request(request_body, secret_key=None):
    """
    Helper function to sign a variable/request object

    :param request_body: Request body to sign
    :param secret_key: Optional parameter, used to override the default signing key
    :return: Signed value of the request using the secret key
    """
    request_body = json.dumps(request_body).encode('utf-8')
    if not secret_key:
        secret_key = os.environ.get('SIGNATURE_KEY', '')

    secret_key = secret_key.encode('utf-8')
    return hmac.new(secret_key, request_body, hashlib.sha256).hexdigest()
