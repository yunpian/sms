/**
 * Created by lgt on 6/8/16.
 */
'use strict';
var util = require('util');
var restify = require('restify');
var utils = require('../common');

function yunpainSMSClient(options) {
    if (!options.apiKey) {
        throw new Error("「apiKey不能为空」!");
    }

    if (!options.mobile || options.mobile.length < 1) {
        throw new Error("「手机号不能为空」!");
    }

    if (!util.isArray(options.mobile)) {
        options.mobile = [options.mobile];
    }

    this.url = options.url || 'http://yunpian.com';
    this.apiKey = options.apiKey;
    this.mobile = options.mobile.join(',');
    this.sendContent = options.sendContent;
    this.userAgent = options.userAgent || utils.defaultUserAgent();
    this.templateId = options.templateId || undefined;
    this.templateValue = options.templateValue || undefined;
}

/**
 * 默认通用发送短信的入口
 * @param query
 * @param callback
 */
yunpainSMSClient.prototype.send = function (query, callback) {
    var client = restify.createStringClient({url: this.url, userAgent: this.userAgent});
    client.post(query, function (err, req, res, obj) {
        if (err) {
            callback(err);
            return;
        }

        callback(null, obj);
    });
};

/**
 * 普通发短信
 * @param path 可选,默认是使用又片网提供的模板处理api path;
 * @param callback
 */
yunpainSMSClient.prototype.sendSMS = function (path, callback) {
    if (typeof (path) === 'function') {
        callback = path;
        path = undefined;
    }

    var routePath = path || '/v1/sms/send.json';
    var urlEncodeText = utils.fixedEncodeURIComponent(this.sendContent);
    var queryParam = util.format("%s?apikey=%s&text=%s&mobile=%s", routePath, this.apiKey, urlEncodeText, this.mobile);
    this.send(queryParam, callback);
};

/**
 * 根据模板信息发送信息
 * @param path 可选,默认是使用又片网提供的模板处理api path;
 * @param callback
 */
yunpainSMSClient.prototype.sendSMSByTemplate = function (path, callback) {
    if (typeof (path) === 'function') {
        callback = path;
        path = undefined;
    }

    if (!this.templateId || !this.templateValue) {
        var err = new Error('模板信息不能为空!');
        callback(err);
        return;
    }

    var routePath = path || '/v1/sms/tpl_send.json';
    var queryParam = util.format("%s?apikey=%s&text=%s&mobile=%s&tpl_id=%s&tpl_value=%s",
        routePath,
        this.apiKey,
        this.sendContent,
        this.mobile,
        this.templateId,
        utils.fixedEncodeURIComponent(this.templateValue)
    );

    this.send(queryParam, callback);
};



module.exports = yunpainSMSClient;
