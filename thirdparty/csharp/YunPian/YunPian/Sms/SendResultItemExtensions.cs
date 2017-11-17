using System;
using System.Collections.Generic;
using System.Text;
using YunPian.ApiResult;

namespace YunPian.Sms
{
    public static class SendResultItemExtensions
    {
        public static SmsResult ToSmsResult(this SendResultItem item)
        {
            return new SmsResult
            {
                Http_Status_Code = item.Http_Status_Code,
                Code = item.Code,
                Msg = item.Msg,
                Detail = item.Detail,

                Total_Count = item.Count,
                Total_Fee = item.Fee,
                Data = item.IsSucceed() ? new List<SendResultItem> { item } : null
            };
        }
    }
}
