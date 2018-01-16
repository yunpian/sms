using System;
using System.Collections.Generic;
using System.Text;
using YunPian.ApiResult;

namespace YunPian.Sms
{
    public class SmsResult : ApiResultBase
    {
        /// <summary>
        ///     成功发送总数
        /// </summary>
        public int Total_Count { get; set; }

        /// <summary>
        ///     扣费金额，单位：元，类型：双精度浮点型/double
        /// </summary>
        public double Total_Fee { get; set; }

        /// <summary>
        ///     计费单位
        /// </summary>
        public string Unit { get; set; }

        public IReadOnlyList<SendResultItem> Data { get; set; }
    }
}
