#/bin/sh
#修改为您的apikey
apikey="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
mobile="186xxxxxxxx"
content=$2
#短信模板
temp="xxx"
#发送内容拼接
text=${temp}${content}

#urlencode编码
curl --data-urlencode "apikey=$apikey" --data-urlencode "mobile=$mobile" --data-urlencode "text=$text" "https://sms.yunpian.com/v2/sms/single_send.json" >> /tmp/sendSNS.log

echo $1 >> /tmp/sendSNS.log
echo $2 >> /tmp/sendSNS.log
