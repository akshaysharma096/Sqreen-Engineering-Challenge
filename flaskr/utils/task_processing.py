from flaskr.config import PUBLICATION_BACKENDS
from uuid import uuid4
import datetime
from .logging import logger


class TaskProcessor:

    def __init__(self):
        self.backends = PUBLICATION_BACKENDS

    def send_to_queue(self, notifications):
        for _, notification in enumerate(notifications):
            self._dump_to_queue(notification)

    def _dump_to_queue(self, notification):
        for _, backend in enumerate(self.backends):
            msg = self._build_messsage(notification)
            logger.info(msg)


    @staticmethod
    def _build_messsage(notification):
        message = {
            'id': uuid4().hex,
            'sent_at': datetime.datetime.utcnow().isoformat(),
            'notification': notification
        }
        return message


task_processor = TaskProcessor()
