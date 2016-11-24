# -*- coding:utf-8 -*-
from django.shortcuts import render
import urllib
import json
import logging
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from django.utils.encoding import smart_str
from sms.signals import received_yunpian_sms_reply
from django.utils import timezone

logger = logging.getLogger('django-send-messages-sms')

@csrf_exempt
@require_http_methods(["POST"])
def receive_reply_sms(request):
    """
    ref: http://www.yunpian.com/api/sms.html
    推送回复短信
    功能说明：开通此接口后，我们将为您实时推送最新的回复短信。您需要提供一个url地址，接受http post请求 
    备注：该接口为高级接口，默认不开放，如有需要请向客服申请开通。 
    推送方式：POST
    其中json数据示例为：
    {
        "id": "2a70c6bb4f2845da816ea1bfe5732747", //唯一序列号
        "mobile": "15205201314", //回复短信的手机号
        "reply_time": "2014-03-17 22:55:21", //回复短信的时间
        "text": "收到了，谢谢！", //回复的短信内容
        "extend": "01",  //您发送时传入的扩展子号，未申请扩展功能或者未传入时为空串
        "base_extend": "8888"  //系统分配的扩展子号
    }      
    """
    try:
        sms_reply = request.POST['sms_reply']
        sms_reply = urllib.unquote_plus(sms_reply)
        content = smart_str(sms_reply)
        rmap = json.loads( content )
        logger.info('receive_reply_sms'+str(rmap))
        now = timezone.now()
        received_yunpian_sms_reply.send(sender=request, 
                                        content=rmap,
                                        received_by=now )
    except Exception as E:
        logger.error('receive_reply_sms error',exc_info=1)
        return HttpResponse("1")
    return HttpResponse("0")
