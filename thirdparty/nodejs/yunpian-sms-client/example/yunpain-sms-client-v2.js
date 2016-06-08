/**
 * Created by cowpanda on 6/8/16.
 */
'use strict';
var smsProvider = require('yunpian-sms-client').v2;
var apiKey = 'your apiKey';
var provider = smsProvider.initWithKey(apiKey);

var text = '【xxxx】您的短信验证码为：23845';
var mobile = 'your mobile';

//单条信息发送
provider.sendSingleSms({
    mobile: mobile,
    text: text,
    uid: '234'
}).then(function (result) {
    if (result) {
        console.log(result);
    }
}).catch(function (err) {
    console.log(err);
});

//====================================
//查短信发送报告
provider.getSmsStatusReport({page_size: 10}).then(function (report) {
    if (report) {
        console.log(report);
    }
}).catch(function (err) {
    console.log(err);
});

//====================================
//查短信发送记录
provider.getSmsSendRecord({start_time: '2016-01-02 00:00:00', end_time: '2016-06-23 12:00:00'}).then(function (record) {
    if (record) {
        console.log(record);
    }
}).catch(function (err) {
    console.log(err);
});


//====================================

//批量发送
provider.sendBatchSms({mobile:'your mobile,your girl mobile...',text:text}).then(function(result){
    if(result){
        console.log(result);
    }
}).catch(function(err){
    console.log(err);
});

//====================================

//指定模板单发（官方不推荐使用）,看起来用处也不是很大
provider.sendSingleTplSms({
    mobile: mobile,
    tpl_id: 1411507,
    tpl_value: "#code#=1411507"
}).then(function (result) {
    if (result) {
        console.log(result);
    }
}).catch(function (err) {
    console.log(err);
});