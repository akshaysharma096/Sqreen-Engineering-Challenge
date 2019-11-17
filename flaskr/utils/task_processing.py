# -*- coding: utf-8 -*-
# Written by Akshay Sharma, <akshay.sharma09695@gmail.com>

from flaskr.config import PUBLICATION_BACKENDS, APPLICATION_ID
from uuid import uuid4
import datetime
from .logging import logger
from flaskr.celery.tasks import process_message


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
            logger.info(msg)
            process_message.apply_async(args=(msg, backend))

    def _build_message(self, notification):
        message = {
            'id': uuid4().hex,
            'sent_at': datetime.datetime.utcnow().isoformat(),
            'notification': notification,
            'self': False
        }
        if notification['application_id'] == self._application_id:
            message['self'] = True
            # Tagging a log with application id.
            logger.info(
                "[APP PROBLEM]: {0}, Message {1} shows in built app issue".format(self._application_id, message))

        return message


task_processor = TaskProcessor()
