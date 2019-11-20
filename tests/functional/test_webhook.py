from tests.helpers import sign_request
import json
import uuid


class TestEventWebhook:
    """
        Class that tests the integrations webhoo for our server.
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
        header = sign_request(security_event_payload, secret_key=uuid.uuid4().hex)
        header = {'X-Sqreen-Integrity': header}
        response = test_client.post('v1/webhook', data=json.dumps(request_body), headers=header,
                                    content_type='application/json')
        assert response.status_code == 401

    def test_invalid_header_pulse_event(self, test_client, pulse_event_payload):
        request_body = pulse_event_payload
        header = sign_request(pulse_event_payload, secret_key=uuid.uuid4().hex)
        header = {'X-Sqreen-Integrity': header}
        response = test_client.post('v1/webhook', data=json.dumps(request_body), headers=header,
                                    content_type='application/json')
        assert response.status_code == 401

    def test_invalid_header_play_book_event(self, test_client, playbook_event_payload):
        request_body = playbook_event_payload
        header = sign_request(playbook_event_payload, secret_key=uuid.uuid4().hex)
        header = {'X-Sqreen-Integrity': header}
        response = test_client.post('v1/webhook', data=json.dumps(request_body), headers=header,
                                    content_type='application/json')
        assert response.status_code == 401

    def test_invalid_json_request(self, test_client):
        request_body = {}
        header = sign_request(request_body)
        header = {'X-Sqreen-Integrity': header}
        response = test_client.post('v1/webhook', data=json.dumps(request_body), headers=header)
        assert response.status_code == 422
