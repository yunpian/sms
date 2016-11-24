# -*- coding: utf-8 -*-
"""SMS backend class."""
import threading
from sms.backends.base import BaseSMSBackend
import httplib
import urllib
from sms.conf import settings as sms_settings

class SMSBackend(BaseSMSBackend):
    """
    A wrapper that manages the yunpian sms network connection.
    """
    def __init__(self,host=None,version=None,apikey=None,fail_silently=False, **kwargs):
        super(SMSBackend, self).__init__(fail_silently=fail_silently)
        if apikey is None:
            self.apikey = sms_settings.API_KEY_YUNPIAN
        if host is None:
            self.host = sms_settings.API_HOST_YUNPIAN
        if version is None:
            version = sms_settings.API_VERSION_YUNPIAN
        self.port = sms_settings.API_PORT_YUNPIAN
        #通用短信接口的URI
        self.sms_send_uri = "/" + version + "/sms/send.json"
        #模板短信接口的URI
        self.sms_tpl_send_uri = "/" + version + "/sms/tpl_send.json"
        self.connection = None
        self._lock = threading.RLock()

    def open(self):
        """
        Ensures we have a connection to the yunpian http sms service server. 
        Returns whether or not a new connection was required (True or False).
        """
        if self.connection:
            # Nothing to do if the connection is already open.
            return False
        try:
            # If local_hostname is not specified, socket.getfqdn() gets used.
            # For performance, we use the cached FQDN for local_hostname.
            self.connection = httplib.HTTPConnection(self.host, self.port)
            return True
        except:
            if not self.fail_silently:
                raise

    def close(self):
        """Closes the connection to the sms server."""
        if self.connection is None:
            return
        try:
            self.connection.close()
        except Exception:
            if self.fail_silently:
                return
            raise
        finally:
            self.connection = None

    def send_messages(self, sms_messages):
        """
        Sends one or more SmsMessage objects and returns 
        the number of sms messages sent.
        """
        if not sms_messages:
            return
        with self._lock:
            new_conn_created = self.open()
            if not self.connection:
                # We failed silently on open().
                # Trying to send would be pointless.
                return
            num_sent = 0
            sent_results = []
            for message in sms_messages:
                sent = self._send(message)
                sent_results.append(sent) 
                if sent:
                    num_sent += 1
            if new_conn_created:
                self.close()
        return (num_sent,sent_results)

    def _send(self, sms_message):
        """A helper method that does the actual sending."""
        if not sms_message.recipients():
            return False
        mobile = sms_message.mobile()
        message = sms_message.message()
        params_map = {'apikey': self.apikey,'mobile':mobile}
        headers = {"Content-type": "application/x-www-form-urlencoded", 
                   "Accept": "text/plain"}
        try:
            if sms_message.tpl_id is None:
                params_map['text'] = massage   
                params = urllib.urlencode(params_map)
                send_uri = self.sms_send_uri
            else:
                params_map['tpl_id'] = sms_message.tpl_id
                params_map['tpl_value'] = message
                params = urllib.urlencode(params_map)
                send_uri = self.sms_tpl_send_uri
            self.connection.request("POST", send_uri, params, headers)
            response = self.connection.getresponse()
            response_str = response.read()
        except Exception:
            if not self.fail_silently:
                raise
            return False
        return response_str



