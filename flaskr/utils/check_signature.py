# -*- coding: utf-8 -*-
# Written by Akshay Sharma, <akshay.sharma09695@gmail.com>


import hmac
import hashlib
import os
from flaskr.config import PYTHON_VERSION


class SqreenSignatureVerification:
    """
        Class to encapsulate the signature verification process for the incoming request from Sqreen
    """

    def __init__(self, signing_secret):
        self.signing_secret = signing_secret

    def _verify_signature(self, request_body, request_signature):
        """
        Helper function to check the signature of the incoming request

        :param request_body: Body of the request
        :param request_signature:
        :return: Boolean, True/False is the request valid or not.
        """
        request_hash = hmac.new(str.encode(self.signing_secret),
                                request_body,
                                hashlib.sha256).hexdigest()
        if hasattr(hmac, 'compare_digest'):
            # If the object does have an function of compare_digest
            if PYTHON_VERSION == 2:
                # Python 2 fix
                return hmac.compare_digest(bytes(request_hash), bytes(request_signature))
            else:
                return hmac.compare_digest(request_hash, request_signature)

        else:
            if len(request_hash) != len(request_signature):
                return False
            result = 0
            if isinstance(request_hash, bytes) and isinstance(request_signature, bytes):
                for x, y in zip(request_hash, request_signature):
                    result |= x ^ y
            else:
                for x, y in zip(request_hash, request_signature):
                    result |= ord(x) ^ ord(y)
            return result == 0

    def check_signature(self, request_signature, request_body):
        """

        :param request_signature: The integrity key received in the request headers
        :param request_body: Body of the request

        :return: Boolean, True/False is the request valid or not.
        """
        return self._verify_signature(request_body, request_signature)


secret_key = os.environ.get('SIGNATURE_KEY', '')
signature_verification = SqreenSignatureVerification(secret_key)
