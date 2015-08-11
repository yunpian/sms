# yunpian-sms-client

[yunpian-sms-client](https://github.com/CowPanda/yunpian-sms-client) 用于对接云片网提供的短信发送接口的nodejs简单实现，相关的接口和示例已测试通过，若有问题请在issue中提出或pull request。

---
# 安装

    npm install yunpian-sms-client

# 发送短信 
```javascript
var yunpainSMSClient = require('yunpian-sms-client');
var c = new yunpainSMSClient({
    apiKey: 'your appkey',
    sendContent: '【your sigure】您的验证码是23405。如非本人操作，请忽略本短信',
    mobile: ['your number']  //注意：请自行验证手机号码是否正确
});

/**
 * 普通短信发送示例
 */
c.sendSMS(function (err, result) {
    if (err) {
        console.log(err);
        return;
    }
    
    console.log(result)
});

```

# 根据定义好的模板发送短信 
```javascript
var c = new yunpainSMSClient({
    apiKey: 'your appkey',
    templateId: 1, //模板Id
    templateValue: "#code#=1234&#company#=yourcompany",
    mobile: ['your number']
});

/**
 * 模板短信发送示例
 */
c.sendSMSByTemplate(function (err, result) {
    if (err) {
        console.log(err);
        return;
    }

    console.log(result)
});
```

