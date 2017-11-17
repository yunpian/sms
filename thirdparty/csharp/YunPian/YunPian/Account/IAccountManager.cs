using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;
using JetBrains.Annotations;

namespace YunPian.Account
{
    public interface IAccountManager
    {
        /// <summary>
        ///     查账户信息
        /// </summary>
        /// <returns></returns>
        Task<Account> GetAsync();

        /// <summary>
        ///     可一次修改emergency_contact、emergency_mobile和alarm_balance中的一个或多个(必须传入一个)
        /// </summary>
        /// <param name="account"></param>
        /// <returns></returns>
        Task<Account> UpdateAsync([NotNull]UpdateAccount account);
    }
}
