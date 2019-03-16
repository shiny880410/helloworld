import gspread
from oauth2client.service_account import ServiceAccountCredentials
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from IPython.display import Image

def plot1(road):
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('D:\\台大\\大二下\\資料科學\\My First Project-5d1a7d0536a5.json', scope)
    gc = gspread.authorize(credentials)
    # Open a worksheet from spreadsheet with one shot
    sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1FJPf9S2vpimDZvefrpnfq31cq3JpmySHse74WQoEgu4/edit?ts=5c8895e5#gid=618695640')
    wks4 = sh.worksheet("復興南北路")

    time = wks4.col_values(3)
    st =[]
    st2=[]
    
    time.pop(0)
    time.pop(0)
    time.pop(0)
    cell = wks4.find(road)
    speed = wks4.col_values(cell.col)
    speed.pop(0)
    speed.pop(0)
    speed.pop(0)
    for i in range(len(time)):
        st2.append([time[i],speed[i]])
        st.append(st2[i])
    #print(st)
    #print(speed)

    plt.style.use('bmh')
    fig = plt.figure()
    ax = plt.axes()

    stnum=[]
    for i in range(len(speed)):
        stnum.append(eval(speed[i].strip('Km/hr')))
    plt.plot(stnum)
    #print(stnum)
    #print(time)
    timex=[]
    timex2=[]
    for j in range(1,len(time),4):
        timex.append(time[j-1].split('~'))
    for k in range(len(timex)):
        timex2.append(timex[k][0])
    #print(timex2)
    fontPath = r'D:\\台大\\大二下\\資料科學\\NotoSansTC-Regular.otf'
    font30 = fm.FontProperties(fname=fontPath, size=10)
    plt.xticks(range(0,len(time),4),timex2, rotation=70)
    plt.ylim(0, 80)
    plt.title(road,fontproperties=font30)
    plt.ylabel("speed(km/hr)")
    plt.xlabel("time")

    fig.savefig('linegraph.png')
    plt.show()
    return 
n=input('請輸入想調查的站點:')
plot1(n)
