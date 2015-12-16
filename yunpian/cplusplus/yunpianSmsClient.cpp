#include <stdio.h>
#include <curl/curl.h>
#include <stdarg.h>
#include <stdlib.h>
#include <string.h>
#define MAXPARAM 2048

CURL *curl;
CURLcode res;
/**

bingone

本样例依赖libcurl库
下载地址 https://curl.haxx.se/download.html

*/
// 修改为您的apikey
char *apikey = "xxxxxxxxxxxxxxxx";
// 修改为您要发送的手机号
char *mobile = "xxxxxxxxxxxxxxxx";
// 设置您要发送的内容
char *text = "【云片网】您的验证码是1234";
// 指定发送的模板id
int tpl_id = 1176663;
// 指定发送模板内容


//char *tpl_data[4] = {"#code#","1234","#company#","云片网"};
char *tpl_data[4] = {"#send_tim*/.:#&=%e#","123#4","#cos&=*!@#$%^&*()-_+={}\\\'de#","asdf"};
// 发送语音验证码内容
int code = 1234;
// 获取user信息url
char *url_get_user     = "https://sms.yunpian.com/v1/user/get.json";
// 智能模板发送短信url
char *url_send_sms     = "https://sms.yunpian.com/v1/sms/send.json";
// 指定模板发送短信url
char *url_tpl_sms      = "https://sms.yunpian.com/v1/sms/tpl_send.json";
// 发送语音短信url
char *url_send_voice   = "https://voice.yunpian.com/v1/voice/send.json";

void send_data(char *url,char *data)
{
	// specify the url
	curl_easy_setopt(curl, CURLOPT_URL, url);
	// specify the POST data
	curl_easy_setopt(curl, CURLOPT_POSTFIELDS, data);
	// get response data
	curl_easy_perform(curl);
	printf("\n\n");
}
/**
* 查账户信息
*/
void get_user(char *apikey)
{
    char params[MAXPARAM + 1];
    char *cp = params;
    sprintf(params,"apikey=%s", apikey);
    send_data(url_get_user, params);
}

/**
* 使用智能匹配模版接口发短信
*/
void send_sms(char *apikey, char *mobile, char *text)
{
    char params[MAXPARAM + 1];
    char *cp = params;
    sprintf(params,"apikey=%s&mobile=%s&text=%s", apikey, mobile, text);
    send_data(url_send_sms, params);
}
/**
* 使用智能匹配模版接口发短信
*/
void send_tpl_sms(char *apikey, char *mobile, int tpl_id, char *tpl_value)
{
    char params[MAXPARAM + 1];
    char *cp = params;
    sprintf(params,"apikey=%s&mobile=%s&tpl_id=%d&tpl_value=%s", apikey, mobile, tpl_id, tpl_value);
    send_data(url_tpl_sms, params);
}
/**
* 使用智能匹配模版接口发短信
*/
void send_voice(char *apikey, char *mobile, int code)
{
    char params[MAXPARAM + 1];
    char *cp = params;
    sprintf(params,"apikey=%s&mobile=%s&code=%d", apikey, mobile, code);
    send_data(url_send_voice, params);
}
int main(void)
{

	curl = curl_easy_init();
	if(NULL == curl) {
		perror("curl open fail\n");
	}
	get_user(apikey);
	//send_sms(apikey,mobile,text);


	char *tmp;
	char *tpl_value = (char *)malloc(sizeof(char) * 500);
	bzero(tpl_value, sizeof(char)*500);

	// 模板发送需要编码两次，第一次URL编码转换
	int len = 0;
	tmp = curl_easy_escape(curl,tpl_data[0],strlen(tpl_data[0]));
	memcpy(tpl_value+len,tmp,strlen(tmp));
	len += strlen(tmp);
	tpl_value[len++] = '=';

	tmp = curl_easy_escape(curl,tpl_data[1],strlen(tpl_data[1]));
	memcpy(tpl_value+len,tmp,strlen(tmp));
	len += strlen(tmp);
	tpl_value[len++] = '&';

	tmp = curl_easy_escape(curl,tpl_data[2],strlen(tpl_data[2]));
	memcpy(tpl_value+len,tmp,strlen(tmp));
	len += strlen(tmp);
	tpl_value[len++] = '=';

	tmp = curl_easy_escape(curl,tpl_data[3],strlen(tpl_data[3]));
	memcpy(tpl_value+len,tmp,strlen(tmp));
	len += strlen(tmp);

	tmp=tpl_value;
	// 第二次URL编码
	tpl_value = curl_easy_escape(curl,tpl_value,strlen(tpl_value));
	send_tpl_sms(apikey,mobile,tpl_id,tpl_value);
	free(tmp);

	curl_easy_cleanup(curl);
	
	return 0;
}
