# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2021/11/29  22:25 
# 名称：sendImage.PY
# 工具：PyCharm
import miraicle
import os
import random


@miraicle.Mirai.receiver('GroupMessage')
def sendImage(bot: miraicle.Mirai, msg: miraicle.GroupMessage):
    if msg.plain in ["来点图"]:
        path = r"D:\东方\カンパ"
        imageList = os.listdir(path)
        image = random.choice(imageList)
        dir = r'file:\\\D:\东方\カンパ' + '\\' + image
        bot.send_group_msg(group=msg.group, msg=[
            miraicle.Plain(image),
            miraicle.Image(url=dir),
            miraicle.At(qq=msg.sender)])
