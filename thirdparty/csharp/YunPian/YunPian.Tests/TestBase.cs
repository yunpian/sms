using System;
using System.Collections.Generic;
using System.Reflection;
using System.Text;
using Autofac;
using YunPian.Configuration;

namespace YunPian.Tests
{
    public class TestBase
    {
        protected IContainer IocContainer { get; }

        public TestBase()
        {
            var builder = new ContainerBuilder();
            builder.RegisterAssemblyTypes(Assembly.GetExecutingAssembly()).AsImplementedInterfaces();

            builder.RegisterAssemblyTypes(Assembly.GetAssembly(typeof(IYunPianConfiguration)))
                .AsImplementedInterfaces();

            builder.Register(c => new DefaultYunPianConfiguration
            {
                ApiKey = "your api key",
            }).As<IYunPianConfiguration>().SingleInstance();

            IocContainer = builder.Build();
        }
    }
}
