# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2021/11/29  22:34 
# 名称：test.PY
# 工具：PyCharm
import os
import random

dir = r'D:\东方\カンパ'
imageList = os.listdir(dir)
image = random.choice(imageList)
dir = r'file:\\\D:\东方\カンパ' + '\\' + image
print(dir)
