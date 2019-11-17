# -*- coding: utf-8 -*-
# Written by Akshay Sharma, <akshay.sharma09695@gmail.com>

from flaskr.config import PUBLICATION_BACKENDS, APPLICATION_ID
from uuid import uuid4
import datetime
from .logging import logger


class TaskProcessor:

    def __init__(self):
        self.backends = PUBLICATION_BACKENDS
        self.application_id = APPLICATION_ID

    def send_to_queue(self, notifications):
        for _, notification in enumerate(notifications):
            self._dump_to_queue(notification)

    def _dump_to_queue(self, notification):
        for _, backend in enumerate(self.backends):
            msg = self._build_messsage(notification)
            logger.info(msg)

    def _build_messsage(self, notification):
        message = {
            'id': uuid4().hex,
            'sent_at': datetime.datetime.utcnow().isoformat(),
            'notification': notification,
            'self': False
        }
        if notification['application_id'] == self.application_id:
            message['self'] = True
            # Tagging a log with application id.
            logger.info("[APP PROBLEM: {0}]: Message {1} shows in built app issue".format(self.application_id, message))

        return message


task_processor = TaskProcessor()
