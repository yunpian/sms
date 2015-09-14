# -*- coding:utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^member/sms/reply-receive/$',
        'sms.views.receive_reply_sms',
        name='receive_reply_sms'),
)

