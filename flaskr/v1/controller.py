# -*- coding: utf-8 -*-
# Written by Akshay Sharma, <akshay.sharma09695@gmail.com>


from flask import Blueprint, request, jsonify

from flaskr.utils.task_processing import task_processor
from flaskr.v1.decorators import validate_incoming_request

v1 = Blueprint('v1', __name__)


@v1.route('/webhook', methods=('POST',))
@validate_incoming_request
def webhook():
    """

    Controller to handle the incoming requests from Sqreen servers
    Processes and dumps the notifications to the respected backends, (SMS, Slack, EMAIL) for notifications.

    :return:200 response code to the Sqreen servers.
    """
    notifications = request.get_json()
    status = task_processor.send_to_queue(notifications)
    if status:
        return jsonify({'status': True}), 200

    return jsonify({'success': False}), 422
