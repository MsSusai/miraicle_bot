# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2021/11/29  23:09 
# 名称：blackList.PY
# 工具：PyCharm
import miraicle

blackDict = {}


@miraicle.Mirai.filter('BlacklistFilter')
def blacklist(bot: miraicle.Mirai, msg: miraicle.GroupMessage, flt: miraicle.BlacklistFilter):
    if msg.plain in ['快拉黑我']:
        bot.send_group_msg(group=msg.group, msg="你已被拉黑", quote=msg.id)
        flt.append(msg.sender)
        blackDict[msg.sender] = blackDict.get(msg.sender, 1) + 1
    elif msg.plain in ["我错了"]:
        if msg.sender in blackDict.keys():
            if blackDict[msg.sender] <= 3:
                bot.send_group_msg(group=msg.group, msg="这次就原谅你了", quote=msg.id)
                flt.remove(msg.sender)
            else:
                bot.send_group_msg(group=msg.group, msg="不可原谅(╯‵□&...", quote=msg.id)
    if bot.is_owner(msg.sender, msg.group):
        if "黑名单" in msg.plain:
            bot.send_group_msg(group=msg.group, msg=flt.show())
        if "解封全部" in msg.plain:
            bot.send_group_msg(group=msg.group, msg=["已经解封全部成员"])
            flt.clear()
