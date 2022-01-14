# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2022/1/14  17:36 
# 名称：saucenaoTest.PY
# 工具：PyCharm
import requests
import json

api_key = "4b59b61c9ab58c00cc41bcb197b70f514ea85b65"
url = 'http://saucenao.com/search.php?output_type=2&numres=1&minsim=80!' \
      + '&dbmask=999' + '&api_key=' + api_key

with open('4.jpg', 'rb') as image:
    files = {'file': image}
    response = requests.post(url=url, files=files)

with open('sauce.json', 'w+') as f:
    json.dump(response.json(), f)
