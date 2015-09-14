# -*- coding: utf-8 -*-
from django.conf import settings

SMS_DEBUG = getattr(settings, 'SMS_DEBUG', False)#if True will no send really sms

SMS_BACKEND = getattr(settings, 'SMS_BACKEND', 'sms.backends.yunpian.SMSBackend')

API_KEY_YUNPIAN = getattr(settings, 'API_KEY_YUNPIAN','enter_your_apikey...')

API_VERSION_YUNPIAN = getattr(settings, 'API_VERSION_YUNPIAN', 'v1')

API_HOST_YUNPIAN = getattr(settings, 'HOST_YUNPIAN','yunpian.com')

API_PORT_YUNPIAN = getattr(settings, 'API_VERSION_YUNPIAN', 80)


