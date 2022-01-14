# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2022/1/14  20:57 
# 名称：qqsaucetest.PY
# 工具：PyCharm
from plugins.imageSearch import SauceNaoSearch

saucenao = SauceNaoSearch('4b59b61c9ab58c00cc41bcb197b70f514ea85b65')
result = saucenao.searchFromUrl(
    "http://gchat.qpic.cn/gchatpic_new/2199596241/730693784-2574473272-9017117B6A5D488A96B7B4B4AFD301BE/0?term=2")
print(result)
