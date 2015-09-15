# -*- coding: utf-8 -*-
from django.test import TestCase
from sms.conf import settings as sms_settings
import sms
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class SMSTestCaseBase(TestCase):

    def setUp(self):
        sms._original_sms_backend = sms_settings.SMS_BACKEND
        sms_settings.SMS_BACKEND = 'sms.backends.locmem.SMSBackend'
        sms.outbox = []

    def tearDown(self):
        sms_settings.SMS_BACKEND = sms._original_sms_backend
        del sms._original_sms_backend
        del sms.outbox

class SMSTestCase(SMSTestCaseBase):
    def test_sms_send(self):
        sms.send_sms(tpl_id='416085',
                     content="#code#=1234&#timeout#=3",
                     recipient_list=['13311102999'])
        self.assertEquals(sms.outbox[0].message(),"#code#=1234&#timeout#=3")

        sms.send_sms(tpl_id='416085',
                     content="#code#=1234&#timeout#=3",
                     recipient_list=['13311109999','18612589999'])
        self.assertEquals(sms.outbox[0].message(),"#code#=1234&#timeout#=3")
        rl = []
        for i in range(1,102):
            rl.append('13311109999')
        self.assertRaises(AssertionError,sms.send_sms,tpl_id='416085',content='#code#=1234&#timeout#=3',recipient_list=rl)

    def test_receive_sms_reply(self):
        reply_data = {
            "id": "2a70c6bb4f2845da816ea1bfe5732747", #唯一序列号
            "mobile": "15205201314",                  #回复短信的手机号
            "reply_time": "2014-03-17 22:55:21",      #回复短信的时间
            "text": "收到了，谢谢！",                 #回复的短信内容
            "extend": "01",                           #您发送时传入的扩展子号，未申请扩展功能或者未传入时为空串
            "base_extend": "8888"                     #系统分配的扩展子号
        }
        import json
        jsonstr = json.dumps(reply_data)
        jsonstr = '%7B%22id%22%3A%2253e480190cf200b80abc8b25%22%2C%22mobile%22%3A%2213311109999%22%2C%22text%22%3A%22test+reply%22%2C%22reply_time%22%3A%222014-08-08+15%3A45%3A18%22%2C%22extend%22%3A%22%22%2C%22base_extend%22%3A%22702118%22%7D'
        data = {'sms_reply':jsonstr}
        url = reverse('receive_reply_sms')
        response = self.client.post(url,data)
        self.assertEquals(response.content,'0')
        response = self.client.post(url,{'sms_reply':'something wrong'})
        self.assertEquals(response.content,'1')

    def test_multiple_message(self):
        from sms.backends import locmem
        from sms.message import SMSMessage

        backend = locmem.SMSBackend()
        mobile = '13311101111'
        m1 = SMSMessage(tpl_id="416222",
                        content="#code#=1234&#timeout#=3",
                        to=(mobile,))
        m2 = SMSMessage(tpl_id="1",content="#company#=户外部落",to=(mobile,))
        m3 = SMSMessage(tpl_id="2",content="#code#=户外部落",to=(mobile,))
        m4 = SMSMessage(tpl_id="3",content="#code#=户外部落",to=(mobile,))
        backend.send_messages([m1,m2,m3,m4])
