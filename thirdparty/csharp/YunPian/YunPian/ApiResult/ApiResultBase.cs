using System;
using System.Collections.Generic;
using System.Text;

namespace YunPian.ApiResult
{
    public class ApiResultBase
    {
        /// <summary>
        ///     调用失败http返回码设为400
        /// </summary>
        public int Http_Status_Code { get; set; }

        /// <summary>
        ///     系统返回码
        /// </summary>
        /// http://www.yunpian.com/api2.0/api-recode.html
        // code = 0:	正确返回。可以从api返回的对应字段中取数据。
        // code > 0:	调用API时发生错误，需要开发者进行相应的处理。
        // -50 < code <= -1:	权限验证失败，需要开发者进行相应的处理。
        // code <= -50:	系统内部错误，请联系技术支持，调查问题原因并获得解决方案。
        public int Code { get; set; }

        /// <summary>
        ///     错误描述
        /// </summary>
        public string Msg { get; set; }

        /// <summary>
        ///     具体错误描述或解决方法
        /// </summary>
        public string Detail { get; set; }
    }
}
