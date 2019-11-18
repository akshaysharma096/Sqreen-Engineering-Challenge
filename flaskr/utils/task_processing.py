# -*- coding: utf-8 -*-
# Written by Akshay Sharma, <akshay.sharma09695@gmail.com>

from flaskr.config import PUBLICATION_BACKENDS, APPLICATION_ID
from uuid import uuid4
import datetime
from flaskr.config import SQREEN_PULSE_EVENT, SQREEN_SECURITY_EVENT
from .logging import logger
from flaskr.celery.tasks import process_message, notify_internal_security_error


class TaskProcessor:

    def __init__(self):
        self._backends = PUBLICATION_BACKENDS
        self._application_id = APPLICATION_ID

    def send_to_queue(self, notifications):
        for _, notification in enumerate(notifications):
            self._dump_to_queue(notification)

    def _dump_to_queue(self, notification):
        for _, backend in enumerate(self._backends):
            msg = self._build_message(notification)
            process_message.apply_async(args=(msg, backend))

    def _build_message(self, notification):
        message = {
            'id': uuid4().hex,
            'processed_at': datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat(),
            'notification': notification
        }
        self._check_for_internal_issue(notification)
        return message

    def _check_for_internal_issue(self, notification):
        if 'application_id' in notification and notification['application_id'] == self._application_id:
            # Tagging a log with application id.
            notification_type = notification['sqreen_payload_type']
            logger.info(
                "[APP PROBLEM]: {0}, Message {1} shows in built app issue".format(self._application_id,
                                                                                  notification_type))
            alert = None
            # Sending alert notification to admins
            if notification_type == SQREEN_SECURITY_EVENT:
                alert = {key: notification[key] for key in
                         ['event_kind', 'humanized_description', 'event_category', 'date_occurred', 'environment',
                          'url']}

            elif notification_type == SQREEN_PULSE_EVENT:
                alert = {key: notification[key] for key in
                         ['humanized_title', 'pulse_genre', 'environment', 'date_started', 'date_ended', 'blocked',
                          'url']}
            if alert:
                notify_internal_security_error.apply_async(args=(alert,))


task_processor = TaskProcessor()
