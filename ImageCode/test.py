# -*- coding: UTF-8 -*-
# @Time : 2022/2/8 14:45
# @File : test.py
# @Software : PyCharm
import pytesseract
from PIL import Image

im = Image.open('1.jpg')
im = im.convert('L')
threshold = 127
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

im = im.point(table, '1')
text = pytesseract.image_to_string(im)
print(text)