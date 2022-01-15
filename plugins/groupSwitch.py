# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2021/11/29  23:07 
# 名称：groupSwitch.PY
# 工具：PyCharm
# import miraicle
#
#
# @miraicle.Mirai.filter('GroupSwitchFilter')
# def group_switch(bot: miraicle.Mirai, msg: miraicle.GroupMessage, flt: miraicle.GroupSwitchFilter):
#     if bot.is_owner(msg.sender, msg.group):
#         if msg.plain == '启用所有组件':
#             flt.enable_all(group=msg.group)
#             bot.send_group_msg(group=msg.group, msg='已在群内启用所有组件', quote=msg.id)
#         elif msg.plain == '禁用所有组件':
#             flt.disable_all(group=msg.group)
#             bot.send_group_msg(group=msg.group, msg='已在群内禁用所有组件', quote=msg.id)
