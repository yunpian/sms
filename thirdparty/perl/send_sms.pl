#!/usr/bin/perl
# Author fy@yiyou.org
# Date  2016-09-11
# 云片网短信-perl发送短信示例
# 使用时，务必将文件保存为utf8格式，否则发送的中文会出现乱码

use strict;
use Data::Dumper;
use HTTP::Tiny;
use JSON;
use utf8;

my $tel='13800138000'; #手机号码
my $msg='【验证码】内容'; #发送内容，需要审核通过

my $response = HTTP::Tiny->new->post_form('https://sms.yunpian.com/v2/sms/single_send.json',
                {apikey=>'_your_apikey_here_', #apikey
                mobile=>$tel,
                text=>$msg});
#print Dumper $response;exit;
my $json=decode_json ($response->{content});
print Dumper $json;
