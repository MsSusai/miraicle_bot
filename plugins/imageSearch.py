# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2022/1/15  16:43 
# 名称：imageSearch.PY
# 工具：PyCharm
# 利用saucenao搜索图片

import miraicle
from assistclass.SauceNaoSearch import SauceNaoSearch
from assistclass.SauceNaoResult import SearchResults


@miraicle.Mirai.receiver('GroupMessage')
def searchImage(bot: miraicle.Mirai, msg: miraicle.GroupMessage):
    global SENDER
    saucenao = SauceNaoSearch('4b59b61c9ab58c00cc41bcb197b70f514ea85b65')
    if msg.plain in ["识别图片", "识图"]:
        SENDER = msg.sender
        bot.send_group_msg(group=msg.group, msg=[miraicle.At(qq=msg.sender),
                                                 miraicle.Plain("请发送要识别的图片"), ])
    if msg.sender == SENDER and msg.first_image is not None:
        result = saucenao.searchFromUrl(msg.first_image.url)
        if isinstance(result, SearchResults):
            bot.send_group_msg(group=msg.group, msg=[miraicle.At(qq=msg.sender),
                                                     miraicle.Plain("识图结果如下：\n" + result.__str__())])
        else:
            bot.send_group_msg(group=msg.group, msg=[miraicle.Plain(result)])
        SENDER = None
