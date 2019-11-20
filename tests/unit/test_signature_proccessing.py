import json
from uuid import uuid4

import pytest

from flaskr.utils.check_signature import signature_verification
from flaskr.utils.crypt import sign_request


class TestSignatureVerification:
    """
        Unit Tests to test, signature verification
    """
    @pytest.mark.parametrize('request_body',
                             [{"id": uuid4().hex, "data": {"name": "Akshay"}}, [{"id": uuid4().hex}, {"id": "1111"}]])
    def test_valid_signature(self, request_body):
        header = sign_request(request_body)
        request_body = json.dumps(request_body).encode('utf-8')
        assert signature_verification.check_signature(header, request_body) == True

    def test_valid_signature_for_security_event_payload(self, security_event_payload):
        header = sign_request(security_event_payload)
        request_body = json.dumps(security_event_payload).encode('utf-8')
        assert signature_verification.check_signature(header, request_body) == True

    def test_valid_signature_for_pulse_event_payload(self, pulse_event_payload):
        header = sign_request(pulse_event_payload)
        request_body = json.dumps(pulse_event_payload).encode('utf-8')
        assert signature_verification.check_signature(header, request_body) == True

    def test_valid_signature_for_playbook_event_payload(self, playbook_event_payload):
        header = sign_request(playbook_event_payload)
        request_body = json.dumps(playbook_event_payload).encode('utf-8')
        assert signature_verification.check_signature(header, request_body) == True
