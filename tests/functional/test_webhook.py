import json
from uuid import uuid4

import pytest

from flaskr.utils.crypt import sign_request


class TestEventWebhook:
    """
        Functional tests, that tests the notification webhook.
    """

    def test_correct_security_event(self, test_client, security_event_payload):
        request_body = security_event_payload
        header = sign_request(security_event_payload)
        header = {'X-Sqreen-Integrity': header}
        response = test_client.post('v1/webhook', data=json.dumps(request_body), headers=header,
                                    content_type='application/json')
        assert response.status_code == 200

    def test_pulse_event(self, test_client, pulse_event_payload):
        request_body = pulse_event_payload
        header = sign_request(pulse_event_payload)
        header = {'X-Sqreen-Integrity': header}
        response = test_client.post('v1/webhook', data=json.dumps(request_body), headers=header,
                                    content_type='application/json')
        assert response.status_code == 200

    def test_play_book_event(self, test_client, playbook_event_payload):
        request_body = playbook_event_payload
        header = sign_request(playbook_event_payload)
        header = {'X-Sqreen-Integrity': header}
        response = test_client.post('v1/webhook', data=json.dumps(request_body), headers=header,
                                    content_type='application/json')
        assert response.status_code == 200

    def test_invalid_header_security_event(self, test_client, security_event_payload):
        request_body = security_event_payload
        header = sign_request(security_event_payload, secret_key=uuid4().hex)
        header = {'X-Sqreen-Integrity': header}
        response = test_client.post('v1/webhook', data=json.dumps(request_body), headers=header,
                                    content_type='application/json')
        assert response.status_code == 401

    def test_invalid_header_pulse_event(self, test_client, pulse_event_payload):
        request_body = pulse_event_payload
        header = sign_request(pulse_event_payload, secret_key=uuid4().hex)
        header = {'X-Sqreen-Integrity': header}
        response = test_client.post('v1/webhook', data=json.dumps(request_body), headers=header,
                                    content_type='application/json')
        assert response.status_code == 401

    def test_invalid_header_play_book_event(self, test_client, playbook_event_payload):
        request_body = playbook_event_payload
        header = sign_request(playbook_event_payload, secret_key=uuid4().hex)
        header = {'X-Sqreen-Integrity': header}
        response = test_client.post('v1/webhook', data=json.dumps(request_body), headers=header,
                                    content_type='application/json')
        assert response.status_code == 401

    def test_empty_json_request(self, test_client):
        request_body = {}
        header = sign_request(request_body)
        header = {'X-Sqreen-Integrity': header}
        response = test_client.post('v1/webhook', data=json.dumps(request_body), headers=header)
        assert response.status_code == 422

    @pytest.mark.parametrize('request_body',
                             [{"id": uuid4().hex, "data": {"name": "Akshay"}}, {"id": uuid4().hex}, {"id": "1111"}])
    def test_empty_json_request(self, test_client, request_body):
        header = sign_request(request_body)
        header = {'X-Sqreen-Integrity': header}
        response = test_client.post('v1/webhook', data=json.dumps(request_body), headers=header,
                                    content_type='application/json')
        assert response.status_code == 422
