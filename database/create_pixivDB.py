# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2022/1/16  17:53 
# 名称：create_pixivDB.PY
# 工具：PyCharm
import sqlite3

connect = sqlite3.connect('pixiv_image.db')
cursor = connect.cursor()

cursor.execute(
    'CREATE TABLE pixiv_imageID'
    '(pixivID        INTEGER PRIMARY KEY,'
    'author  VARCHAR(20),'
    'title        TEXT)')

connect.commit()
connect.close()
