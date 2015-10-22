package yunpian

import (
	"testing"

	. "github.com/smartystreets/goconvey/convey"
)

var yourapikey = "请在这里填写你的API KEY用于测试"
var api *YunpianAPI
var yunpianAPI *YunpianAPI

func TestInit(t *testing.T) {
	api = &YunpianAPI{}
	yunpianAPI = NewYunpianAPI(yourapikey)
}

func Testgeturl(t *testing.T) {
	Convey("geturl", t, func() {
		So(geturl(URL_USER_GET), ShouldEqual, "http://yunpian.com:80/v1/user/get.json")
	})
}

func TestNewYunpianAPI(t *testing.T) {
	Convey("NewYunpianAPI", t, func() {
		newAPI := NewYunpianAPI(yourapikey)
		So(newAPI.APIKey, ShouldEqual, yourapikey)
	})
}

func TestUserGet(t *testing.T) {
	Convey("UserGet Success", t, func() {
		_, err := yunpianAPI.UserGet()
		So(err, ShouldBeNil)
	})

	Convey("UserGet Fail", t, func() {
		_, err := api.UserGet()
		So(err, ShouldNotBeNil)
	})
}

func TestUserSet(t *testing.T) {
	Convey("UserSet Success", t, func() {
		err := NewYunpianAPI(yourapikey).UserSet(UserSetInfo{AlarmBalance: 100, EmergencyContact: "love@shesuyo.com", EmergencyMobile: "13250061802"})
		So(err, ShouldBeNil)
	})

	Convey("UserSet Fail", t, func() {
		err := api.UserSet(UserSetInfo{AlarmBalance: 100, EmergencyContact: "love@shesuyo.com", EmergencyMobile: "13250061802"})
		So(err, ShouldNotBeNil)
	})
}

func TestTplGetDefault(t *testing.T) {
	Convey("TplGetDefault Success", t, func() {
		_, err := yunpianAPI.TplGetDefault(1)
		So(err, ShouldBeNil)
	})

	Convey("TplGetDefault Fail", t, func() {
		_, err := api.TplGetDefault(1)
		So(err, ShouldNotBeNil)
	})
}

func TestTplGetDefaultAll(t *testing.T) {
	Convey("TplGetDefaultAll Success", t, func() {
		_, err := yunpianAPI.TplGetDefaultAll()
		So(err, ShouldBeNil)
	})

	Convey("TplGetDefaultAll Fail", t, func() {
		_, err := api.TplGetDefaultAll()
		So(err, ShouldNotBeNil)
	})
}

func TestTplAdd(t *testing.T) {
	Convey("TplAdd Success", t, func() {
		_, err := yunpianAPI.TplAdd("【你公司的名字】您的验证码是#code#", 0)
		So(err, ShouldBeNil)
	})

	Convey("TplAdd Fail", t, func() {
		_, err := api.TplAdd("【你公司的名字】您的验证码是#code#", 0)
		So(err, ShouldNotBeNil)
	})
}

func TestTplGet(t *testing.T) {
	Convey("TestTplGet Success", t, func() {
		_, err := yunpianAPI.TplGet(1)
		So(err, ShouldBeNil)
	})

	Convey("TestTplGet Fail", t, func() {
		_, err := api.TplGet(1)
		So(err, ShouldNotBeNil)
	})
}

func TestTplGetALL(t *testing.T) {
	Convey("TplGetALL Success", t, func() {
		_, err := yunpianAPI.TplGetALL()
		So(err, ShouldBeNil)
	})

	Convey("TplGetALL Fail", t, func() {
		_, err := api.TplGetALL()
		So(err, ShouldNotBeNil)
	})
}

func TestSmsSend(t *testing.T) {
	Convey("SmsSend Success", t, func() {
		_, err := yunpianAPI.SmsSend(SMSSendInfo{Mobile: "13250061802", Text: "【云片网】您的验证码是970702"})
		So(err, ShouldBeNil)
	})

	Convey("SmsSend Fail", t, func() {
		_, err := api.SmsSend(SMSSendInfo{Mobile: "13250061802", Text: "【云片网】您的验证码是970702"})
		So(err, ShouldNotBeNil)
	})
}

func TestSmsTplSend(t *testing.T) {
	Convey("SmsTplSend Success", t, func() {
		//使用1模板发送
		_, err := yunpianAPI.SmsTplSend(SMSTplSendInfo{Tpl_ID: 1, Mobile: "13250061802", Tpl_Value: "#code#=970702&#company#=云片网"})
		So(err, ShouldBeNil)
	})

	Convey("SmsTplSend Fail", t, func() {
		_, err := api.SmsTplSend(SMSTplSendInfo{Tpl_ID: 1, Mobile: "13250061802", Tpl_Value: "#code#=970702&#company#=云片网"})
		So(err, ShouldNotBeNil)
	})
}

func TestVoiceSend(t *testing.T) {
	Convey("VoiceSend Success", t, func() {
		_, err := yunpianAPI.VoiceSend(VoiceSendInfo{Mobile: "13250061802", Code: "970702"})
		So(err, ShouldBeNil)
	})

	Convey("VoiceSend Fail", t, func() {
		_, err := api.VoiceSend(VoiceSendInfo{Mobile: "13250061802", Code: "970702"})
		So(err, ShouldNotBeNil)
	})
}
