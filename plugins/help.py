# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2022/1/15  22:37 
# 名称：help.PY
# 工具：PyCharm
import miraicle


# 输入“帮助”显示指令
@miraicle.Mirai.receiver("GroupMessage")
def help(bot: miraicle.Mirai, msg: miraicle.GroupMessage):
    if msg.plain in ["帮助", "help"]:
        bot.send_group_msg(group=msg.group, msg=[miraicle.Plain("[Hello|hello]：测试用\n"
                                                                "[本群词云]：生成本群的词云\n"
                                                                "[识别图片|识图]：图片识别功能\n"
                                                                "[快拉黑我]：神秘功能\n")])
