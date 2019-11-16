from flask import Flask
import logging

app = Flask(__name__)

logging.basicConfig(filename='logs/server.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

logger = app.logger
