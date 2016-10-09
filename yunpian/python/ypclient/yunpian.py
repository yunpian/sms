# coding: utf8
"""
YunPian client for python.

Independence: requests=2.11.0

Features:
    1. Persistent connection
    2. Support py2/py3
    3. Configurable client

:author: gzj 20160812
"""

import requests

try:
    from urllib.parse import quote
except ImportError:
    from urllib import quote


class ClientBase(object):
    """
    :author gzj 20160808
    """
    ALLOWED_METHODS = ['post']

    TPL_CERTIFY_NOTIFY_ALWAYS = 0
    TPL_CERTIFY_NOTIFY_ONLY_DENIED = 1
    TPL_CERTIFY_NOTIFY_ONLY_PASSED = 2
    TPL_CERTIFY_NOTIFY_ONLY_NO = 3

    CARRIER_CHINA_MOBILE = '10086'
    CARRIER_CHINA_UNICOM = '10010'
    CARRIER_CHINA_TELECOM = '10000'

    def __init__(self, api_key, time_out=5, res_format='json', ssl_verify=True):
        """
        :param api_key: {string}
        :param res_format: {string}
        :param time_out: {int} duration of request time out, in seconds
        """
        self.__heads = {
            "Accept": "application/json;charset=utf-8;",
            "Content-Type": "application/x-www-form-urlencoded;charset=utf-8;"
        }
        self.api_key = api_key
        self.url_tpl = "https://{business_type}.yunpian.com/{version}/{resource}/{function}.{res_format}"
        self.api_version = None
        self.session = requests.Session()
        self.time_out = time_out
        self.res_format = res_format
        self.ssl_verify=ssl_verify

    def request(self, business_type, resource, function, req_method, **kwargs):
        """
        make a request
        :param business_type: {string}
        :param resource: {string} resource name
        :param function: {string} method name to handle resource
        :param req_method: {string} request method
        :param kwargs: {dict} request params
        :return: {Response}
        :author: gzj 20160812
        """
        req_url = self.url_tpl.format(
            business_type=business_type,
            version=self.api_version,
            resource=resource,
            function=function,
            res_format=self.res_format,
        )

        req_method = req_method.lower()

        kwargs['apikey'] = self.api_key
        kwargs = self.assemble_params(**kwargs)

        if req_method not in self.ALLOWED_METHODS:
            raise ValueError('method %s is not allowed' % req_method)

        return getattr(self.session, req_method)(req_url, data=kwargs, verify=self.ssl_verify, timeout=self.time_out)

    @staticmethod
    def assemble_params(**kwargs):
        """
        :param kwargs: {dict} params
        :return: {dict}
        :author: gzj 20160812
        """
        params = {}
        for k, v in kwargs.items():
            if v != None:
                params[k] = v
        return params

    @staticmethod
    def assemble_tpl(signature, content):
        """
        :param signature: {string}
        :param content: {string}
        :return: {string} SMS template
        :author: gzj 20160812
        """
        return '【%s】%s' % (signature, content)

    @staticmethod
    def format_datetime(dt, time_format='%Y-%m-%d %H:%M:%S'):
        """
        :param dt: {datetime}
        :param time_format: {string}
        :return: {string} formatted datetime
        :author: gzj 20160812
        """
        return dt.strftime(time_format)


