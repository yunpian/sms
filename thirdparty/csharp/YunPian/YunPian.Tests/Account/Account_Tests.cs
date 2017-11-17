using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;
using Autofac;
using Shouldly;
using Xunit;
using YunPian.Account;
using YunPian.ApiResult;
using YunPian.Configuration;

namespace YunPian.Tests.Account
{
    public class Account_Tests : TestBase
    {
        private readonly IAccountManager _accountManager;

        public Account_Tests()
        {
            _accountManager = IocContainer.Resolve<IAccountManager>();
        }

        [Fact]
        public async Task GetAccountInfo_Test()
        {
            //Act
            var result = await _accountManager.GetAsync();

            //Assert
            result.IsSucceed().ShouldBeTrue();

            result.Nick.ShouldNotBeNull();
            result.Gmt_Created.ShouldNotBe(default(DateTime));
            result.Mobile.ShouldNotBeNull();
            result.Email.ShouldNotBeNull();
            result.Ip_WhiteList.ShouldNotBeNull();
            result.Api_Version.ShouldNotBeNull();
            result.Balance.ShouldNotBeNull();
            result.Alarm_Balance.ShouldNotBeNull();
            result.Emergency_Contact.ShouldNotBeNull();
            result.Emergency_Mobile.ShouldNotBeNull();
        }

        [Fact]
        public async Task Get_AccountInfo_Has_Error_Test()
        {
            //Act
            var errorAccountManager = new AccountManager(new DefaultYunPianConfiguration { ApiKey = "123456" });
            var result = await errorAccountManager.GetAsync();

            //Assert
            result.IsSucceed().ShouldBeFalse();

            result.Nick.ShouldBeNull();
            result.Gmt_Created.ShouldBe(default(DateTime));
            result.Mobile.ShouldBeNull();
            result.Email.ShouldBeNull();
            result.Ip_WhiteList.ShouldBeNull();
            result.Api_Version.ShouldBeNull();
            result.Balance.ShouldBeNull();
            result.Alarm_Balance.ShouldBe(0);
            result.Emergency_Contact.ShouldBeNull();
            result.Emergency_Mobile.ShouldBeNull();
        }


        [Fact]
        public async Task Set_AccountInfo_Test()
        {
            //Act
            var result = await _accountManager.UpdateAsync(new UpdateAccount
            {
                Alarm_Balance = 100,
                Emergency_Contact = "小明",
                Emergency_Mobile = "13800138000"
            });

            //Assert
            result.IsSucceed().ShouldBeTrue();

            result.Nick.ShouldNotBeNull();
            //result.Gmt_Created.ShouldNotBe(default(DateTime));
            result.Mobile.ShouldNotBeNull();
            result.Email.ShouldNotBeNull();
            result.Ip_WhiteList.ShouldNotBeNull();
            result.Api_Version.ShouldNotBeNull();
            result.Balance.ShouldNotBeNull();
            result.Alarm_Balance.ShouldNotBeNull();
            result.Emergency_Contact.ShouldNotBeNull();
            result.Emergency_Mobile.ShouldNotBeNull();

            result.Alarm_Balance.ShouldBe(100);
            result.Emergency_Contact.ShouldBe("小明");
            result.Emergency_Mobile.ShouldBe("13800138000");
        }

        [Fact]
        public async Task Set_AccountInfo_Must_Pass_Less_One_Argument_Test()
        {
            //Assert
            var ex = await Assert.ThrowsAsync<ArgumentException>(async () =>
                await _accountManager.UpdateAsync(new UpdateAccount()));

            ex.ShouldNotBeNull();
            ex.ShouldBeOfType<ArgumentException>();
            //ex.Message.ShouldBe("请至少传入一个欲修改的账户信息");
        }
    }
}
