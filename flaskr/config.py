# -*- coding: utf-8 -*-
# Written by Akshay Sharma, <akshay.sharma09695@gmail.com>


import sys
import os

PYTHON_VERSION = sys.version_info[0]

# Setting up the backend to automatically help process task asynchronously.
CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379')
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379')

# Tuple are immutable data-types, good for security.
# For adding and removing backend we need to change this and our app will behave automatically
PUBLICATION_BACKENDS = (
    'SQREEN_APP.BACKENDS.RABBITMQ',
    'SQREEN_APP.BACKENDS.SLACK',
    'SQREEN_APP.BACKENDS.SMS',
    'SQREEN_APP.BACKENDS.EMAIL'
)

SECURITY_HEADERS = (
    {'header': 'X-Frame-Options', 'value': 'DENY'},
    {'header': 'X-XSS-Protection', 'value': '1; mode=block'},
    {'header': 'X-Content-Type-Options', 'value': 'nosniff'},
    {'header': 'Content-Security-Policy', 'value': "default-src 'self'"},
    {'header': "Strict-Transport-Security", "value": "max-age=31536000; includeSubDomains"}
)
