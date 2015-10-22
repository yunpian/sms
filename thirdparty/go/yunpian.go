package yunpian

import (
	"errors"
	"fmt"
	"strconv"

	"coding.net/moss/yogo/httplib"
)

//--------------------------------------------------------------
//							变量声明
//--------------------------------------------------------------

var SCHEMES = "http://"
var HOST = "yunpian.com"
var PORT = 80
var VERSION = "v1"
var FORMAT = "json"

//1.1 查看账户信息
var URL_USER_GET = "user/get"

//1.2 修改账户信息
var URL_USER_SET = "user/set"

//2.1 取默认模板
var URL_TPL_GETDEFAULT = "tpl/get_default"

//2.2 添加模板
var URL_TPL_ADD = "tpl/add"

//2.3 取模板
var URL_TPL_GET = "tpl/get"

//2.4 修改模板
var URL_TPL_UPDATE = "tpl/update"

//2.5 删除模板
var URL_TPL_DEL = "tpl/del"

//3.1 智能匹配模板发送
var URL_SMS_SEND = "sms/send"

//3.2 获取状态报告
var URL_SMS_PULLSTATUS = "sms/pull_status"

//3.3 推送状态报告
//3.4 获取回复信息
var URL_SMS_PULLREPLY = "sms/pull_reply"

//3.5 推送回复信息
//3.6 查回复信息
var URL_SMS_GETREPLY = "sms/get_reply"

//3.7 插屏蔽词
var URL_SMS_GETBLACKWORD = "sms/get_black_word"

//3.8 指定模板发送
var URL_SMS_TPLSEND = "sms/tpl_send"

//3.9 批量个性化发送
var URL_SMS_MULTISEND = "sms/multi_send"

//4.1 发语音验证码
var URL_VOICE_SEND = "voice/send"

//4.2 获取状态报告
var URL_VOICE_PULLSTATUS = "voice/pull_status"

//4.3 推送状态报告

//--------------------------------------------------------------
//							结构体
//--------------------------------------------------------------

type YunpianAPI struct {
	APIKey string
}

type BaseStruct struct {
	Code   int
	Msg    string
	Detail string
}

type User struct {
	BaseStruct
	UserDetail UserDetail `json:"user"`
}

type UserDetail struct {
	Nick             string
	GMT_Creted       string `json:"gmt_created"`
	Mobile           string
	Email            string
	IP_WhiteList     string `json:"ip_whitelist"`
	API_VERSION      string `json:"api_version"`
	Balance          int
	AlarmBalance     int    `json:"alarm_balance"`
	EmergencyContact string `json:"emergency_contact"`
	EmergencyMobile  string `json:"emergency_mobile"`
}

type UserSetInfo struct {
	AlarmBalance     int
	EmergencyContact string
	EmergencyMobile  string
}

type Tpls struct {
	BaseStruct
	Templates []Template `json:"template"`
}

type Tpl struct {
	BaseStruct
	Template Template `json:"template"`
}

type Template struct {
	Tpl_id       int    `json:"tpl_id"`
	Tpl_Content  string `json:"tpl_content"`
	Check_Status string `json:"check_status"`
	Reason       string `json:"reason"`
}

type SMSResult struct {
	Count int
	Fee   int
	Sid   int64
}

type SMSSend struct {
	BaseStruct
	Result SMSResult
}

type SMSSendInfo struct {
	Mobile       string
	Text         string
	Extend       string
	Uid          string
	Callback_URL string
}

type SMSStatu struct {
	Sid               int64
	Uid               string
	User_Receive_Time string `json:"user_receive_time"`
	Error_Msg         string `json:"error_msg"`
	Mobile            string
	Report_Status     string `json:"report_status"`
}

type SMSPullStatus struct {
	BaseStruct
	SMSStatus []SMSStatu `json:"sms_status"`
}

type SMSReply struct {
	Mobile      string
	Reply_Time  string `json:"reply_time"`
	Text        string
	Extend      string
	Base_Extend string `json:"base_extend"`
}

type SMSPullReply struct {
	BaseStruct
	SMSReplys []SMSReply `json:"sms_reply"`
}

