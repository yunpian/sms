using System;
using System.Collections.Generic;
using System.Text;
using YunPian.ApiResult;

namespace YunPian.Account
{
    public class Account : ApiResultBase
    {
        /// <summary>
        ///     用户名
        /// </summary>
        public string Nick { get; set; }

        /// <summary>
        ///     注册时间
        /// </summary>
        public DateTime Gmt_Created { get; set; }

        /// <summary>
        ///     手机号
        /// </summary>
        public string Mobile { get; set; }

        /// <summary>
        ///     邮箱
        /// </summary>
        public string Email { get; set; }

        /// <summary>
        ///     IP白名单，推荐使用
        /// </summary>
        public string Ip_WhiteList { get; set; }

        /// <summary>
        ///     api版本号
        /// </summary>
        public string Api_Version { get; set; }

        /// <summary>
        ///     账户剩余条数或者剩余金额（根据账户类型）
        /// </summary>
        public string Balance { get; set; }

        /// <summary>
        ///     剩余条数或剩余金额低于该值时提醒
        /// </summary>
        public long Alarm_Balance { get; set; }

        /// <summary>
        ///     紧急联系人
        /// </summary>
        public string Emergency_Contact { get; set; }

        /// <summary>
        ///     紧急联系人电话
        /// </summary>
        public string Emergency_Mobile { get; set; }
    }
}
