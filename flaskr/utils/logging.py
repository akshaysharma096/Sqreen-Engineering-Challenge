# -*- coding: utf-8 -*-
# Written by Akshay Sharma, <akshay.sharma09695@gmail.com>

from flask import Flask
import logging

app = Flask(__name__)

logging.basicConfig(filename='logs/server.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(threadName)s : %(message)s')

logger = app.logger
