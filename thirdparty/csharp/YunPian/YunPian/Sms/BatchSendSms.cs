using System;
using System.Collections.Generic;
using System.Text;

namespace YunPian.Sms
{
    public class BatchSendSms
    {
        /// <summary>
        ///     接收的手机号；发送多个手机号请以逗号分隔，一次不要超过1000个；
        /// </summary>
        public List<string> Mobile { get; set; }

        /// <summary>
        ///     已审核短信模板
        /// </summary>
        public string Text { get; set; }

        /// <summary>
        ///     其它附加参数
        /// </summary>
        public SendSmsOption Option { get; set; }
    }
}