class ClientV1(ClientBase):
    """
    :author: gzj 20160812
    """
    def __init__(self, *args, **kwargs):
        super(ClientV1, self).__init__(*args, **kwargs)

        self.api_version = 'v1'

    def get_account(self):
        """
        Get account information
        :return: {Response}
        :author: gzj 20160812
        """
        return self.request('sms', 'user', 'get', 'post')

    def modify_account(self, emergency_contact, emergency_mobile, alarm_balance):
        """
        Modify account information
        :param emergency_contact: {string}
        :param emergency_mobile: {string}
        :param alarm_balance: {int}
        :return: {Response}
        :author: gzj 20160812
        """
        params = dict(
            emergency_contact=emergency_contact,
            emergency_mobile=emergency_mobile,
            alarm_balance=alarm_balance,
        )

        return self.request('sms', 'user', 'set', 'post', **params)

    def create_sms_tpl(self, signature, content, notify_type=ClientBase.TPL_CERTIFY_NOTIFY_ALWAYS):
        """
        Create SMS template. A SMS template makes up from signature and content. New sms must be certified before using.
        :param signature: {string}
        :param content: {string}
        :param notify_type: {string}
        :return: {Response}
        :author: gzj 20160812
        """
        tpl_content = self.assemble_tpl(signature, content)
        return self.request('sms', 'tpl', 'add', 'post', tpl_content=tpl_content, notify_type=notify_type)

    def get_sms_tpl(self, tpl_id=None):
        """
        Get SMS template information
        :param tpl_id: {int}
        :return: {Response}
        :author: gzj 20160812
        """
        return self.request('sms', 'tpl', 'get', 'post', tpl_id=tpl_id)

    def modify_sms_tpl(self, tpl_id, signature, content):
        """
        Modify SMS template. Once be modified, the template will be re-certified as a new one.
        :param tpl_id: {int}
        :param signature: {string}
        :param content: {string}
        :return: {Response}
        :author: gzj 20160812
        """
        tpl_content = self.assemble_tpl(signature, content)
        return self.request('sms', 'tpl', 'update', 'post', tpl_id=tpl_id, tpl_content=tpl_content)

    def del_sms_tpl(self, tpl_id):
        """
        Delete SMS template.
        :param tpl_id: {int}
        :return: {Response}
        :author: gzj 20160812
        """
        return self.request('sms', 'tpl', 'del', 'post', tpl_id=tpl_id)

    def send_sms(self, mobile, content, extend=None, uid=None, callback_url=None):
        """
        Send SMS. The content of SMS should match one template you have registered.
        :param mobile: {string} mobile phone number to receive sms
        :param content: {string} sms content
        :param extend: {string}
        :param uid: {string}
        :param callback_url: {string}
        :return: {Response}
        :author: gzj 20160812
        """
        params = {
            'mobile': mobile,
            'text': content,
            'extend': extend,
            'uid': uid,
            'callback': callback_url
        }
        return self.request('sms', 'sms', 'send', 'post', **params)

    def get_sms_status(self, page_size=None):
        """
        Get SMS status.

        ATTENTION: Server will clean all sms status data after the data is returned.

        :param page_size: {int}
        :return: {Response}
        :author: gzj 20160812
        """
        return self.request('sms', 'sms', 'pull_status', 'post', page_size=page_size)

    def get_sms_reply(self, page_size=None):
        """
        Get customer reply.

        ATTENTION: Server will clean all sms status data after the data is returned.

        :param page_size: {int}
        :return: {Response}
        :author: gzj 20160812
        """
        return self.request('sms', 'sms', 'pull_reply', 'post', page_size=page_size)

    def retrieve_sms_reply(self, start_time, end_time, page_size,
                           page_num=1, mobile=None, return_fields=None, sort_fields=None):
        """
        Retrieve customer reply by query param

        :param start_time: {datetime|string}
        :param end_time: {datetime|string}
        :param page_size: {int}
        :param mobile: {string}
        :param page_num: {int}
        :param return_fields: {disabled}
        :param sort_fields: {disabled}
        :return: {Response}
        :author: gzj 20160812
        """
        params = {
            'start_time': start_time if type(start_time) == str else self.format_datetime(start_time),
            'end_time': end_time if type(end_time) == str else self.format_datetime(end_time),
            'page_num': page_num,
            'page_size': page_size,
            'mobile': mobile,
            'return_fields': return_fields,
            'sort_fields': sort_fields
        }
        return self.request('sms', 'sms', 'get_reply', 'post', **params)

    def get_black_word(self, content):
        """
        Get words , which are not allowed, in content
        :param content: {string} content for checking
        :return: {Response}
        :author: gzj 20160812
        """
        return self.request('sms', 'sms', 'get_black_word', 'post', text=content)

    def send_tpl_sms(self, mobile, tpl_id, tpl_context, extend=None, uid=None):
        """
        Send SMS by template id.

        :param mobile: {string}
        :param tpl_id: {int}
        :param tpl_context: {dict} If you want to render a template like 'I am #name#', then tpl_param should be {"name": "your name"}
        :param extend: {string}
        :param uid: {string}
        :return: {Response}
        :author: gzj 20160812
        """
        real_context = []
        for k, v in tpl_context.items():
            k = quote('#%s#' % k)
            v = quote(v)
            real_context.append('%s=%s' % (k, v))

        params = dict(
            mobile=mobile,
            tpl_id=tpl_id,
            tpl_value='&'.join(real_context),
            extend=extend,
            uid=uid
        )

        return self.request('sms', 'sms', 'tpl_send', 'post', **params)

    def send_multi_sms(self, mobiles=[], contents=[], jobs=[], extend=None, uid=None, callback_url=None):
        """
        Send multiple SMS to multiple mobile at the same time
        :param mobiles: {list} phone number strings
        :param contents: {list} message content strings
        :param jobs: {list|dict} element is a mobile -> sms map, break into phones/messages at last
            example:
                case list:
                    [
                        {
                            'phone_1': 'message_1',
                            'phone_2': 'message_2',
                            ...
                        },
                        {
                            'phone_2': 'message_3',
                            'phone_3': 'message_4',
                            ...
                        },
                        ...
                    ]

                case dict:
                    {
                        'phone_1': 'message_1',
                        'phone_2': 'message_2',
                        ...
                    }

        :param extend: {string}
        :param uid: {string}
        :param callback_url: {string}
        :return: {Response}
        :author: gzj 20160812
        """

        if jobs:
            mobiles, contents = [], []

            if type(jobs) == dict:
                jobs = [jobs]

            for job in jobs:
                for mobile, content in job.items():
                    mobiles.append(mobile)
                    contents.append(quote(content))

        if len(mobiles) > 1000:
            raise ValueError('Can\'t send more then 1000 SMS at the same time')

        mobiles = ','.join(mobiles)
        contents = ','.join(contents)
        params = dict(
            mobile=mobiles,
            text=contents,
            extend=extend,
            uid=uid,
            callback_url=callback_url
        )

        return self.request('sms', 'sms', 'multi_send', 'post', **params)

    def get_sms_send_record(self, start_time, end_time, page_size, page_num=1, mobile=None):
        """
        :param start_time: {datetime|string}
        :param end_time: {datetime|string}
        :param page_size: {int}
        :param page_num: {int}
        :param mobile: {string}
        :return: {Response}
        :author: gzj 20160812
        """
        params = dict(
            start_time=start_time if type(start_time) == str else self.format_datetime(start_time),
            end_time=end_time if type(end_time) == str else self.format_datetime(end_time),
            page_size=page_size,
            page_num=page_num,
            mobile=mobile
        )
        return self.request('sms', 'sms', 'get_record', 'post', **params)

    def count_sms(self, start_time, end_time, mobile=None, page_num=None, page_size=None):
        """
        :param start_time: {datetime|string}
        :param end_time: {datetime|string}
        :param mobile: {string}
        :param page_num: {int}
        :param page_size: {int}
        :return: {Response}
        :author: gzj 20160812
        """
        params = dict(
            start_time=start_time if type(start_time) == str else self.format_datetime(start_time),
            end_time=end_time if type(end_time) == str else self.format_datetime(end_time),
            mobile=mobile,
            page_num=page_num,
            page_size=page_size
        )
        return self.request('sms', 'sms', 'count', 'post', **params)

    def voice_verification_code(self, phone, code, callback_url=None, display_num=None):
        """
        :param phone: {string}
        :param code: {int}
        :param callback_url: {string}
        :param display_num: {string}
        :return: {Response}
        :author: gzj 20160812
        """
        params = dict(
            mobile=phone,
            code=code,
            callback_url=callback_url,
            display_num=display_num
        )
        return self.request('voice', 'voice', 'send', 'post', **params)
    
    def get_voice_verification_status(self, page_size=None):
        """
        :param page_size: {int}
        :return: {Response}
        :author: gzj 20160812
        """
        return self.request('voice', 'voice', 'pull_status', 'post', page_size=page_size)

    def get_data_traffic(self, carrier=None):
        """

        :param carrier: {string}
        :return: {Response}
        :author: gzj 20160812
        """
        return self.request('flow', 'flow', 'get_package', 'post', carrier=carrier)

    def recharge_data_traffic(self, mobile, sn, callback_url=None):
        """
        :param mobile: {string}
        :param sn: {string}
        :param callback_url: {string}
        :return: {Response}
        :author: gzj 20160812
        """
        return self.request('flow', 'flow', 'recharge', 'post', mobile=mobile, sn=sn, callback_url=callback_url)

    def get_data_traffic_status(self, page_size=None):
        """
        :param page_size: {int}
        :return: {Response}
        :author: gzj 20160812
        """
        return self.request('flow', 'flow', 'pull_status', 'post', page_size=page_size)


