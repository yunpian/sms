
<%
'安装IIS并重启后可用
@LANGUAGE="VBSCRIPT" CODEPAGE="65001"
%>
<%
response.contenttype = "text/html;charset=utf-8"

'提交方法
method = "POST"
'您要发送的手机号
mobile = "xxxxxxxxxxx"
'修改为您的apikey(https://www.yunpian.com)登陆官网后获取
apikey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
'发送内容
text ="【云片网】您的验证码是1234"
'使用模板号
tpl_id = 1
'使用模板内容
tpl_value = Server.URLEncode("#code#=1234&#company#=云片网")
'查询账户信息https地址
url_get_user   = "https://sms.yunpian.com/v1/user/get.json"
'智能匹配模板发送https地址
url_send_sms   = "https://sms.yunpian.com/v1/sms/send.json"
'指定模板发送接口https地址
url_tpl_sms   = "https://sms.yunpian.com/v1/sms/tpl_send.json"
'发送语音验证码接口https地址
url_send_voice = "https://voice.yunpian.com/v1/voice/send.json"

data_get_user  =  "apikey=" & apikey
data_send_sms  =  "apikey=" & apikey & "&mobile=" & mobile & "&text=" & text
data_tpl_sms	= "apikey=" & apikey & "&mobile=" & mobile & "&tpl_id=" & tpl_id & "&tpl_value=" & tpl_value
data_send_voice = "apikey=" & apikey & "&mobile=" & mobile & "&code=" & "1234"

response.write GetBody(url_get_user,data_get_user) & "<hr>"
response.write GetBody(url_send_sms,data_send_sms) & "<hr>"
response.write GetBody(url_tpl_sms,data_tpl_sms) & "<hr>"
response.write GetBody(url_send_voice,data_send_voice) & "<hr>"

Function GetBody(url,data) 
	Set https = Server.CreateObject("MSXML2.ServerXMLHTTP") 
	With https
	.Open method, url, False
	.setRequestHeader "Content-Type","application/x-www-form-urlencoded"
	.Send data
	
	GetBody= .ResponseBody
	End With
	GetBody = bytetostr(httpss.ResponseBody,"utf-8")
	Set httpss = Nothing 
	
End Function

function bytetostr(vin,cset)
dim bs,sr
set bs = server.createObject("adodb.stream")
    bs.type = 2
    bs.open
    bs.writetext vin
    bs.position = 0
    bs.charset = cset
    bs.position = 2
    sr = bs.readtext
    bs.close
set bs = nothing
bytetostr = sr
end function



response.write "<hr>"

%>
