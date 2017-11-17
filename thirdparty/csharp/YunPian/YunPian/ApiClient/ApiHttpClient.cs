using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace YunPian.ApiClient
{
    internal class ApiHttpClient
    {
        public async Task<TResult> PostAsync<TResult>(string url,
            FormUrlEncodedContent content) where TResult : class
        {
            using (var client = new HttpClient())
            {
                var response = await client.PostAsync(url, content);
                return JsonConvert.DeserializeObject<TResult>(await response.Content.ReadAsStringAsync());
            }
        }
    }
}
