# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2021/11/29  22:11 
# 名称：hello_world.PY
# 工具：PyCharm
import miraicle


@miraicle.Mirai.receiver('GroupMessage')
def hello_to_group(bot: miraicle.Mirai, msg: miraicle.GroupMessage):
    if msg.plain in ["hello", "Hello"]:
        bot.send_group_msg(group=msg.group,
                           msg=[
                               miraicle.Plain("Hello World!"),
                               miraicle.Face().from_face_id(74),
                               miraicle.At(qq=msg.sender)
                           ])


# @miraicle.Mirai.receiver('FriendMessage')
# def hello_to_friend(bot: miraicle.Mirai, msg: miraicle.FriendMessage):
#     bot.send_friend_msg(qq=msg.sender, msg='Hello world!')
