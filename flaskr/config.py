# -*- coding: utf-8 -*-
# Written by Akshay Sharma, <akshay.sharma09695@gmail.com>


import sys
import os

PYTHON_VERSION = sys.version_info[0]

# Setting up the backend to automatically help process task asynchronously.
CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'amqp://127.0.0.1:5672')
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'amqp://127.0.0.1:5672')
APPLICATION_ID = os.environ.get('SCREEN_APPLICATION_ID', None)

# Tuple are immutable data-types, good for security.
# For adding and removing backend we need to change this and our app will behave automatically
RABBITMQ_BACKEND = 'SQREEN_APP.BACKENDS.RABBITMQ'
SLACK_BACKEND = 'SQREEN_APP.BACKENDS.SLACK'
SMS_BACKEND = 'SQREEN_APP.BACKENDS.SMS'
EMAIL_BACKEND = 'SQREEN_APP.BACKENDS.EMAIL'

PUBLICATION_BACKENDS = (
    RABBITMQ_BACKEND, SLACK_BACKEND, SMS_BACKEND, EMAIL_BACKEND
)

SQREEN_SECURITY_EVENT = 'security_event'
SQREEN_PULSE_EVENT = 'pulse'

# Can add more headers here and the app will dynamically change the headers.
SECURITY_HEADERS = (
    {'header': 'X-Frame-Options', 'value': 'DENY'},
    {'header': 'X-XSS-Protection', 'value': '1; mode=block'},
    {'header': 'X-Content-Type-Options', 'value': 'nosniff'},
    {'header': 'Content-Security-Policy', 'value': "default-src 'self'"},
    {'header': "Strict-Transport-Security", "value": "max-age=31536000; includeSubDomains"}
)
