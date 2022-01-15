# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2021/11/29  20:15 
# 名称：bot.PY
# 工具：PyCharm
import miraicle
from plugins import *

qq = 1981016457  # 你登录的机器人 QQ 号
verify_key = 'mirai'  # 你在 setting.yml 中设置的 verifyKey
port = 8080  # 你在 setting.yml 中设置的 port (http)

bot = miraicle.Mirai(qq=qq, verify_key=verify_key, port=port)
# bot.set_filter(miraicle.GroupSwitchFilter(r'config\group_switch.json'))
bot.set_filter(miraicle.BlacklistFilter(r'config\blacklist.json'))
bot.run()
