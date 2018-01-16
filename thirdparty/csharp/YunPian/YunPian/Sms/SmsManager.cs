using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;
using YunPian.ApiClient;
using YunPian.Configuration;
using YunPian.Helper;

namespace YunPian.Sms
{
    public class SmsManager : ISmsManager
    {
        private readonly IYunPianConfiguration _yunPianConfiguration;

        public SmsManager(IYunPianConfiguration yunPianConfiguration)
        {
            _yunPianConfiguration = yunPianConfiguration;
        }

        /// <summary>
        ///     应用附加参数
        /// </summary>
        /// <param name="builder"></param>
        /// <param name="option"></param>
        private static void ApplySendOption(FormUrlEncodedContentBuilder builder, SendSmsOption option)
        {
            if (!string.IsNullOrWhiteSpace(option?.Extend))
            {
                builder.Add("extend", option.Extend);
            }
            if (!string.IsNullOrWhiteSpace(option?.Uid))
            {
                builder.Add("uid", option.Uid);
            }
            if (!string.IsNullOrWhiteSpace(option?.Callback_Url))
            {
                builder.Add("callback_url", option.Callback_Url);
            }
        }

        /// <summary>
        ///     单条发送
        ///     一次发送一条短信，常用于短信验证、找回密码、短信登录、监控报警
        /// </summary>
        /// <param name="sms"></param>
        /// <returns></returns>
        public async Task<SmsResult> Send(SingleSendSms sms)
        {
            const string apiUrl = "https://sms.yunpian.com/v2/sms/single_send.json";

            Check.NotNull(sms, nameof(sms));
            Check.NotNullOrWhiteSpace(sms.Mobile, nameof(sms.Mobile));
            Check.NotNullOrWhiteSpace(sms.Text, nameof(sms.Text));

            var content = new FormUrlEncodedContentBuilder
            {
                {"apikey", _yunPianConfiguration.ApiKey},
                {"mobile", sms.Mobile},
                {"text", sms.Text}
            };

            ApplySendOption(content, sms.Option);

            return (await new ApiHttpClient().PostAsync<SendResultItem>(apiUrl, content)).ToSmsResult();
        }

        /// <summary>
        ///     批量发送相同内容
        ///     批量发送订单状态通知，活动信息群发
        /// </summary>
        /// <param name="sms"></param>
        /// <returns></returns>
        public async Task<SmsResult> Send(BatchSendSms sms)
        {
            const string apiUrl = "https://sms.yunpian.com/v2/sms/batch_send.json";

            Check.NotNull(sms, nameof(sms));
            Check.NotNullOrEmpty(sms.Mobile, nameof(sms.Mobile));
            Check.NotNullOrWhiteSpace(sms.Text, nameof(sms.Text));

            var content = new FormUrlEncodedContentBuilder
            {
                {"apikey", _yunPianConfiguration.ApiKey},
                {"mobile", string.Join(",", sms.Mobile)},
                {"text", sms.Text}
            };

            ApplySendOption(content, sms.Option);

            return await new ApiHttpClient().PostAsync<SmsResult>(apiUrl, content);
        }

        /// <summary>
        ///     批量发送不同内容
        ///     批量发送短信内容带变量的订单状态通知，活动信息群发
        /// </summary>
        /// <param name="sms"></param>
        /// <returns></returns>
        public async Task<SmsResult> Send(MultiSendSms sms)
        {
            const string apiUrl = "https://sms.yunpian.com/v2/sms/multi_send.json";

            Check.NotNull(sms, nameof(sms));
            Check.NotNullOrEmpty(sms.Mobile, nameof(sms.Mobile));
            Check.NotNullOrEmpty(sms.Text, nameof(sms.Text));

            var content = new FormUrlEncodedContentBuilder
            {
                {"apikey", _yunPianConfiguration.ApiKey},
                {"mobile", string.Join(",", sms.Mobile)},
                {"text", string.Join(",", sms.Text)}
            };

            ApplySendOption(content, sms.Option);

            return await new ApiHttpClient().PostAsync<SmsResult>(apiUrl, content);
        }
    }
}
