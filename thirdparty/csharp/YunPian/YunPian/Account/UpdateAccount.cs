using System;
using System.Collections.Generic;
using System.Text;

namespace YunPian.Account
{
    /// <summary>
    ///     修改账号信息
    /// </summary>
    public class UpdateAccount
    {
        /// <summary>
        ///     剩余条数或剩余金额低于该值时提醒
        /// </summary>
        public long? Alarm_Balance { get; set; }

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
