# -*- coding: utf-8 -*-
# Written by Akshay Sharma, <akshay.sharma09695@gmail.com>

from flaskr.config import PUBLICATION_BACKENDS
from flaskr.utils.logging import logger


class BackendProcessor:

    def __init__(self):
        self._supported_backends = set(PUBLICATION_BACKENDS)

    def send_to_backend(self, notification, backend):
        if backend not in self._supported_backends:
            return
        logger.info(
            "[NOTIFICATION DISPATCH]: Dispatching notification: {0} to backend: {1}".format(notification, backend))


backends = BackendProcessor()
