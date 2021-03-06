# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2022/1/16  19:21 
# 名称：PixivSpider.PY
# 工具：PyCharm
import requests
from bs4 import BeautifulSoup
import re
import random

USER_AGENT_LIST = [
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]


class PixivSpider:
    def __init__(self, url):
        self.url = url
        self.header = {
            'User-Agent': random.choice(USER_AGENT_LIST),
            # 'cookie':
            'referer': 'https://www.pixiv.net/',
            'accept': 'application/json',
            'authority': 'www.pixiv.net',
            'accept-Language': 'en'
        }
        self.proxy = {'http': 'http://127.0.0.1:10809',
                      'https': 'https://127.0.0.1:10809'}

    def get_img_info(self):
        pass
