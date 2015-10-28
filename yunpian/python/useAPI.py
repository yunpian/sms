#!/usr/local/bin/python
#-*-coding:utf-8-*-

#author: jacky
# Time: 14-2-22 下午11:48uthor: jacky
# Desc: 短信http接口的python代码调用示例
# https://www.yunpian.com/api/demo.html
import httplib
import urllib
import json
#服务地址
host = "yunpian.com"
#端口号
port = 80
#版本号
version = "v1"
#查账户信息的URI
user_get_uri = "/" + version + "/user/get.json"
#智能匹配模版短信接口的URI
sms_send_uri = "/" + version + "/sms/send.json"
#模板短信接口的URI
sms_tpl_send_uri = "/" + version + "/sms/tpl_send.json"
#语音短信接口的URI
sms_voice_send_uri = "/" + version + "/voice/send.json"
#语音验证码
voiceCode = 1234
def get_user_info(apikey):
    """
    取账户信息
    """
    conn = httplib.HTTPConnection(host , port=port)
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn.request('POST',user_get_uri,str( 'apikey=' + apikey))
    response = conn.getresponse()
    response_str = response.read()
    conn.close()
    return response_str

def send_sms(apikey, text, mobile):
    """
    能用接口发短信
    """
    params = urllib.urlencode({'apikey': apikey, 'text': text, 'mobile':mobile})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = httplib.HTTPConnection(host, port=port, timeout=30)
    conn.request("POST", sms_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    conn.close()
    return response_str

def tpl_send_sms(apikey, tpl_id, tpl_value, mobile):
    """
    模板接口发短信
    """
    params = urllib.urlencode({'apikey': apikey, 'tpl_id':tpl_id, 'tpl_value': tpl_value, 'mobile':mobile})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = httplib.HTTPConnection(host, port=port, timeout=30)
    conn.request("POST", sms_tpl_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    conn.close()
    return response_str

def send_voice_sms(apikey, code, mobile):
    """
    能用接口发短信
    """
    params = urllib.urlencode({'apikey': apikey, 'code': code, 'mobile':mobile})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = httplib.HTTPConnection(host, port=port, timeout=30)
    conn.request("POST", sms_voice_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    conn.close()
    return response_str

if __name__ == '__main__':
    apikey = "a4b3f38430ef7be6704b03181e76e7ca"
    mobile = "18812412312"
    text = "您的验证码是1234【云片网】"
    #查账户信息
    print(get_user_info(apikey))
    #调用智能匹配模版接口发短信
    print send_sms(apikey,text,mobile)
    #调用模板接口发短信
    tpl_id = 1 #对应的模板内容为：您的验证码是#code#【#company#】
    tpl_value = '#code#=1234&#company#=云片网'
    print(tpl_send_sms(apikey, tpl_id, tpl_value, mobile))
    #调用模板接口发语音短信
    print (send_voice_sms(apikey,voiceCode,mobile))