### yunpian-sms-client

[yunpian-sms-client](https://github.com/CowPanda/yunpian-sms-client) 用于对接云片网提供的短信发送接口的nodejs简单实现，相关的接口和示例已测试通过，若有问题请在issue中提出或pull request。

> 更新版本至v2，详见云片网API文档:[v2.0文档](https://www.yunpian.com/api2.0)
> **注：使用此`yunpian-sms-client` 的旧版本(*v1.x*)若升级至当前最新版本，原调用的代码需要进行局部修改，请参见示例:[v1.x使用示例](https://github.com/CowPanda/yunpian-sms-client/blob/master/example/yunpain-sms-client-v1.js)** 。

> **本次更新主要是为了适配云片网API v2.0新接口(*按自己需要实现了部份*)，在调用层面支持Promise的风格调用，缩减了一些无用的代码。**

---

[TOC]

---

### 说明

`yunpian-sms-client` 旧版本的调用方式请移步[示例中查看](https://github.com/CowPanda/yunpian-sms-client/blob/master/example/yunpain-sms-client-v1.js), 以下信息都是以当前版本做说明，所列出的接口实现中已支持官方文档中注明的所有参数(*有些参数如发送信息后希望回调uid需要申请开通，这里就不作演示了*).

### 安装

    npm install yunpian-sms-client

### 初始化一个SMS Provider

```
var smsProvider = require('yunpian-sms-client').v2;
var apiKey = 'your apiKey';
var provider = smsProvider.initWithKey(apiKey);
var text = '【xxxx】您的短信验证码为：23845';
var mobile = 'your mobile';
```

### 单条信息发送
```javascript

provider.sendSingleSms({
    mobile: mobile,
    text: text,
    uid: '234'//可选，请参见官方文档说明
}).then(function (result) {
    if (result) {
        console.log(result);
    }
}).catch(function (err) {
    console.log(err);
});

//或者分步写效果是一样，后续的示例不再重复说明
var promise = provider.sendSingleSms({
    mobile: mobile,
    text: text,
    uid: '234'//可选，请参见官方文档说明
});

promise.then(function(result){
//
});
promise.catch(function(err){
 //
})
```

### 批量发送信息

```

provider.sendBatchSms({mobile:'your mobile,your girl mobile...',text:text}).then(function(result){
    if(result){
        console.log(result);
    }
}).catch(function(err){
    console.log(err);
});

```

### 指定模板单发（官方不推荐使用）,看起来用处也不是很大

```

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

```

### 查短信发送报告

```
provider.getSmsStatusReport({page_size: 10}).then(function (report) {
    if (report) {
        console.log(report);
    }
}).catch(function (err) {
    console.log(err);
});
```

### 查短信发送记录

```
provider.getSmsSendRecord({start_time: '2016-01-02 00:00:00', end_time: '2016-06-23 12:00:00'}).then(function (record) {
    if (record) {
        console.log(record);
    }
}).catch(function (err) {
    console.log(err);
});

```


### 备注

其他的接口暂不对接了，需真有需要再行对接。




