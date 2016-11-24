# -*- coding:utf-8 -*-
from django.dispatch import Signal

"""
content:
    {
        "id": "2a70c6bb4f2845da816ea1bfe5732747", //唯一序列号
        "mobile": "15205201314", //回复短信的手机号
        "reply_time": "2014-03-17 22:55:21", //回复短信的时间
        "text": "收到了，谢谢！", //回复的短信内容
        "extend": "01",  //您发送时传入的扩展子号，未申请扩展功能或者未传入时为空串
        "base_extend": "8888"  //系统分配的扩展子号
    }      

received_by:
timezone.now()
"""
received_yunpian_sms_reply = Signal( providing_args=["content","received_by"] )

