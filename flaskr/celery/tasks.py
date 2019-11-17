# -*- coding: utf-8 -*-
# Written by Akshay Sharma, <akshay.sharma09695@gmail.com>

from flask import Flask
from flaskr.utils.logging import logger
from flaskr import config
from flaskr.celery_config import make_celery
from flaskr.backends.backend_processor import backends

flask_app = Flask(__name__)
flask_app.config.update(
    CELERY_BROKER_URL=config.CELERY_BROKER_URL,
    CELERY_RESULT_BACKEND=config.CELERY_RESULT_BACKEND
)
celery = make_celery(flask_app)


@celery.task()
def process_message(notification, backend):
    logger.info("[INBOUND ALERT RECEIVED]: {0} for backend: {1}".format(notification, backend))
    backends.send_to_backend(notification, backends)
