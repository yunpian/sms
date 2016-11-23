### yunpian-sms-client
[![npm](https://img.shields.io/npm/v/yunpian-sms-client.svg?style=plastic)](https://npmjs.org/package/yunpian-sms-client) [![npm](https://img.shields.io/npm/dm/yunpian-sms-client.svg?style=plastic)](https://npmjs.org/package/yunpian-sms-client) [![npm](https://img.shields.io/npm/dt/yunpian-sms-client.svg?style=plastic)](https://npmjs.org/package/yunpian-sms-client)

[yunpian-sms-client](https://github.com/CowPanda/yunpian-sms-client) 用于对接云片网提供的短信发送接口的nodejs简单实现，相关的接口和示例已测试通过，若有问题请在issue中提出或pull request。

> 更新版本至v2，详见云片网API文档:[v2.0文档](https://www.yunpian.com/api2.0)
> **注：使用此`yunpian-sms-client` 的旧版本(*v1.x*)若升级至当前最新版本，原调用的代码需要进行局部修改，请参见示例:[v1.x使用示例](https://github.com/CowPanda/yunpian-sms-client/blob/master/example/yunpain-sms-client-v1.js)** 。

> **本次更新主要是为了适配云片网API v2.0新接口(*按自己需要实现了部份*)，在调用层面支持Promise的风格调用，缩减了一些无用的代码。**

> **2016-11-23更新**根据反馈，增加获取回复短信及检查是否屏蔽词接口，并开放自定义调用云片v2.0 API方法，详见下文说明；


---

[TOC]

---

### 说明

`yunpian-sms-client` 旧版本的调用方式请移步[示例中查看](https://github.com/CowPanda/yunpian-sms-client/blob/master/example/yunpain-sms-client-v1.js), 以下信息都是以当前版本做说明，所列出的接口实现中已支持官方文档中注明的所有参数(*有些参数如发送信息后希望回调uid需要申请开通，这里就不作演示了*).

### 安装

    npm install yunpian-sms-client --save

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

### 获取短信回复记录

```
provider.getSmsReplyRecord({
    start_time: '2016-08-11 00:00:00',
    end_time: '2017-08-11 00:00:00',
    page_num:1, //页码，默认1，必填
    page_size:20 //页大小，最大允许100，必填,
    /*mobile:13xxxxxx*///填写时只查该手机号的回复，不填时查所有的回复 ,可选
}).then(function (res) {
    if(res) {
        console.log(res);
    }
}).catch(function (e) {
    console.log(e);
});

```

### 检查内容是否包含屏蔽词

```
provider.isBlackWord('发票,微贷,贷款').then(function (res) {
    if (res) { //返回屏蔽词数组
        console.log(res);
    }
}).catch(function (e) {
    console.log(e);
});
```

### 备注

其他未在此文档中的接口调用，大家若有需要，可以通过以下方式**自定义实现**(_即可自行根据云片的v2.0文档路径定义调用_)，如自定义实现获取回复内容的接口也可以这么实现(_其他接口同理_):

```
//注:若是es6使用者可以直接使用let
var data = {
    start_time: '2016-08-11 00:00:00',
    end_time: '2017-08-11 00:00:00',
    page_num: 1, //页码，默认1，必填
    page_size: 20 //页大小，最大允许100，必填,
    /*mobile:13xxxxxx*///填写时只查该手机号的回复，不填时查所有的回复 ,可选
};
var path = '/v2/sms/get_reply.json';
provider.getCustomReqSmsAPI(data, path).then(function (res) {
    if (res) {
        console.log(res);
    }
}).catch(function (e) {
    console.log(e);
});

```

### 其他说明

习惯上使用co或es6+的童鞋，也可以包装为以下方式:

```
  return co(function *() {
        const path = '/v2/sms/get_reply.json';
        let data = {
            start_time: '2016-08-11 00:00:00',
            end_time: '2017-08-11 00:00:00',
            page_num: 1, //页码，默认1，必填
            page_size: 20 //页大小，最大允许100，必填,
            /*mobile:13xxxxxx*///填写时只查该手机号的回复，不填时查所有的回复 ,可选
        };

        return provider.getCustomReqSmsAPI(data, path);
    });
```


