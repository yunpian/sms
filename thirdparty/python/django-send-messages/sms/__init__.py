# -*- coding: utf-8 -*-
"""
Tools for sending sms
"""
from __future__ import unicode_literals

import re

from django.utils.module_loading import import_by_path
from sms.message import SMSMessage
from sms.conf import settings as sms_settings
import sms
import logging
import json

logger = logging.getLogger('hwbuluo')

def get_connection(backend=None, fail_silently=False, **kwds):
    """Load an sms backend and return an instance of it.
    If backend is None (default) settings.SMS_BACKEND is used.
    Both fail_silently and other keyword arguments are used in the
    constructor of the backend.
    """
    klass = import_by_path(backend or sms_settings.SMS_BACKEND)
    return klass(fail_silently=fail_silently, **kwds)


def send_sms(tpl_id=None,
             content='',
             recipient_list=None,
             fail_silently=False,
             connection=None):
    """
    Easy wrapper for sending a single message to a recipient list. All members
    of the recipient list will see the other recipients in the 'To' field.
    """
    connection = connection or get_connection(fail_silently=fail_silently)

    return SMSMessage(tpl_id, content,
                      recipient_list,connection=connection).send()


MOBILE_RE = r'^(13[0-9]|15[012356789]|18[0-9]|14[57]|17[6-8])[0-9]{8}$'
MOBILE_RE_PATTERN = re.compile(MOBILE_RE)
def is_correct_mobile(mnumber):
    """
    http://www.jihaoba.com/tools/?com=haoduan
    http://blog.csdn.net/fengshi_sh/article/details/12085307
    移动：139 138 137 136 135 134 147 150 151 152 157 158 159 178 182 
          183 184 187 188  
    联通：130 131 132 155 156 185 186 145 176  
    电信：133 153 177 180 181 189  
    ^(0|86|17951)?(13[0-9]|15[012356789]|18[0-9]|14[57]|17[6-8])[0-9]{8}$
    """
    match = MOBILE_RE_PATTERN.match(mnumber)
    if match:
        return True
    else:
        return False

def simple_send_sms(tpl_id, phone_nos, content):
    """
    tpl_id 模版ＩＤ
    phone_nos 电话号码
    content 内容
    """
    if sms_settings.SMS_DEBUG:#本地local server测试时需要
        print 'send sms activiation %s' % content

    result = send_sms(tpl_id=tpl_id,
                      content=content,
                      recipient_list=phone_nos)
    # add log and add receive send error deal
    #http://www.yunpian.com/api/retcode.html
    response_msgs = result[1]
    for response_msg in response_msgs:
        res = json.loads(response_msg)
        code = res.get("code", None)
        msg = res.get("msg", '')
        if code is not None:
            if code == 0:
                logger.info("success send a msg")
            elif code > 0:
                detail = res.get("detail", '')
                rmsg = "send sms Error:调用API时发生错误，需要开发者进行相应的处理。#===code:%d msg:%s detail:%s===#" % (
                code, msg, detail)
                logger.error(rmsg)
            elif code <= -1 and code > -50:
                detail = res.get("detail", '')
                rmsg = "send sms Error:调用API时发生错误，需要开发者进行相应的处理。#===code:%d msg:%s detail:%s===#" % (
                code, msg, detail)
                logger.error(rmsg)
            elif code <= -50:
                detail = res.get("detail", '')
                rmsg = "send sms Error:调用API时发生错误，需要开发者进行相应的处理。#===code:%d msg:%s detail:%s===#" % (
                code, msg, detail)
                logger.error(rmsg)
        else:
            logger.error('Sms Response No code!')
    return response_msgs
