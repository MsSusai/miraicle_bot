# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2021/11/29  23:09 
# 名称：blackList.PY
# 工具：PyCharm
import miraicle

blackDict = {}


@miraicle.Mirai.filter('BlacklistFilter')
def blacklist(bot: miraicle.Mirai, msg: miraicle.GroupMessage, flt: miraicle.BlacklistFilter):
    if str(msg.sender) not in flt.show():  # 如果不在黑名单内
        if msg.plain in '快拉黑我':
            bot.send_group_msg(group=msg.group, msg="你已被拉黑", quote=msg.id)
            flt.append(msg.sender)
            blackDict[msg.sender] = blackDict.get(msg.sender, 1) + 1

    elif msg.plain in "我错了":  # 道歉取消黑名单
        if msg.sender in blackDict.keys():
            if blackDict[msg.sender] <= 3:
                bot.send_group_msg(group=msg.group, msg="这次就原谅你了", quote=msg.id)
                flt.remove(msg.sender)
            else:
                bot.send_group_msg(group=msg.group, msg="不可原谅(╯‵□&...", quote=msg.id)

    elif bot.is_owner(msg.sender, msg.group):  # 群主操作权限
        if msg.plain in "黑名单":
            bot.send_group_msg(group=msg.group, msg=[miraicle.Plain("\n".join(flt.show()))])

        if msg.plain in "解封全部成员":
            bot.send_group_msg(group=msg.group, msg=[miraicle.Plain("已经解封全部成员")])
            flt.clear()
