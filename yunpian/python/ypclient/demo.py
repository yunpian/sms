# coding: utf8
from datetime import datetime

# 使用V1 API
# from yunpian import ClientV1
# c = ClientV1('your api key')

# 使用V2 API
from yunpian import ClientV2
c = ClientV2('your api key')

#### 账户API
# V1/V2 查看账户信息
res = c.get_account()

# V1/V2 修改账户信息
# res = c.modify_account('name', 'phone', 20)


#### 模板API
# V2 取默认模板
# res = c.get_default_sms_tpl()

# V1/V2 添加模板
# res = c.create_sms_tpl('签名', '模板内容')

# V1/V2 取模板
# res = c.get_sms_tpl(111111)

# V1/V2 修改模板
# res = c.modify_sms_tpl(11111, '新签名', '新模板内容')

# V1/V2 删除模板
# res = c.del_sms_tpl(111111)


#### 短信API
# V1 智能匹配模板发送; V2 单条发送
# res = c.send_sms('151xxxxxxxx', '【签名】短信内容')

# V2 批量发送
# res = c.broadcast_sms(['151xxxxxxx1', '151xxxxxxx2'], '【签名】短信内容')

# V1 批量个性化发送; V2 个性化发送;
# 使用jobs方式配置任务
# res = c.send_multi_sms(jobs=[
#     {
#         '151xxxxxxx1': '【签名1】短信内容1',
#         '151xxxxxxx2': '【签名2】短信内容2',
#     },
#     {
#         '151xxxxxxx2': '【签名3】短信内容3',
#         '151xxxxxxx3': '【签名4】短信内容4',
#     },
# ])
# 使用流水线方式配置任务
# res = c.send_multi_sms(
#     mobiles=['151xxxxxxx1', '151xxxxxxx2', '151xxxxxxx2', '151xxxxxxx3'],
#     contents=['【签名1】短信内容1', '【签名2】短信内容2', '【签名3】短信内容3', '【签名4】短信内容4']
# )

# V1/V2 获取状态报告
# res = c.get_sms_status()

# V1/V2 推送状态报告
# res = c.get_sms_reply()

# V1/V2 查回复短信
# res = c.retrieve_sms_reply('2016-08-13 00:00:00', datetime.now(), 20)

# V1/V2 查短信发送记录
# res = c.get_sms_send_record('2016-08-13 00:00:00', datetime.now(), 20)

# V1/V2 查屏蔽词
# res = c.get_black_word('我是大傻逼')  # "傻逼"是屏蔽词

# V1 指定模板发送; V2 指定模板单发
# res = c.send_tpl_sms('151xxxxxxxx', 11111, {'context': '模板上下文'})


#### 语音API
# V1/V2 发送语音验证码
# res = c.voice_verification_code('151xxxxxxxx', 112233)

# V1/V2 获取状态报告
# res = c.get_voice_verification_status()


#### 流量API
# V1/V2 查询流量包
# res = c.get_data_traffic()

# V1/V2 流量包充值
# res = c.recharge_data_traffic('151xxxxxxxx', '1008601')

# V1/V2 获取状态报告
# res = c.get_data_traffic_status()




# 读取返回值
data = res.json()
