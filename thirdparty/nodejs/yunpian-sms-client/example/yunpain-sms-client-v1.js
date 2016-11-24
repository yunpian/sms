/**
 * Created by cowpanda on 8/11/15.
 */
var yunpainSMSClient = require('yunpian-sms-client').v1;
/**
 * 普通短信发送示例
 */
var text = '【xxxxx】您的短信验证码为：23845';
var c = new yunpainSMSClient({
    apiKey: 'your app key',
    sendContent: text,
    mobile: ['your mobile']
});

c.sendSMS(function (err, result) {
    if (err) {
        console.log(err);
        return;
    }

    console.log(result)
});

//=================================================

/**
 * 模板短信发送示例
 */
var t = new yunpainSMSClient({
    apiKey: 'your app key',
    templateId: 1411507,
    templateValue: "#code#=1234",
    mobile: ['your mobile']
});

t.sendSMSByTemplate(function (err, result) {
    if (err) {
        console.log(err);
        return;
    }

    console.log(result)
});

//=================================================
/**
 * 自行拼接query发送示例
 */
var yunpainSMSClient = require('yunpian-sms-client').v1;
var c = new yunpainSMSClient({
    apiKey: 'your appkey',
    url:'http://yunpian.com',
    sendContent: '【your sigure】您的验证码是23405。如非本人操作，请忽略本短信',
    mobile: ['your number']  //注意：请自行验证手机号码是否正确
});
var query = '/v1/xxxx.json?apiKey=your apikey&text=your content....';

/**
 * 直接拼接query发送短信
 */
c.send(query,function (err, result) {
    if (err) {
        console.log(err);
        return;
    }

    console.log(result)
});
