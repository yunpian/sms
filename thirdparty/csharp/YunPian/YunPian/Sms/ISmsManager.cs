using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;
using JetBrains.Annotations;

namespace YunPian.Sms
{
    public interface ISmsManager
    {
        /// <summary>
        ///     单条发送
        ///     一次发送一条短信，常用于短信验证、找回密码、短信登录、监控报警
        /// </summary>
        /// <param name="sms"></param>
        /// <returns></returns>
        Task<SmsResult> Send(SingleSendSms sms);

        /// <summary>
        ///     批量发送相同内容
        ///     批量发送订单状态通知，活动信息群发
        /// </summary>
        /// <param name="sms"></param>
        /// <returns></returns>
        Task<SmsResult> Send(BatchSendSms sms);

        /// <summary>
        ///     批量发送不同内容
        ///     批量发送短信内容带变量的订单状态通知，活动信息群发
        /// </summary>
        /// <param name="sms"></param>
        /// <returns></returns>
        Task<SmsResult> Send(MultiSendSms sms);
    }
}
