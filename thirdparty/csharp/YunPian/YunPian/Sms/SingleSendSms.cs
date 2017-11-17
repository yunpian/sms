using System;
using System.Collections.Generic;
using System.Text;

namespace YunPian.Sms
{
    public class SingleSendSms
    {
        /// <summary>
        ///     接收的手机号
        /// </summary>
        public string Mobile { get; set; }

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
