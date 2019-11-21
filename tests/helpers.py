# -*- coding: utf-8 -*-
# Written by Akshay Sharma, <akshay.sharma09695@gmail.com>

from flaskr.config import SLACK_BACKEND


def get_sample_publication_backend():
    """
    :return: Returns a sample test backend
    """
    return SLACK_BACKEND