type SMSGetReplyInfo struct {
	Start_Time    string
	End_Time      string
	Page_Num      int
	Page_Size     int
	Mobile        string
	Return_fields string
	Sort_Fields   string
}

type SMSGetReply struct {
	BaseStruct
	SMS_Replys []SMSReply `json:"sms_reply"`
}

type SMSGetBlackWordResult struct {
	Black_Word string `json:"black_word"`
}

type SMSGetBlackWord struct {
	BaseStruct
	Result SMSGetBlackWordResult
}

type SMSTplSendInfo struct {
	BaseStruct
	Mobile    string
	Tpl_ID    int    `json:"tpl_id"`
	Tpl_Value string `json:"tpl_value"`
	Extend    string
	Uid       string
}

type VoiceSendInfo struct {
	Mobile       string
	Code         string
	Callback_URL string
	Display_Num  string
}

type VoiceSendResult struct {
	Count int
	Fee   int
	Sid   string
}

type VoiceSend struct {
	BaseStruct
	Result VoiceSendResult
}

type VoiceStatu struct {
	Sid               string
	Uid               string
	User_Receive_Time string `json:"user_receive_time"`
	Duration          int
	Error_Msg         string `json:"error_msg"`
	Mobile            string
	Report_Status     string `json:"report_status"`
}

type VoicePullStatus struct {
	BaseStruct
	Voice_Status []VoiceStatu `json:"voice_status"`
}

//--------------------------------------------------------------
//                          函数实现
//--------------------------------------------------------------

//拼接请求URL
func geturl(url string) string {
	return fmt.Sprintf("%s%s:%d/%s/%s.%s", SCHEMES, HOST, PORT, VERSION, url, FORMAT)
}

//创建新的云片API
func NewYunpianAPI(apikey string) *YunpianAPI {
	return &YunpianAPI{apikey}
}

//1.1 查账户信息
func (this *YunpianAPI) UserGet() (User, error) {
	req := httplib.Post(geturl(URL_USER_GET))
	req.Param("apikey", this.APIKey)
	user := User{}
	req.ToJson(&user)
	if user.Code == 0 {
		return user, nil
	}
	return user, errors.New(user.Detail)
}

//1.2 修改账户信息
func (this *YunpianAPI) UserSet(user UserSetInfo) error {
	req := httplib.Post(geturl(URL_USER_SET))
	req.Param("apikey", this.APIKey)
	if user.AlarmBalance != 0 {
		req.Param("alarm_balance", strconv.Itoa(user.AlarmBalance))
	}
	if user.EmergencyContact != "" {
		req.Param("emergency_contact", user.EmergencyContact)
	}
	if user.EmergencyMobile != "" {
		req.Param("emergency_mobile", user.EmergencyMobile)
	}
	baseStruct := BaseStruct{}
	req.ToJson(&baseStruct)
	if baseStruct.Code == 0 {
		return nil
	}
	return errors.New(baseStruct.Detail)
}

//2.1 取默认模板
func (this *YunpianAPI) TplGetDefault(id int) (Template, error) {
	req := httplib.Post(geturl(URL_TPL_GET))
	req.Param("apikey", this.APIKey)
	req.Param("tpl_id", strconv.Itoa(id))
	tpl := Tpl{}
	req.ToJson(&tpl)
	if tpl.Code == 0 {
		return tpl.Template, nil
	}
	return Template{}, errors.New(tpl.Detail)
}
func (this *YunpianAPI) TplGetDefaultAll() ([]Template, error) {
	req := httplib.Post(geturl(URL_TPL_GET))
	req.Param("apikey", this.APIKey)
	tpl := Tpls{}
	req.ToJson(&tpl)
	if tpl.Code == 0 {
		return tpl.Templates, nil
	}
	return nil, errors.New(tpl.Detail)
}

