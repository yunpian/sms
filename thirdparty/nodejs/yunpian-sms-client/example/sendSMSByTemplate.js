/**
 * Created by cowpanda on 8/11/15.
 */
var yunpainSMSClient = require('../lib');

var c = new yunpainSMSClient({
    apiKey: 'your appkey',
    templateId: 1,
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
