using System;
using System.Collections.Generic;
using System.Text;
using YunPian.ApiResult;

namespace YunPian.Sms
{
    public class SendResultItem : ApiResultBase
    {
        /// <summary>
        ///     发送成功短信的计费条数(计费条数：70个字一条，超出70个字时按每67字一条计费)
        /// </summary>
        public int Count { get; set; }

        /// <summary>
        ///     扣费金额，单位：元，类型：双精度浮点型/double
        /// </summary>
        public double Fee { get; set; }

        /// <summary>
        ///     计费单位
        /// </summary>
        public string Unit { get; set; }

        /// <summary>
        ///     发送手机号
        /// </summary>
        public string Mobile { get; set; }

        /// <summary>
        ///     短信id，64位整型， 对应Java和C#的Long，不可用int解析
        /// </summary>
        public long Sid { get; set; }
    }
}
