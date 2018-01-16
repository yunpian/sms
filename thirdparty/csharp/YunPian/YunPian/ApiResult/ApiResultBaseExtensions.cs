using System;
using System.Collections.Generic;
using System.Text;

namespace YunPian.ApiResult
{
    public static class ApiResultBaseExtensions
    {
        /// <summary>
        ///     系统返回码
        /// http://www.yunpian.com/api2.0/api-recode.html
        // code = 0:	正确返回。可以从api返回的对应字段中取数据。
        // code > 0:	调用API时发生错误，需要开发者进行相应的处理。
        // -50 < code <= -1:	权限验证失败，需要开发者进行相应的处理。
        // code <= -50:	系统内部错误，请联系技术支持，调查问题原因并获得解决方案。
        /// </summary>
        /// <param name="result"></param>
        /// <returns></returns>
        public static bool IsSucceed(this ApiResultBase result)
        {
            return result?.Http_Status_Code == 0;
        }
    }
}
