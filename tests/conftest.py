# -*- coding: utf-8 -*-
# Written by Akshay Sharma, <akshay.sharma09695@gmail.com>

import datetime
import uuid
import pytest
from flaskr import create_app


@pytest.fixture(scope="module")
def security_event_payload():
    request_body = [{
        "sqreen_payload_type": "security_event",
        "application_account_account_keys": [
            {
                "name": "email",
                "value": "jeff45@harrell.com"
            }
        ],
        "application_id": "5dd058775c3feb0021c0bb43",
        "application_name": "Demo app",
        "environment": "production",
        "date_occurred": "2016-12-21T07:22:32.732000+00:00",
        "event_category": "authentication",
        "event_id": "587b234e4891d57c1bf5c8c9",
        "event_kind": "auth_tor_tentative",
        "url": "https://my.sqreen.com/application/d8b47501fad44fb28d09967e1f1b09a258d85f4ba5d44e759b886f9663e7cf01/events/587b234e4891d57c1bf5c8c9",
        "humanized_description": "Connection to jeff45@harrell.com from TOR (135.96.171.118)",
        "ips": [
            {
                "address": "135.96.171.118",
                "date_resolved": "2017-01-15T07:22:54.573000+00:00",
                "geo": {
                    "city": "Sag",
                    "code": "ROU",
                    "point": [
                        21.283300399780273,
                        46.04999923706055
                    ]
                },
                "is_tor": True
            }
        ]
    }]
    return request_body


@pytest.fixture(scope="module")
def pulse_event_payload():
    request_body = [{
        "humanized_geos": "Paris, France",
        "pulse_category": None,
        "humanized_accounts": "user@example.com",
        "date_ended": None,
        "application_id": "5dd058775c3feb0021c0bb43",
        "blocked": True,
        "url": "https://my.sqreen.com/application/5dd058775c3feb0021c0bb43/pulses/5dd5b454e56c7e0024169b4b",
        "date_started": "2019-11-20T21:47:00.090825+00:00",
        "sqreen_payload_type": "pulse",
        "incidents_count": 0,
        "user_agents_count": 0,
        "environment": "production",
        "accounts_count": 0,
        "humanized_title": "Massive account takeover attempts on user@example.com",
        "application_name": "APPLICATION",
        "ip_addresses_count": 0,
        "id": "5dd5b454e56c7e0024169b4b",
        "pulse_genre": "account_takeover"
    }]
    return request_body


@pytest.fixture(scope="module")
def playbook_event_payload():
    request_body = [{
        "sqreen_payload_type": "security_response",
        "id": None,
        "date_created": "2019-11-20T21:47:00.097178+00:00",
        "properties": {
            "ips": [
                {
                    "ip_cidr": "127.0.0.1"
                }
            ],
            "user_identifiers": [
                "sqreen@example.com"
            ]
        },
        "application": {
            "name": "APPLICATION",
            "id": "5dd058775c3feb0021c0bb43",
            "environment": "production"
        },
        "playbook": {
            "id": "5dd5b454e56c7e0024169b4c",
            "name": "Test Playbook"
        }
    }]
    return request_body


@pytest.fixture(scope="module")
def test_client():
    flask_app = create_app()
    testing_client = flask_app.test_client()
    ctx = flask_app.app_context()
    ctx.push()
    yield testing_client
    ctx.pop()


@pytest.fixture(scope="module")
def sample_notification(security_event_payload):
    notification = {
        'id': uuid.uuid4().hex,
        'processed_at': datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat(),
        'notification': security_event_payload[0]
    }
    return notification


@pytest.fixture(scope="module")
def sample_internal_issue(security_event_payload):
    payload = security_event_payload[0]
    alert = {key: payload[key] for key in
             ['event_kind', 'humanized_description', 'event_category', 'date_occurred', 'environment',
              'url']}
    return alert
