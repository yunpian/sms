/**
 * Created by cowpanda on 8/11/15.
 */
var yunpainSMSClient = require('../lib');

var c = new yunpainSMSClient({
    apiKey: 'your appkey',
    sendContent: '【your sigure】您的验证码是23405。如非本人操作，请忽略本短信',
    mobile: ['your number']
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
