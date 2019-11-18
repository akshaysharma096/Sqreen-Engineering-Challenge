# -*- coding: utf-8 -*-
# Written by Akshay Sharma, <akshay.sharma09695@gmail.com>


from flask import Blueprint, request, jsonify
from flaskr.utils.logging import logger
from flaskr.utils.task_processing import task_processor
from .decorators import validate_incoming_request

v1 = Blueprint('v1', __name__)


@v1.route('/webhook', methods=('POST',))
@validate_incoming_request
def webhook():
    """

    Controller to handle the incoming requests from Sqreen servers
    Processes and dumps the notifications to the respected backends, (SMS, Slack) for notifications.

    :return:200 response code to the Sqreen servers.
    """
    notifications = request.get_json()
    try:
        task_processor.send_to_queue(notifications)
    except Exception as error:
        logger.error('[NOTIFICATION DISPATCH FAILED]: error {0}'.format(error), exc_info=True)
    return jsonify({'status': 'ok'}), 200
