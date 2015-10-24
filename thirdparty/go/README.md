# yunpian
云片网 GO SDK


##基本概念
```
创建一个api对象
然后对应的方式调用函数 
api.{resource}{function}
传入参数的结构体为函数名+Info
例:SmsSend(info SMSSendInfo)
返回值error为nil则是执行成功，附带的返回信息在第一个返回值中。
```

##使用需要import 本代码
``` go
import (
	"github.com/shesuyo/yunpian"
)
```

##创建一个新的云片API
``` go
api := NewYunpianAPI("你的apikey")
```

##发送手机短信验证码
``` go
api.SmsSend(SMSSendInfo{Mobile: "13250061802", Text: "【垣创科技】您的验证码是970702"})
```

##发送语音验证码
``` go
api.VoiceSend(VoiceSendInfo{Mobile: "13250061802", Text: "970702"})
```

##更多函数使用方式请查看测试函数