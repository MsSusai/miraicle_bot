# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2021/11/29  23:09 
# 名称：blackList.PY
# 工具：PyCharm
import miraicle


@miraicle.Mirai.filter('BlacklistFilter')
def blacklist(bot: miraicle.Mirai, msg: miraicle.GroupMessage, flt: miraicle.BlacklistFilter):
    if msg.plain in ['快拉黑我']:
        bot.send_group_msg(group=msg.group, msg="你已被拉黑", quote=msg.id)
        flt.append(msg.sender)
    elif msg.plain in ["我错了"]:
        bot.send_group_msg(group=msg.group, msg="这次就原谅你了", quote=msg.id)
        flt.remove(msg.sender)
