## 云片短信API文档(2.0)
.NET Standard 2.0 框架

* 设计之初就考虑了依赖注入,方便集成各种系统.
* 由于短信的特殊性,请替换测试的相关代码后再进行单元测试.
* 详细见测试代码

### 使用方法

``` csharp
var _accountManager = new AccountManager(new DefaultYunPianConfiguration
{
	ApiKey = "your api key"
});
var accountInfo = await _accountManager.GetAsync();


var smsManager = new SmsManager(new DefaultYunPianConfiguration
{
	ApiKey = "your api key"
});
var smsResult = await smsManager.Send(new BatchSendSms()
{
	Mobile = new List<string>
	{
		"13800138000",
		"13800138001"
	},
	Text = "尊敬的用户，您的帐号于2017-01-01成功充值100元，如有疑问请联系客服。"
});
```

### 依赖注入(autofac)

``` csharp
var builder = new ContainerBuilder();
builder.RegisterAssemblyTypes(Assembly.GetExecutingAssembly()).AsImplementedInterfaces();

builder.RegisterAssemblyTypes(Assembly.GetAssembly(typeof(IYunPianConfiguration)))
	.AsImplementedInterfaces();

builder.Register(c => new DefaultYunPianConfiguration
{
	ApiKey = "your api key",
}).As<IYunPianConfiguration>().SingleInstance();

IocContainer = builder.Build();
```

### 账户API
``` csharp
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


public class Account : ApiResultBase
{
	/// <summary>
	///     用户名
	/// </summary>
	public string Nick { get; set; }

	/// <summary>
	///     注册时间
	/// </summary>
	public DateTime Gmt_Created { get; set; }

	/// <summary>
	///     手机号
	/// </summary>
	public string Mobile { get; set; }

	/// <summary>
	///     邮箱
	/// </summary>
	public string Email { get; set; }

	/// <summary>
	///     IP白名单，推荐使用
	/// </summary>
	public string Ip_WhiteList { get; set; }

	/// <summary>
	///     api版本号
	/// </summary>
	public string Api_Version { get; set; }

	/// <summary>
	///     账户剩余条数或者剩余金额（根据账户类型）
	/// </summary>
	public string Balance { get; set; }

	/// <summary>
	///     剩余条数或剩余金额低于该值时提醒
	/// </summary>
	public long Alarm_Balance { get; set; }

	/// <summary>
	///     紧急联系人
	/// </summary>
	public string Emergency_Contact { get; set; }

	/// <summary>
	///     紧急联系人电话
	/// </summary>
	public string Emergency_Mobile { get; set; }
}
```

### 短信API
``` csharp
public interface ISmsManager
{
	/// <summary>
	///     单条发送
	///     一次发送一条短信，常用于短信验证、找回密码、短信登录、监控报警
	/// </summary>
	/// <param name="sms"></param>
	/// <returns></returns>
	Task<SmsResult> Send(SingleSendSms sms);

	/// <summary>
	///     批量发送相同内容
	///     批量发送订单状态通知，活动信息群发
	/// </summary>
	/// <param name="sms"></param>
	/// <returns></returns>
	Task<SmsResult> Send(BatchSendSms sms);

	/// <summary>
	///     批量发送不同内容
	///     批量发送短信内容带变量的订单状态通知，活动信息群发
	/// </summary>
	/// <param name="sms"></param>
	/// <returns></returns>
	Task<SmsResult> Send(MultiSendSms sms);
}

public class SingleSendSms
{
	/// <summary>
	///     接收的手机号
	/// </summary>
	public string Mobile { get; set; }

	/// <summary>
	///     已审核短信模板
	/// </summary>
	public string Text { get; set; }

	/// <summary>
	///     其它附加参数
	/// </summary>
	public SendSmsOption Option { get; set; }
}

public class BatchSendSms
{
	/// <summary>
	///     接收的手机号；发送多个手机号请以逗号分隔，一次不要超过1000个；
	/// </summary>
	public List<string> Mobile { get; set; }

	/// <summary>
	///     已审核短信模板
	/// </summary>
	public string Text { get; set; }

	/// <summary>
	///     其它附加参数
	/// </summary>
	public SendSmsOption Option { get; set; }
}

public class MultiSendSms
{
	/// <summary>
	///     接收的手机号；发送多个手机号请以逗号分隔，一次不要超过1000个；
	/// </summary>
	public List<string> Mobile { get; set; }

	/// <summary>
	///     已审核短信模板，多个已审核短信模板请使用UTF-8做urlencode；
	///     使用逗号分隔，一次不要超过1000条且已审核短信模板条数必须与手机号个数相等
	/// </summary>
	public List<string> Text { get; set; }

	/// <summary>
	///     其它附加参数
	/// </summary>
	public SendSmsOption Option { get; set; }
}

public class SmsResult : ApiResultBase
{
	/// <summary>
	///     成功发送总数
	/// </summary>
	public int Total_Count { get; set; }

	/// <summary>
	///     扣费金额，单位：元，类型：双精度浮点型/double
	/// </summary>
	public double Total_Fee { get; set; }

	/// <summary>
	///     计费单位
	/// </summary>
	public string Unit { get; set; }

	public IReadOnlyList<SendResultItem> Data { get; set; }
}

public class SendResultItem : ApiResultBase
{
	/// <summary>
	///     发送成功短信的计费条数(计费条数：70个字一条，超出70个字时按每67字一条计费)
	/// </summary>
	public int Count { get; set; }

	/// <summary>
	///     扣费金额，单位：元，类型：双精度浮点型/double
	/// </summary>
	public double Fee { get; set; }

	/// <summary>
	///     计费单位
	/// </summary>
	public string Unit { get; set; }

	/// <summary>
	///     发送手机号
	/// </summary>
	public string Mobile { get; set; }

	/// <summary>
	///     短信id，64位整型， 对应Java和C#的Long，不可用int解析
	/// </summary>
	public long Sid { get; set; }
}
```