//2.2 添加模板
func (this *YunpianAPI) TplAdd(tpl_content string, notify_type int) (Template, error) {
	req := httplib.Post(geturl(URL_TPL_ADD))
	req.Param("apikey", this.APIKey)
	req.Param("tpl_content", tpl_content)
	req.Param("notify_type", strconv.Itoa(notify_type))
	tpl := Tpl{}
	req.ToJson(&tpl)
	if tpl.Code == 0 {
		return tpl.Template, nil
	}
	return Template{}, errors.New(tpl.Detail)
}

//2.3 取模板
func (this *YunpianAPI) TplGet(tpl_id int) (Template, error) {
	req := httplib.Post(geturl(URL_TPL_GET))
	req.Param("apikey", this.APIKey)
	req.Param("tpl_id", strconv.Itoa(tpl_id))
	tpl := Tpl{}
	req.ToJson(&tpl)
	if tpl.Code == 0 {
		return tpl.Template, nil
	}
	return Template{}, errors.New(tpl.Detail)
}
func (this *YunpianAPI) TplGetALL() ([]Template, error) {
	req := httplib.Post(geturl(URL_TPL_GET))
	req.Param("apikey", this.APIKey)
	tpl := Tpls{}
	req.ToJson(&tpl)
	if tpl.Code == 0 {
		return tpl.Templates, nil
	}
	return nil, errors.New(tpl.Detail)
}

//2.4 修改模板
func (this *YunpianAPI) TplUpdate(tpl_id int, tpl_content string) (Template, error) {
	req := httplib.Post(geturl(URL_TPL_UPDATE))
	req.Param("apikey", this.APIKey)
	req.Param("tpl_id", strconv.Itoa(tpl_id))
	req.Param("tpl_content", tpl_content)
	tpl := Tpl{}
	req.ToJson(&tpl)
	if tpl.Code == 0 {
		return tpl.Template, nil
	}
	return Template{}, errors.New(tpl.Detail)
}

//2.5 删除模板
func (this *YunpianAPI) TplDel(tpl_id int) error {
	req := httplib.Post(geturl(URL_TPL_DEL))
	req.Param("apikey", this.APIKey)
	req.Param("tpl_id", strconv.Itoa(tpl_id))
	baseStruct := BaseStruct{}
	req.ToJson(&baseStruct)
	if baseStruct.Code == 0 {
		return nil
	}
	return errors.New(baseStruct.Detail)
}

//3.1 智能匹配模板发送
func (this *YunpianAPI) SmsSend(info SMSSendInfo) (SMSResult, error) {
	req := httplib.Post(geturl(URL_SMS_SEND))
	req.Param("apikey", this.APIKey)
	req.Param("mobile", info.Mobile)
	req.Param("text", info.Text)
	if info.Extend != "" {
		req.Param("extend", info.Extend)
	}
	if info.Uid != "" {
		req.Param("uid", info.Uid)
	}
	if info.Callback_URL != "" {
		req.Param("callback_url", info.Callback_URL)
	}
	send := SMSSend{}
	req.ToJson(&send)
	if send.Code == 0 {
		return send.Result, nil
	}
	return SMSResult{}, errors.New(send.Detail)
}

//3.2 获取状态报告
func (this *YunpianAPI) SmsPullStatus(page_size ...int) ([]SMSStatu, error) {
	req := httplib.Post(geturl(URL_SMS_PULLSTATUS))
	req.Param("apikey", this.APIKey)
	if len(page_size) > 0 {
		req.Param("page_size", strconv.Itoa(page_size[0]))
	}
	smspullstatus := SMSPullStatus{}
	req.ToJson(&smspullstatus)
	if smspullstatus.Code == 0 {
		return smspullstatus.SMSStatus, nil
	}
	return nil, errors.New(smspullstatus.Detail)
}

//3.4 获取回复短信
func (this *YunpianAPI) SmsPullReply(page_size ...int) ([]SMSReply, error) {
	req := httplib.Post(geturl(URL_SMS_PULLREPLY))
	req.Param("apikey", this.APIKey)
	if len(page_size) > 0 {
		req.Param("page_size", strconv.Itoa(page_size[0]))
	}
	smspullreply := SMSPullReply{}
	req.ToJson(&smspullreply)
	if smspullreply.Code == 0 {
		return smspullreply.SMSReplys, nil
	}
	return nil, errors.New(smspullreply.Detail)
}

