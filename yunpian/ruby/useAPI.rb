=begin

Desc:短信http接口的ruby代码调用示例
author shaoyan
date 2015-10.28

=end

require 'net/http'
params = {}

#修改为您的apikey.可在官网（http://www.yuanpian.com)登录后用户中心首页看到
apikey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
#修改为您要发送的手机号码，多个号码用逗号隔开
mobile = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
#修改为您要发送的短信内容
text = '【云片网】您的验证码是1234'
#查询账户信息HTTP地址
get_user_info_uri = URI.parse('http://yunpian.com/v1/user/get.json')
#智能匹配模板发送HTTP地址
send_sms_uri = URI.parse('http://yunpian.com/v1/sms/send.json')
#指定模板发送接口HTTP地址
send_tpl_sms_uri = URI.parse('http://yunpian.com/v1/sms/tpl_send.json')
#发送语音验证码接口HTTP地址
send_voice_uri = URI.parse('http://yunpian.com/v1/voice/send.json')

params['apikey'] = apikey
#打印用户信息
response =  Net::HTTP.post_form(get_user_info_uri,params)
print response.body + "\n"

params['mobile'] = mobile
params['text'] = text
#智能匹配模板发送
response = Net::HTTP.post_form(send_sms_uri,params)
print response.body + "\n"
#指定模板发送
#设置模板ID，如使用1号模板:【#company#】您的验证码是#code#
#设置对应的模板变量值

params['tpl_id'] = 1
params['tpl_value'] = '#code#=1234&#company#=yunpian'
response = Net::HTTP.post_form(send_tpl_sms_uri,params)
print response.body + "\n"
#发送语音验证码
params['code'] = 1234
response = Net::HTTP.post_form(send_voice_uri,params)
print response.body + "\n"

