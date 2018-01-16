using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;
using Autofac;
using Shouldly;
using Xunit;
using YunPian.ApiResult;
using YunPian.Sms;

namespace YunPian.Tests.Sms
{
    public class Sms_Tests : TestBase
    {
        private readonly ISmsManager _smsManagerManager;

        public Sms_Tests()
        {
            _smsManagerManager = IocContainer.Resolve<ISmsManager>();
        }

        [Fact]
        public async Task Single_Send_Test()
        {
            //Act
            var result = await _smsManagerManager.Send(new SingleSendSms
            {
                Mobile = "13800138000",
                Text = "【笔记荚】您的订单编号：123456,物流信息：654321"
            });

            //Assert
            result.IsSucceed().ShouldBeTrue();
        }

        [Fact]
        public async Task Single_Send_With_Error_Test()
        {
            //Act
            var result = await _smsManagerManager.Send(new SingleSendSms
            {
                Mobile = "13800138000",
                Text = "【中国银行】您的订单编号：123456,物流信息：654321"
            });

            //Assert
            result.IsSucceed().ShouldBeFalse();
            result.Data.ShouldBeNull();
        }


        [Fact]
        public async Task Batch_Send_Test()
        {
            //Act
            var result = await _smsManagerManager.Send(new BatchSendSms
            {
                Mobile = new List<string>
                {
                    "13800138000",
                    "13800138001"
                },
                Text = "【笔记荚】您的订单编号：123456,物流信息：654321"
            });

            //Assert
            result.IsSucceed().ShouldBeTrue();
        }

        [Fact]
        public async Task Multi_Send_Test()
        {
            //Act
            var result = await _smsManagerManager.Send(new MultiSendSms
            {
                Mobile = new List<string>
                {
                    "13800138000",
                    "13800138001"
                },
                Text = new List<string>
                {
                    "【笔记荚】您的订单编号：123456,物流信息：654321",
                    "【笔记荚】您的订单编号：654321,物流信息：123456"
                }
            });

            //Assert
            result.IsSucceed().ShouldBeTrue();
        }
    }
}
