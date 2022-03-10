# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2021/11/29  23:09 
# 名称：blackList.PY
# 工具：PyCharm
import miraicle

blackDict = {}


@miraicle.Mirai.filter('BlacklistFilter')
def blacklist(bot: miraicle.Mirai, msg: miraicle.GroupMessage, flt: miraicle.BlacklistFilter):
    if str(msg.sender) not in flt.show() and msg.plain == '快拉黑我':  # 如果不在黑名单内
        bot.send_group_msg(group=msg.group, msg="你已被拉黑", quote=msg.id)
        flt.append(msg.sender)
        blackDict[msg.sender] = blackDict.get(msg.sender, 0) + 1
        # print(blackDict)
        # print(type(blackDict[msg.sender]))

    elif msg.sender in blackDict.keys() and msg.plain == "我错了":  # 道歉取消黑名单
        if blackDict[msg.sender] < 3:
            bot.send_group_msg(group=msg.group, msg="这次就原谅你了", quote=msg.id)
            flt.remove(msg.sender)
        else:
            bot.send_group_msg(group=msg.group, msg="不可原谅(╯‵□&...", quote=msg.id)

    if bot.is_owner(msg.sender, msg.group):  # 群主操作权限
        if msg.plain == "黑名单":
            if flt.show():
                bot.send_group_msg(group=msg.group, msg=[miraicle.Plain("\n".join(flt.show()))])
            else:
                bot.send_group_msg(group=msg.group, msg=[miraicle.Plain("黑名单没有人哦")])
        elif msg.plain == "解封全部成员":
            bot.send_group_msg(group=msg.group, msg=[miraicle.Plain("已经解封全部成员")])
            flt.clear()
