# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2022/1/15  23:04 
# 名称：create_wordcloudDB.PY
# 工具：PyCharm
import sqlite3


connect = sqlite3.connect('word_cloud.db')
cursor = connect.cursor()
cursor.execute(
    'CREATE TABLE msgs'
    '(id        INTEGER PRIMARY KEY AUTOINCREMENT,'
    'time       INT,'
    'sender_id  INT,'
    'group_id   INT,'
    'msg        TEXT)')

cursor.execute('CREATE INDEX idx_group_id ON msgs(group_id)')

connect.commit()
connect.close()