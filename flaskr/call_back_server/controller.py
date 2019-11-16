# -*- coding: utf-8 -*-
# Written by Akshay Sharma, <akshay.sharma09695@gmail.com>


from flask import Blueprint, request, jsonify
from flaskr.utils.logging import logger
# from flask_app.utils.task_processing import task_processor
from .decorators import validate_incoming_request

call_back_server = Blueprint('admin', __name__)


@call_back_server.route('/webhook', methods=('POST','GET'))
# @validate_incoming_request
def webhook():
    logger.info("GET REQUEST")
    notifications = request.get_json()
    # task_processor.send_to_queue(notifications)
    return jsonify({'status': 'ok'}), 200
