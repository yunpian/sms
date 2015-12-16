package main
import (
	"net/http"
	"io/ioutil"
	"net/url"
    "fmt"
 )
// bingone
func main(){

	// 设置为您的apikey(https://www.yunpian.com)用户中心可查
	apikey 		:= "xxxxxxxxxxxxxxxxxxxxxxxx"
	 // 发送的手机号
	mobile 		:= "xxxxxxxxxxxxxxxxxxxxxxxx"
	// 发送内容
	text 		:= "您的验证码是1234【云片网】"
	// 发送模板编号
	tpl_id		:= 1
	// 发送模板内容
	tpl_value	:= "#code#=1234&#company#=云片网"
	// 语音验证码
	code		:= 1234
	// 获取user信息url
	url_get_user	:= "https://sms.yunpian.com/v1/user/get.json";
	// 智能模板发送短信url
	url_send_sms	:= "https://sms.yunpian.com/v1/sms/send.json";
	// 指定模板发送短信url
	url_tpl_sms		:= "https://sms.yunpian.com/v1/sms/tpl_send.json";
	// 发送语音短信url
	url_send_voice 	:= "https://voice.yunpian.com/v1/voice/send.json";

	data_get_user	:= url.Values{"apikey": {apikey}}
	data_send_sms	:= url.Values{"apikey": {apikey}, "mobile": {mobile},"text":{text}}
	data_tpl_sms	:= url.Values{"apikey": {apikey}, "mobile": {mobile},"tpl_id":{fmt.Sprintf("%d", tpl_id)},"tpl_value":{tpl_value}}
	data_send_voice	:= url.Values{"apikey": {apikey}, "mobile": {mobile},"code":{fmt.Sprintf("%d", code)}}


	httpsPostForm(url_get_user,data_get_user)
	httpsPostForm(url_send_sms,data_send_sms)
	httpsPostForm(url_tpl_sms,data_tpl_sms)
	httpsPostForm(url_send_voice,data_send_voice)
}

func httpsPostForm(url string,data url.Values) {
	resp, err := http.PostForm(url,data)

	if err != nil {
		// handle error
	}

	defer resp.Body.Close()
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		// handle error
	}

	fmt.Println(string(body))

}
