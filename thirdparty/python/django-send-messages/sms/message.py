# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import six

import logging
logger = logging.getLogger('django-send-messages-sms')

class SMSMessage(object):
    """
    A container for SMS information.
    """
    encoding = None     # None => use settings default

    def __init__(self,tpl_id=None,content='',to=None,connection=None):
        """
        Initialize a single sms message (which can be sent to multiple
        recipients).

        All strings used to create the message can be unicode strings
        (or UTF-8 bytestrings). The SafeMIMEText class will handle any
        necessary encoding conversions.
        """
        if to:
            assert not isinstance(to, six.string_types),'"to" argument must be a list or tuple'
            assert not len(to) > 100,'"to" argument can not exceed 100'
            self.to = list(to)
        else:
            self.to = []
        self.content = content
        self.connection = connection
        self.tpl_id = tpl_id

    def get_connection(self, fail_silently=False):
        from sms import get_connection
        if not self.connection:
            self.connection = get_connection(fail_silently=fail_silently)
        return self.connection

    def message(self):
        return self.content

    def recipients(self):
        """
        Returns a set of all recipients of the sms (includes direct
        addressees as well as Cc and Bcc entries).
        """
        return set(self.to)

    def send(self, fail_silently=False):
        """Sends the sms message."""
        if not self.recipients():
            # Don't bother creating the network connection if there's nobody to
            # send to.
            return 0
        return self.get_connection(fail_silently).send_messages([self])


    def mobile(self):
        from sms import is_correct_mobile
        recipients = [mobile_number for mobile_number in self.recipients() 
                      if is_correct_mobile(mobile_number)]
        logger.info("prepared to send sms to mobiles:%s;",
                    self.recipients(),exc_info=1)
        logger.info("successed send sms to mobiles:%s;",
                    recipients,exc_info=1)
        return ','.join(recipients)
