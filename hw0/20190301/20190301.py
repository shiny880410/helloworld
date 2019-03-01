import requests
import os
from bs4 import BeautifulSoup
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import re
import numpy as np
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import jieba
import time
import math
from collections import Counter
def get_wordcloud_of_keywords(a, image_path=False):
    
    if image_path:
        coloring = np.array(Image.open(os.path.join(image_path)))
        color_func = ImageColorGenerator(coloring)
        wc = WordCloud(max_font_size=60,
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

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('D:\\台大\\大二下\\資料科學\\My First Project-5d1a7d0536a5.json', scope)
gc = gspread.authorize(credentials)
# Open a worksheet from spreadsheet with one shot
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1I-m9HwjiPkYES3Ll5PvWk-xijm_9bcn_jxnDOhtpnZE/edit#gid=0')
wks2 = sh.worksheet("關鍵字")
n=input('請輸入關鍵字:')
wks2.update_acell('A1',n)
time.sleep(5)
values_list = wks2.col_values(1)
values_list.pop(0)
newswords=[]
newswordsunited=''
for i in values_list:
    newswords.append(wks2.acell('C'+str((int(i)+1))).value)
for j in newswords:
    newswordsunited+=j
for k in '！，。\n？：；「」●＄％、qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM,./[];\=1234567890':
    newswordsunited=newswordsunited.replace(k,'')
jieba.set_dictionary('dict.txt.big')
jieba.load_userdict("userdict.txt")
words = jieba.cut(newswordsunited, cut_all=False)

   
st=[]
for word in set(words):
    
    if len(word)>1:
        qct=newswordsunited.count(word)
        st.append([word,qct])
st.sort()
st.sort(key=lambda x:x[1],reverse= True)


font_path = r'msjh.ttc'

ten_wc = get_wordcloud_of_keywords(dict(st), './2288.png')

ten_wc.to_image()
plt.figure( figsize=(60,30))
plt.imshow(ten_wc,interpolation='bilinear')
plt.axis("off")
plt.tight_layout(pad=0)
#顯示用
plt.savefig("2288WC.png")
plt.show()

