#!perl -w
# Desc:短信http接口的ruby代码调用示例
# author shaoyan
# date 2015-10.28
use strict;
use LWP;
#修改为您的apikey.可在官网（http://www.yuanpian.com)登录后用户中心首页看到
my $apikey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
#修改为您要发送的手机号码，多个号码用逗号隔开
my $mobile = '12312312312';
#修改为您要发送的短信内容
my $text = '【云片网】您的验证码是1234';

#查询账户信息HTTP地址
my $get_user_info_uri = 'http://yunpian.com/v1/user/get.json';
#智能匹配模板发送HTTP地址
my $send_sms_uri = 'http://yunpian.com/v1/sms/send.json';
#指定模板发送接口HTTP地址
my $send_tpl_sms_uri = 'http://yunpian.com/v1/sms/tpl_send.json';
#发送语音验证码接口HTTP地址
my $send_voice_uri = 'http://yunpian.com/v1/voice/send.json';

# 获取用户信息
my $browser = LWP::UserAgent->new();
my $response= $browser->post($get_user_info_uri, 
["apikey" => $apikey]); #多加了一个被发送的数据的数组
print $response->content,"\n"; # 输出获得的网页内容

# 使用智能模板发送短信
$response= $browser->post($send_sms_uri, 
["apikey" => $apikey,"mobile"=>$mobile,"text"=>$text]); #多加了一个被发送的数据的数组
print $response->content,"\n"; # 输出获得的网页内容
#使用模板发送短信
$response= $browser->post($send_tpl_sms_uri, 
["apikey" => $apikey,"mobile"=>$mobile,"tpl_id"=>1,"tpl_value"=>'#code#=1234&#company#=yunpian']); #多加了一个被发送的数据的数组
print $response->content,"\n"; # 输出获得的网页内容
#发送语音验证码
$response= $browser->post($send_voice_uri, 
["apikey" => $apikey,"mobile"=>$mobile,"code"=>1234]); #多加了一个被发送的数据的数组
print $response->content,"\n"; # 输出获得的网页内容