using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;
using YunPian.ApiClient;
using YunPian.Configuration;

namespace YunPian.Account
{
    public class AccountManager : IAccountManager
    {
        private readonly IYunPianConfiguration _yunPianConfiguration;

        public AccountManager(IYunPianConfiguration yunPianConfiguration)
        {
            _yunPianConfiguration = yunPianConfiguration;
        }
 
        /// <summary>
        ///     查账户信息
        /// </summary>
        /// <returns></returns>
        public async Task<Account> GetAsync()
        {
            const string apiUrl = "https://sms.yunpian.com/v2/user/get.json";

            return await new ApiHttpClient().PostAsync<Account>(apiUrl, new FormUrlEncodedContentBuilder
            {
                {"apikey", _yunPianConfiguration.ApiKey}
            });
        }

        /// <summary>
        ///     可一次修改emergency_contact、emergency_mobile和alarm_balance中的一个或多个(必须传入一个)
        /// </summary>
        /// <param name="account"></param>
        /// <returns></returns>
        public async Task<Account> UpdateAsync(UpdateAccount account)
        {
            const string apiUrl = "https://sms.yunpian.com/v2/user/set.json";

            if (account.Emergency_Contact == null && account.Emergency_Mobile == null && account.Alarm_Balance == null)
            {
                throw new ArgumentException("请至少传入一个欲修改的账户信息");
            }

            var content = new FormUrlEncodedContentBuilder
            {
                {"apikey", _yunPianConfiguration.ApiKey}
            };

            if (account.Emergency_Contact != null)
            {
                content.Add("emergency_contact", account.Emergency_Contact);
            }

            if (account.Emergency_Mobile != null)
            {
                content.Add("emergency_mobile", account.Emergency_Mobile);
            }

            if (account.Alarm_Balance.HasValue)
            {
                content.Add("alarm_balance", account.Alarm_Balance.Value.ToString());
            }

            return await new ApiHttpClient().PostAsync<Account>(apiUrl, content);
        }
    }
}
