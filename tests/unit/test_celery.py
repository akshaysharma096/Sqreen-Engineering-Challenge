from tests.helpers import get_sample_publication_backend
import json
import uuid

from flaskr.celery.tasks import process_message, notify_internal_security_error
from unittest.mock import patch


class TestCeleryTask:
    """
        Class to test tasks for processing.
    """
    def test_notification_processing_task(self, sample_notification):
        with patch('flaskr.config.CELERY_ALWAYS_EAGER', True, create=True):
            backend = get_sample_publication_backend()
            return_value = process_message(sample_notification, backend)
            assert return_value == True

    def test_internal_security_issue_task(self, sample_internal_issue):
        with patch('flaskr.config.CELERY_ALWAYS_EAGER', True, create=True):
            return_value = notify_internal_security_error(sample_internal_issue)
            assert return_value == True
