/**
 * Created by cowpanda on 6/8/16.
 */
'use strict';
var fs = require('fs');
var os = require('os');
var path = require('path');
//var json = require('../../package');
var apiVersion = require('../../package').version;//JSON.parse(fs.readFileSync(path.normalize(__dirname + '../../package.json'), 'utf8')).version;
var userAgent = '';
(function () {
    var UA = 'yunpian-sms-client/' + apiVersion +
        ' (' + os.arch() + '-' + os.platform() + '; ' +
        'v8/' + process.versions.v8 + '; ' +
        'OpenSSL/' + process.versions.openssl + ') ' +
        'node/' + process.versions.node;
    userAgent = UA;
})();

var config = {
    v1: {
        smsHost: 'http://yunpian.com',
        smsDefaultSendPath: '/v1/sms/send.json',
        smsTplSendPath: '/v1/sms/tpl_send.json'
    },
    v2: {
        smsHost: 'https://sms.yunpian.com',
        smsSingleSendPath: '/v2/sms/single_send.json',
        smsBatchSendPath: '/v2/sms/batch_send.json',
        smsTplSingleSendPath: '/v2/sms/tpl_single_send.json',
        smsTplBatchSendPath: '/v2/sms/tpl_batch_send.json',
        smsAccountInfoPath: '/v2/user/get.json',
        smsMultiSendPath: '/v2/sms/multi_send.json',
        smsSendStatusReportPath: '/v2/sms/pull_status.json',
        smsSendRecordPath: '/v2/sms/get_record.json'
    },
    apiVersion: apiVersion,
    defaultUserAgent: userAgent,
    batchSendAllowMobileCount: 1000
}

module.exports = config;