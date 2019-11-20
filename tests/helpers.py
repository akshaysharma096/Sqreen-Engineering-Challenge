import os
import hmac
import hashlib
import json
from flaskr.config import SLACK_BACKEND


def sign_request(request_body, secret_key=None):
    request_body = json.dumps(request_body).encode('utf-8')
    if not secret_key:
        secret_key = os.environ.get('SIGNATURE_KEY', '')

    secret_key = secret_key.encode('utf-8')
    return hmac.new(secret_key, request_body, hashlib.sha256).hexdigest()


def get_sample_publication_backend():
    return SLACK_BACKEND
