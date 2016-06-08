/**
 * Created by cowpanda on 6/8/16.
 */
'use strict';
var _ = require('underscore');
var util = require('util');
var restify = require('restify');
var utils = require('../common');
var Promise = require('bluebird');
var config = require('../config').v2;

var smsInstance = {};

function smsProvider(apiKey) {
    var c = restify.createStringClient({url: config.smsHost, userAgent: config.defaultUserAgent});
    this.client = c;
    this.apiKey = apiKey;
    return this;
}

/**
 * 单个发送
 * @param data {mobile:"?",text:?}
 */
smsProvider.prototype.sendSingleSms = function (data) {
    if (!data.mobile || data.mobile.length < 1) {
        throw new Error("「手机号不能为空」!");
    }

    if (!data.text) {
        throw new Error("「短信内容不能为空」!");
    }

    var self = this;
    return beginSendRequest(data, config.smsSingleSendPath, self);
};

/**
 * 批量发送
 * @param data {mobile:"?,?,?",text:?}
 */
smsProvider.prototype.sendBatchSms = function (data) {
    if (!data.mobile || data.mobile.length < 1) {
        throw new Error("「手机号不能为空」!");
    }

    if (!data.text) {
        throw new Error("「短信内容不能为空」!");
    }

    var self = this;
    return beginSendRequest(data, config.smsBatchSendPath, self);
};

/**
 * 个性化发送
 * @param data {mobile:"?,?",text:"?,?"}
 */
smsProvider.prototype.sendMultiSms = function (data) {
    if (!data.mobile || data.mobile.length < 1) {
        throw new Error("「手机号不能为空」!");
    }

    if (!data.text) {
        throw new Error("「短信内容不能为空」!");
    }

    var tmpMobile = data.mobile.split(',');
    if (tmpMobile.length > config.batchSendAllowMobileCount) {
        throw new Error("「发送的手机号不能超过" + config.batchSendAllowMobileCount + "个」!");
    }
    var tmpText = data.mobile.split(',');
    if (tmpMobile.length != tmpText.length) {
        throw new Error("「手机号个数必须与短信内容条数相等」!");
    }

    var self = this;
    return beginSendRequest(data, config.smsMultiSendPath, self);
}

/**
 * 指定模板单发
 * ref:https://www.yunpian.com/api2.0/sms.html#cc2
 * @param data {mobile:?,tpl_id:?,tpl_value:?}
 */
smsProvider.prototype.sendSingleTplSms = function (data) {
    if (!data.mobile || data.mobile.length < 1) {
        throw new Error("「手机号不能为空」!");
    }

    if (!data.tpl_id) {
        throw new Error("「模板Id不能为空」!");
    }

    if (!data.tpl_value) {
        throw new Error("「模板内容不能为空」!");
    }

    var self = this;
    return beginSendRequest(data, config.smsTplSingleSendPath, self);
}

/**
 * 指定模板群发 （不推荐使用）
 * @param data
 */
smsProvider.prototype.sendMutiTplSms = function (data) {
    if (!data.mobile || data.mobile.length < 1) {
        throw new Error("「手机号不能为空」!");
    }

    if (!data.tpl_id) {
        throw new Error("「模板Id不能为空」!");
    }

    if (!data.tpl_value) {
        throw new Error("「模板内容不能为空」!");
    }

    var self = this;
    return beginSendRequest(data, config.smsTplBatchSendPath, self);
}

/**
 * 获取状态报告
 * ref:https://www.yunpian.com/api2.0/sms.html#c4
 * @param data {page_size:[option]}
 */
smsProvider.prototype.getSmsStatusReport = function (data) {
    var self = this;
    if (!data) {
        data = {page_size: 20};
    }

    return beginSendRequest(data, config.smsSendStatusReportPath, self);
}

/**
 * 查询短信发送记录
 * ref:https://www.yunpian.com/api2.0/sms.html#c9
 * @param data {mobile:[option],start_time:?,end_time:?}
 */
smsProvider.prototype.getSmsSendRecord = function (data) {
    if (!data.start_time) {
        throw new Error("「短信发送开始时间不能为空」!");
    }

    if (!data.end_time) {
        throw new Error("「短信发送结束时间不能为空」!");
    }

    var self = this;
    return beginSendRequest(data, config.smsSendRecordPath, self);
}


function beginSendRequest(data, path, self) {
    var postData = getFormatPost(data, path, self.apiKey);
    return new Promise(function (resolve, reject) {
        self.client.post(postData, function (err, req, res, obj) {
            if (err) {
                reject(err);
                return;
            }

            resolve(JSON.parse(obj));
        });
    });
}

var needFormatKeys = ['text', 'tpl_value', 'start_time', 'end_time'];
function getFormatPost(data, path, apiKey) {
    var postData = util.format("%s?apikey=%s&", path, apiKey);
    for (var key in data) {
        if (_.contains(needFormatKeys, key)) {
            var smsContent = utils.fixedEncodeURIComponent(data[key]);
            postData += key + '=' + smsContent + '&';
            continue;
        }

        postData += key + '=' + data[key] + '&';// util.format(key + '=%s&', data[key]);
    }

    var res = postData.substr(0, postData.lastIndexOf('&'));
    return res;
}

function getProviderWithApiKey(apiKey) {
    if (!apiKey) {
        throw new Error("「apiKey不能为空」!");
    }

    if (smsInstance.v2) {
        return smsInstance.v2;
    }

    var instance = new smsProvider(apiKey);
    smsInstance.v2 = instance;
    return smsInstance.v2;
}

module.exports = {
    initWithKey: getProviderWithApiKey
};
