# -*- coding: utf-8 -*-
# Written by Akshay Sharma, <akshay.sharma09695@gmail.com>


from flask import Blueprint, request, jsonify
from flaskr.utils.logging import logger
from flaskr.utils.task_processing import task_processor
from .decorators import validate_incoming_request

v1 = Blueprint('v1', __name__)


@v1.route('/webhook', methods=('POST', 'GET'))
# @validate_incoming_request
def webhook():
    logger.info("GET REQUEST")
    notifications = request.get_json()
    task_processor.send_to_queue(notifications)
    return jsonify({'status': 'ok'}), 200
