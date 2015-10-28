// 修改为您的apikey.可在官网（http://www.yuanpian.com)登录后用户中心首页看到
var apikey = 'a4b3f38430ef7be6704b03181e76e7ca';
// 修改为您要发送的手机号码，多个号码用逗号隔开
var mobile = '18912312312';
// 修改为您要发送的短信内容
var text = '【云片网】您的验证码是1234';
// 指定发送的模板编号
var tpl_id = 1;
// 指定发送模板的内容
var tpl_value =  '#code#=1234&#company#=yunpian';
// 语音短信的内容
var code = 1234;
// 查询账户信息HTTP地址
var get_user_info_uri = '/v1/user/get.json';
// 智能匹配模板发送HTTP地址
send_sms_uri = '/v1/sms/send.json';
// 指定模板发送接口HTTP地址
send_tpl_sms_uri = '/v1/sms/tpl_send.json';
// 发送语音验证码接口HTTP地址
send_voice_uri = '/v1/voice/send.json';



var http = require('http');  
  
var qs = require('querystring');  

query_user_info(get_user_info_uri,apikey);

send_sms(send_sms_uri,apikey,mobile,text);

send_tpl_sms(send_tpl_sms_uri,apikey,mobile,tpl_id,tpl_value);

send_voice_sms(send_voice_uri,mobile,code);
function query_user_info(uri,apikey){
    var post_data = {  
    'apikey': apikey,  
    };//这是需要提交的数据
    var content = qs.stringify(post_data);  
    post(uri,content);
}

function send_sms(uri,apikey,mobile,text){
    var post_data = {  
    'apikey': apikey,  
    'mobile':mobile,
    'text':text,
    };//这是需要提交的数据  
    var content = qs.stringify(post_data);  
    post(uri,content);
}

function send_tpl_sms(uri,apikey,mobile,tpl_id,tpl_value){
    var post_data = {  
    'apikey': apikey,
    'mobile':mobile,
    'tpl_id':tpl_id,
    'tpl_value':tpl_value,  
    };//这是需要提交的数据  
    var content = qs.stringify(post_data);  
    post(uri,content); 
}
function send_voice_sms(uri,apikey,mobile,code){
    var post_data = {  
    'apikey': apikey,
    'mobile':mobile,
    'code':code,
    };//这是需要提交的数据  
    var content = qs.stringify(post_data);  
    post(uri,content); 
}
function post(uri,content){
    var options = {  
        hostname: 'www.yunpian.com',  
        port: 80,  
        path: uri,  
        method: 'POST',  
        headers: {  
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'  
        }  
    };
    var req = http.request(options, function (res) {  
        // console.log('STATUS: ' + res.statusCode);  
        // console.log('HEADERS: ' + JSON.stringify(res.headers));  
        res.setEncoding('utf8');  
        res.on('data', function (chunk) {  
            console.log('BODY: ' + chunk);  
        });  
    }); 
    req.write(content);  
  
    req.end();   
}

