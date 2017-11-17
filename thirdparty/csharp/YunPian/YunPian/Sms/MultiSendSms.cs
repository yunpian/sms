using System;
using System.Collections.Generic;
using System.Text;

namespace YunPian.Sms
{
    public class MultiSendSms
    {
        /// <summary>
        ///     接收的手机号；发送多个手机号请以逗号分隔，一次不要超过1000个；
        /// </summary>
        public List<string> Mobile { get; set; }

        /// <summary>
        ///     已审核短信模板，多个已审核短信模板请使用UTF-8做urlencode；
        ///     使用逗号分隔，一次不要超过1000条且已审核短信模板条数必须与手机号个数相等
        /// </summary>
        public List<string> Text { get; set; }

        /// <summary>
        ///     其它附加参数
        /// </summary>
        public SendSmsOption Option { get; set; }
    }
}
