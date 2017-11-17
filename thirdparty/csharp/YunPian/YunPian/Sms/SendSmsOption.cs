using System;
using System.Collections.Generic;
using System.Text;

namespace YunPian.Sms
{
    public class SendSmsOption
    {
        /// <summary>
        ///     下发号码扩展号，纯数字
        /// </summary>
        public string Extend { get; set; }


        /// <summary>
        ///     该条短信在您业务系统内的ID，如订单号或者短信发送记录流水号。
        ///     默认不开放，如有需要请联系客服申请。
        /// </summary>
        public string Uid { get; set; }

        /// <summary>
        ///     短信发送后将向这个地址推送(运营商返回的)发送报告。
        ///     如推送地址固定，建议在"数据推送与获取”做批量设置。
        ///     如后台已设置地址，且请求内也包含此参数，将以请求内地址为准
        /// </summary>
        public string Callback_Url { get; set; }
    }
}
