# -*- codeing = utf-8 -*-
# @Time : 2022/1/10
# @Author : Ello
# @File : wordCloud.py
# @Software : IntelliJ IDEA

import jieba
from matplotlib import pyplot as plt
from wordcloud import WordCloud
import numpy as np
import sqlite3
from PIL import Image

conn = sqlite3.connect("movie250.db")
cur = conn.cursor()
sql = "select instroduction from movie250"
data = cur.execute(sql)
text = ""
for item in data:
    text = text + item[0]
print(text)
cur.close()
conn.close()

#分词
cut = jieba.cut(text)
word = " ".join(cut)
print(len(word))

#词云图片
img = Image.open(r".\static\assets\img\tree.jpg")
img_array = np.array(img)
wc = WordCloud(
    background_color="white",
    mask = img_array,
    font_path="msyh.ttc"
)
wc.generate_from_text(word)


#绘制图片
fig = plt.figure(1)
plt.imshow(wc)
plt.axis('off')
plt.show()


