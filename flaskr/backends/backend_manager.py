# -*- coding: utf-8 -*-
# Written by Akshay Sharma, <akshay.sharma09695@gmail.com>

from abc import ABC, abstractmethod


class BackendManager(ABC):
    """
        Abstract class to process a notification
    """

    @abstractmethod
    def process_notification(self, notification):
        pass


class SmsManager(BackendManager):

    def process_notification(self, notification):
        pass


class SlackManager(BackendManager):

    def process_notification(self, notification):
        pass


class EmailManager(BackendManager):

    def process_notification(self, notification):
        pass


class RabbitMQManager(BackendManager):

    def process_notification(self, notification):
        pass


sms_manager = SmsManager()
slack_manager = SlackManager()
email_manager = EmailManager()
rabbitmq_manager = RabbitMQManager()