class ClientV2(ClientV1):
    """
    :author: gzj 20160812
    """
    def __init__(self, *args, **kwargs):
        """
        :author: gzj 20160812
        """
        super(ClientV2, self).__init__(*args, **kwargs)

        self.api_version = 'v2'

    def get_default_sms_tpl(self, tpl_id=None):
        """
        :param tpl_id: {int}
        :return: {Response}
        :author: gzj 20160812
        """
        return self.request('sms', 'tpl', 'get_default', 'post', tpl_id=tpl_id)

    def send_sms(self, mobile, content, extend=None, uid=None, callback_url=None):
        """
        :return: {Response}
        :author: gzj 20160812
        """
        params = {
            'mobile': mobile,
            'text': content,
            'extend': extend,
            'uid': uid,
            'callback': callback_url
        }
        return self.request('sms', 'sms', 'single_send', 'post', **params)

    def broadcast_sms(self, mobiles, content, extend=None, uid=None, callback_url=None):
        """
        :param mobiles: {list} mobile phone number list
        :param content: {string}
        :param extend: {string}
        :param uid: {string}
        :param callback_url: {string}
        :return: {Response}
        :author: gzj 20160812
        """
        params = dict(
            mobile=','.join(mobiles),
            text=content,
            extend=extend,
            uid=uid,
            callback_url=callback_url
        )
        return self.request('sms', 'sms', 'batch_send', 'post', **params)

    def send_tpl_sms(self, mobile, tpl_id, tpl_context, extend=None, uid=None):
        """
        :return: {Response}
        :author: gzj 20160812
        """
        real_context = []
        for k, v in tpl_context.items():
            k = quote('#%s#' % k)
            v = quote(v)
            real_context.append('%s=%s' % (k, v))

        params = dict(
            mobile=mobile,
            tpl_id=tpl_id,
            tpl_value='&'.join(real_context),
            extend=extend,
            uid=uid
        )

        return self.request('sms', 'sms', 'tpl_single_send', 'post', **params)

    def broadcast_tpl_sms(self, *args, **kwargs):
        raise NotImplementedError('waiting ...')
