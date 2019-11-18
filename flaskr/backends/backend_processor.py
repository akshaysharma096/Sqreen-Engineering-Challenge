# -*- coding: utf-8 -*-
# Written by Akshay Sharma, <akshay.sharma09695@gmail.com>

from flaskr.config import PUBLICATION_BACKENDS
from flaskr.utils.logging import logger
from flaskr import config
from flaskr.backends.backend_manager import slack_manager, email_manager, sms_manager, rabbitmq_manager


class BackendProcessor:

    def __init__(self):
        self._supported_backends = set(PUBLICATION_BACKENDS)

    def send_to_backend(self, notification, backend):
        if backend not in self._supported_backends:
            return
        if backend == config.EMAIL_BACKEND:
            email_manager.process_notification(notification)
        elif backend == config.SMS_BACKEND:
            sms_manager.process_notification(notification)
        elif backend == config.RABBITMQ_BACKEND:
            rabbitmq_manager.process_notification(notification)
        elif backend == config.SLACK_BACKEND:
            slack_manager.process_notification(notification)
        else:
            logger.info(
                "[NOTIFICATION DISPATCHING FAILURE]: Dispatching notification failed: {0} for backend: {1}".format(
                    notification,
                    backend))

    @staticmethod
    def notify_admins(alert):
        email_manager.notify_admins(alert)
        sms_manager.notify_admins(alert)
        slack_manager.notify_admins(alert)
        email_manager.notify_admins(alert)


backend_processor = BackendProcessor()
