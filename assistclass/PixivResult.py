# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2022/1/16  19:06 
# 名称：PixivResult.PY
# 工具：PyCharm
from typing import Optional
import sqlite3


class PixivResult:
    def __init__(self,
                 imgID: Optional[int] = None,
                 author: Optional[str] = None,
                 title: Optional[str] = None
                 ):
        self.imgID = imgID
        self.author = author
        self.title = title

    def save_to_DB(self):
        pass
