# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2021/11/29  22:13 
# 名称：repeat.PY
# 工具：PyCharm
# 功能：复读
import miraicle

msg_dict = {}


@miraicle.Mirai.receiver('GroupMessage')
def repeat(bot: miraicle.Mirai, msg: miraicle.GroupMessage):
    group = msg.group
    if group not in msg_dict:
        msg_dict[group] = {'msg_repeat': msg, 'repeat_times': 1}
    elif msg_dict[group]['msg_repeat'] == msg:
        msg_dict[group]['repeat_times'] += 1
    else:
        msg_dict[group] = {'msg_repeat': msg, 'repeat_times': 1}
    if msg_dict[group]['repeat_times'] == 2:
        bot.send_group_msg(group=msg.group, msg=msg)