//3.6 查看回复信息
func (this *YunpianAPI) SmsGetReply(info SMSGetReplyInfo) ([]SMSReply, error) {
	req := httplib.Post(geturl(URL_SMS_GETREPLY))
	req.Param("apikey", this.APIKey)
	req.Param("start_time", info.Start_Time)
	req.Param("end_time", info.End_Time)
	req.Param("page_num", strconv.Itoa(info.Page_Num))
	req.Param("page_size", strconv.Itoa(info.Page_Size))
	if info.Mobile != "" {
		req.Param("mobile", info.Mobile)
	}
	smsgetreply := SMSGetReply{}
	req.ToJson(&smsgetreply)
	if smsgetreply.Code == 0 {
		return smsgetreply.SMS_Replys, nil
	}
	return nil, errors.New(smsgetreply.Detail)
}

//3.7 查看屏蔽词
func (this *YunpianAPI) SmsGetBlackWord(text string) (string, error) {
	req := httplib.Post(geturl(URL_SMS_GETBLACKWORD))
	req.Param("apikey", this.APIKey)
	req.Param("text", text)
	smsgetblackword := SMSGetBlackWord{}
	req.ToJson(&smsgetblackword)
	if smsgetblackword.Code == 0 {
		return smsgetblackword.Result.Black_Word, nil
	}
	return "", errors.New(smsgetblackword.Detail)
}

//3.8 指定模板发送
func (this *YunpianAPI) SmsTplSend(info SMSTplSendInfo) (SMSResult, error) {
	req := httplib.Post(geturl(URL_SMS_TPLSEND))
	req.Param("apikey", this.APIKey)
	req.Param("mobile", info.Mobile)
	req.Param("tpl_id", strconv.Itoa(info.Tpl_ID))
	req.Param("tpl_value", info.Tpl_Value)
	req.Param("extend", info.Extend)
	req.Param("uid", info.Uid)
	smstplsend := SMSSend{}
	req.ToJson(&smstplsend)
	if smstplsend.Code == 0 {
		return smstplsend.Result, nil
	}
	return SMSResult{}, errors.New(smstplsend.Detail)
}

//3.9 批量个性化发送
func (this *YunpianAPI) SmsMultiSend(info SMSSendInfo) ([]SMSSend, error) {
	req := httplib.Post(geturl(URL_SMS_MULTISEND))
	req.Param("apikey", this.APIKey)
	req.Param("mobile", info.Mobile)
	req.Param("text", info.Text)
	req.Param("extend", info.Extend)
	req.Param("uid", info.Uid)
	req.Param("callback_url", info.Callback_URL)
	smssends := []SMSSend{}
	err := req.ToJson(&smssends)
	if err == nil {
		return smssends, nil
	}
	return nil, err

}

//4.1 发送语音验证码
func (this *YunpianAPI) VoiceSend(info VoiceSendInfo) (VoiceSendResult, error) {
	req := httplib.Post(geturl(URL_VOICE_SEND))
	req.Param("apikey", this.APIKey)
	req.Param("mobile", info.Mobile)
	req.Param("code", info.Code)
	req.Param("callback_url", info.Callback_URL)
	req.Param("display_num", info.Display_Num)
	voicesend := VoiceSend{}
	req.ToJson(&voicesend)
	if voicesend.Code == 0 {
		return voicesend.Result, nil
	}
	return VoiceSendResult{}, errors.New(voicesend.Detail)
}

//获取状态报告
func (this *YunpianAPI) VoicePullStatus(page_size ...int) ([]VoiceStatu, error) {
	req := httplib.Post(geturl(URL_VOICE_PULLSTATUS))
	req.Param("apikey", this.APIKey)
	if len(page_size) > 0 {
		req.Param("page_size", strconv.Itoa(page_size[0]))
	}
	voicepullstatus := VoicePullStatus{}
	req.ToJson(&voicepullstatus)
	if voicepullstatus.Code == 0 {
		return voicepullstatus.Voice_Status, nil
	}
	return nil, errors.New(voicepullstatus.Detail)
}
