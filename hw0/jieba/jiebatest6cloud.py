import os
import pickle
import requests
from bs4 import BeautifulSoup
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import jieba
import numpy as np
from collections import Counter

def get_wordcloud_of_keywords(a, image_path=False):
    
    if image_path:
        coloring = np.array(Image.open(os.path.join(image_path)))
        color_func = ImageColorGenerator(coloring)
        wc = WordCloud(max_font_size=15,
                       background_color="white",
                       mask=coloring,
                       color_func=color_func,
                       font_path=font_path,
                       width=1000, height=1000,
                       max_words=10000)
    else:
        wc = WordCloud(max_font_size=15,
                       background_color="white",
                       colormap='Set2',
                       font_path=font_path,
                       width=1000, height=300,
                       max_words=10000)

    im = wc.generate_from_frequencies(frequencies=a)
    return im


with open('./newtalk.pkl', 'rb') as f:
    data = pickle.load(f)
data = data[::-1]
s = [news['content'] for news in data]
s1=''
for i in range(len(s)):
    s1+=s[i]
#print(s1)
print('done')
for i in '，。\n？：；「」●＄％':
     s1=s1.replace(i,'')
#print(s1)
jieba.set_dictionary('dict.txt.big')
jieba.load_userdict("userdict.txt")
words = jieba.cut(s1, cut_all=False)

st=[]
for word in set(words):
    qct=s1.count(word)
    st.append([word,qct])
st.sort()
st.sort(key=lambda x:x[1],reverse= True)
#print(dict(st))


font_path = r'msjh.ttc'

ten_wc = get_wordcloud_of_keywords(dict(st), './1234.jpg')
# ten_wc.to_file('politicians/tenwc.png')
ten_wc.to_image()
plt.figure( figsize=(60,30))
plt.imshow(ten_wc,interpolation='bilinear')
plt.axis("off")
plt.tight_layout(pad=0)
#顯示用
plt.show()


