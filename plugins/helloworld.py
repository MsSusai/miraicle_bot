# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2022/1/15  17:14 
# 名称：helloworld.PY
# 工具：PyCharm
import miraicle


@miraicle.Mirai.receiver('GroupMessage')
def hello_to_group(bot: miraicle.Mirai, msg: miraicle.GroupMessage):
    if msg.plain in ['Hello', 'hello']:
        bot.send_group_msg(group=msg.group, msg=[miraicle.Plain('Hello world!'),
                                                 miraicle.Face().from_face_id(74),
                                                 miraicle.At(qq=msg.sender)])
