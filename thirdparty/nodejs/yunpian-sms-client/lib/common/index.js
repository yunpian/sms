/**
 * Created by cowpanda on 6/8/16.
 */
'use strict';

var fs = require('fs');
var os = require('os');
var path = require('path');
var apiVersion = require('../../package').version;

/**
 * 默认userAgent--若用户未设置
 * @returns {string}
 */
function defaultUserAgent() {
    var UA = 'yunpian-sms-client/' + apiVersion +
        ' (' + os.arch() + '-' + os.platform() + '; ' +
        'v8/' + process.versions.v8 + '; ' +
        'OpenSSL/' + process.versions.openssl + ') ' +
        'node/' + process.versions.node;
    return (UA);
}

/**
 * 转换编码
 */
function fixedEncodeURIComponent(str) {
    return encodeURIComponent(str).replace(/[!'()]/g, escape).replace(/\*/g, "%2A");
}

module.exports = {
    apiVersion: apiVersion,
    defaultUserAgent: defaultUserAgent,
    fixedEncodeURIComponent: fixedEncodeURIComponent
}