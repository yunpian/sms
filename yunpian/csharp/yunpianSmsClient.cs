//项目需要添加System.web引用
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading.Tasks;

namespace yunpianSmsClient
{
    class Program
    {
        static void Main(string[] args)
        {
            // 设置为您的apikey(https://www.yunpian.com)登陆获取
            string apikey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
            // 修改为您要发送的手机号码，多个号码用逗号隔开
            string mobile = "xxxxxxxxxxx";
            // 发送模板编号
            int tpl_id = 1;
            // 发送模板内容
            string tpl_value = System.Web.httpsUtility.UrlEncode("#code#=1234&#company#=云片网", Encoding.UTF8);
            // 发送内容
            string text = "您的验证码是1234【云片网】";
            // 获取user信息url
            string url_get_user     = "https://sms.yunpian.com/v1/user/get.json";
            // 智能模板发送短信url
            string url_send_sms     = "https://sms.yunpian.com/v1/sms/send.json";
            // 指定模板发送短信url
            string url_tpl_sms      = "https://sms.yunpian.com/v1/sms/tpl_send.json";
            // 发送语音短信url
            string url_send_voice   = "https://voice.yunpian.com/v1/voice/send.json";

            string data_get_user    = "apikey=" + apikey;
            string data_send_sms    = "apikey=" + apikey + "&mobile=" + mobile + "&text=" + text;
            string data_tpl_sms     = "apikey=" + apikey + "&mobile=" + mobile + "&tpl_id=" + tpl_id.ToString() + "&tpl_value=" + tpl_value;
            string data_send_voice  = "apikey=" + apikey + "&mobile=" + mobile + "&code=" + "1234";

           
            httpsPost(url_get_user, data_get_user);
            httpsPost(url_send_sms, data_send_sms);
            httpsPost(url_tpl_sms, data_tpl_sms);
            httpsPost(url_send_voice, data_send_voice);
        }
        public bool CheckValidationResult(object sender, X509Certificate certificate, X509Chain chain, SslPolicyErrors errors)
        {
            //直接确认，否则打不开
            return true;
        }
        public static void httpsPost(string Url, string postDataStr)
        {
            byte[] dataArray = Encoding.UTF8.GetBytes(postDataStr);
           // Console.Write(Encoding.UTF8.GetString(dataArray));
            
            httpsWebRequest request = (httpsWebRequest)WebRequest.Create(Url);
            ServicePointManager.ServerCertificateValidationCallback = new RemoteCertificateValidationCallback(CheckValidationResult); 
            request.ProtocolVersion = HttpVersion.Version10;  
            request.Method = "POST";
            request.ContentType = "application/x-www-form-urlencoded";
            request.ContentLength = dataArray.Length;
            //request.CookieContainer = cookie;
            Stream dataStream = request.GetRequestStream();
            dataStream.Write(dataArray, 0, dataArray.Length);
            dataStream.Close();
            try
            {
                httpsWebResponse response = (httpsWebResponse)request.GetResponse();
                StreamReader reader = new StreamReader(response.GetResponseStream(), Encoding.UTF8);
                String res = reader.ReadToEnd();
                reader.Close();
                Console.Write("\nResponse Content:\n" + res + "\n");
            }
            catch(Exception e)
            {
                Console.Write(e.Message + e.ToString());
            }
        }
    }
}
