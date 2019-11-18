# -*- coding: utf-8 -*-
# Written by Akshay Sharma, <akshay.sharma09695@gmail.com>

from flask import Flask
from flaskr.utils.logging import logger
from flaskr import config
from flaskr.celery_config import make_celery
from flaskr.backends.backend_processor import backend_processor

flask_app = Flask(__name__)
flask_app.config.update(
    CELERY_BROKER_URL=config.CELERY_BROKER_URL,
    CELERY_RESULT_BACKEND=config.CELERY_RESULT_BACKEND
)
celery = make_celery(flask_app)


@celery.task()
def process_message(notification, backend):
    logger.info("[INBOUND ALERT RECEIVED]: {0} for backend: {1} \n".format(notification, backend))
    backend_processor.send_to_backend(notification, backend)


@celery.task()
def notify_internal_security_error(alert):
    logger.info("[INTERNAL SECURITY ALERT]: {0} \n".format(alert))
    backend_processor.notify_admins(alert)
