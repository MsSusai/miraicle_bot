# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2022/1/14  20:57 
# 名称：qqsaucetest.PY
# 工具：PyCharm
from assistclass.SauceNaoSearch import SauceNaoSearch

saucenao = SauceNaoSearch('4b59b61c9ab58c00cc41bcb197b70f514ea85b65')
result = saucenao.searchFromUrl(
    "https://i.pximg.net/img-original/img/2022/01/15/09/43/57/95534252_p0.png")
print(result)
