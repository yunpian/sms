# YunPian SDK For Node.js

[![npm](https://img.shields.io/npm/v/yunpian-sdk.svg?style=plastic)](https://npmjs.org/package/yunpian-sdk) [![npm](https://img.shields.io/npm/dm/yunpian-sdk.svg?style=plastic)](https://npmjs.org/package/yunpian-sdk) [![npm](https://img.shields.io/npm/dt/yunpian-sdk.svg?style=plastic)](https://npmjs.org/package/yunpian-sdk)

云片注册地址： <https://www.yunpian.com/component/reg?inviteCode=atevkh>

Minimum, Flexible, Scalable.

支持Lazy Require。


<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [安装和使用](#%E5%AE%89%E8%A3%85%E5%92%8C%E4%BD%BF%E7%94%A8)
- [手机号合法性校验](#%E6%89%8B%E6%9C%BA%E5%8F%B7%E5%90%88%E6%B3%95%E6%80%A7%E6%A0%A1%E9%AA%8C)
- [已支持的接口](#%E5%B7%B2%E6%94%AF%E6%8C%81%E7%9A%84%E6%8E%A5%E5%8F%A3)
  - [USER - 账户API](#user---%E8%B4%A6%E6%88%B7api)
  - [TPL - 模板API](#tpl---%E6%A8%A1%E6%9D%BFapi)
  - [SMS - 短信API](#sms---%E7%9F%AD%E4%BF%A1api)
  - [VOICE - 语音API](#voice---%E8%AF%AD%E9%9F%B3api)
  - [FLOW - 流量API](#flow---%E6%B5%81%E9%87%8Fapi)
- [License](#license)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->


## 安装和使用

国际惯例：

```
npm install yunpian-sdk --save
```

公共参数：

```js
var options = {
  apikey: 'xxxxxxx'
};
```

ES7:

```js
import {USER} from 'yunpian-sdk';
const user = new USER({
  apikey: 'xxxx'
});
// Within Async Func
(async() => {
  const result = await user.set({
    emergency_contact: 'Willin',
    emergency_mobile: '1xxxxxxxxxx'
  });
  // xxxx
});
```

ES5:

```js
var YUNPIAN = require('yunpian-sdk');
// 加载全部方法
var user = new YUNPIAN.USER({
  apikey: 'xxxx'
});
// 或加载某些方法
var user = new YUNPIAN.USER({
  apikey: 'xxxx'
}, ['get', 'set']);
// 或加载某个方法
var user = new YUNPIAN.USER({
  apikey: 'xxxx'
}, 'get');
user.set({
  emergency_contact: 'Willin',
  emergency_mobile: '1xxxxxxxxxx'
}).then(function(result){
  // xxxx
});
```

## 手机号合法性校验

ES7 示例代码：

```js
import {phone} from 'yunpian-sdk';

// 加区号匹配国际各国号码格式
phone('+8613312345678'); // true
phone('+85265698900'); // true
phone('+112345678'); // false

// 不加区号按中国号码匹配
phone('13312341234'); // true
phone('112345678'); // false

// 按地区匹配
// 地区码使用3位缩写国家代码（大写）
phone('+18175698900', 'USA'); // true
phone('13212345678', 'CHN'); // true
phone('+18175698900', 'CHN'); // false
phone('13212345678', 'HKG'); // false
```

ES5 示例代码：

```js
var phone = require('yunpian-sdk').phone;

phone('+8613312345678'); // true
phone('13312341234'); // true
phone('13212345678', 'CHN'); // true
```


## 已支持的接口

### USER - 账户API

API文档参考： <https://www.yunpian.com/api2.0/user.html>


ES7 示例：

```js
import {USER} from 'yunpian-sdk';

const user = new USER({
  apikey: 'xxxx'
});

(async() => {
  const user = await user.get();
  // xxxx

  const result = await user.set({
    emergency_contact: 'Willin',
    emergency_mobile: '1xxxxxxxxxx'
  });
  // xxxx
})();

```

### TPL - 模板API

API文档参考： <https://www.yunpian.com/api2.0/tpl.html>

### SMS - 短信API

API文档参考： <https://www.yunpian.com/api2.0/sms.html>

ES7 示例：

```js
import {SMS} from 'yunpian-sdk';

const sms = new SMS({
  apikey: 'xxxx'
});

(async() => {
  console.log(await sms.singleSend({
    mobile: 'xxxx',
    text: '【xxxx】您的验证码是：123456 （验证码10分钟内有效），请勿将验证码泄露给其他人。如非本人操作，请忽略本短信。'
  }));
})();

```

### VOICE - 语音API

API文档参考： <https://www.yunpian.com/api2.0/voice.html>

### FLOW - 流量API

API文档参考： <https://www.yunpian.com/api2.0/flow.html>


## License

MIT

通过支付宝捐赠：

![qr](https://cloud.githubusercontent.com/assets/1890238/15489630/fccbb9cc-2193-11e6-9fed-b93c59d6ef37.png)
