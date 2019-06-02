# DataScience_CSX 4001

## **2019-02-21 Week1**

### 1. Github signup 
* Download desktop version 
* Editing README


## **2019-02-28 Week2**
###  Upload mind map of the sample code 
![image](https://github.com/shiny880410/helloworld/blob/master/hw0/sample_mindmap.PNG)
###  HW0 : Use modules and googlespread to make a wordcloud
* Web crawler (BeautufulSoup/requests) [crawler](https://github.com/shiny880410/helloworld/blob/master/hw0/20190301/craw.py)
* Save and search the news with keywords (gspread) [googleSpreadSheet](https://docs.google.com/spreadsheets/d/1I-m9HwjiPkYES3Ll5PvWk-xijm_9bcn_jxnDOhtpnZE/edit?usp=sharing)
* Cut the news and make the wordcloud (jieba/wordcloud) [hw0](https://github.com/shiny880410/helloworld/blob/master/hw0/20190301/20190301.py)
	* February 28 incident 
![image](https://github.com/shiny880410/helloworld/blob/master/hw0/20190301/2288WC.png)
	* 還願
![image](https://github.com/shiny880410/helloworld/blob/master/hw0/20190301/hwanuanWC.png)

## **2019-03-07 Week3**
### HW1 : Collecting data from the website and changing them to Tidy Data (gspread) [crawler](https://docs.google.com/spreadsheets/d/1FJPf9S2vpimDZvefrpnfq31cq3JpmySHse74WQoEgu4/edit?usp=sharing)
* The data is from Taipei city government website (Update every five minutes) [data](https://data.taipei/dataset/detail/preview?id=b5aaf33a-a6dc-4836-bce6-09986241fe11&rid=8a2ea001-f483-4441-a458-af697653296c)/[code](https://script.google.com/d/MoFMifnPZJWSCCY-qUiHSjPRWp2vJfyNW/edit?mid=ACjPJvERJyEGyupYcceMP2zgbi-XBuoeIsc0jfoRDNc5MlD6BwZz1y98hUQGoXpna_Td5fKbbZpZ7mjLOxd_ttiI0JYeVDz0v2bUWugd56YlQ25FS8iYvWkyBGtfK9-uGZXbtfreI9hibGE&uiv=2)
* 7 observation spots on 復興路 and 9 observation spots on 建國高架
* Average car speed in weekdays (Mon. to Fri.)
* To know the relation between car speed and time, we do the data tidying 
to make variables forms a column, and the observation in the same time forms a row
* To eliminate the meaningless fluctuations, we average the speed every 10 minutes
* Rush hours defined by Traffic Control Center are 7:00 to 9:00 and 17:00 to 19:00 
## **2019-03-14 Week4**
### HW2&3 : Exploratory Data Analysis (EDA) : Speed on the Roads
* Q1-1 : How does the speed varies with time?
	* We listed the data according to the location of the spots on the road and time.
	* More convenient to make v-t graph.
	* Draw the line graph of car speed on each spot during a day (matplotlib) [Line Graph](https://github.com/shiny880410/helloworld/blob/master/hw1/linegraph.ipynb)
![image](https://github.com/shiny880410/helloworld/blob/master/hw1/linegraph.png)
	* 小結論 : 難以從單一 v-t 折線圖觀察出明顯趨勢，故我們試圖改變資料呈現方式。
* Q1-2 : Using gif to make the results more clear. 
	* Draw the line graph that varies with time during a day (matplotlib) [Line Graph2](https://github.com/shiny880410/helloworld/blob/master/hw1/復興南路2.ipynb)
![image](https://github.com/shiny880410/helloworld/blob/master/hw1/%E5%BE%A9%E8%88%88%E5%BE%80%E5%8D%97.gif)
	* 小結論 : 從動圖中我們可以有些初步觀察，並且進一步想知道是否能透過分析訂定出適合復興路的尖峰、離峰時段，讓交控更彈性更有效率。
* Q1-3 : How to define rush hour of 復興路 ?
	* __Method 1__ : Define peak time / off-peak time with outliers : One sample t-test (T.TEST)
	* Reference : 
	1. [高雄市區建國路段旅行時間差異性檢定與推估](https://research.kcg.gov.tw/upload/RelFile/Research/1069/635852659299120887.pdf)
	2. [五福路車流特性分析與應用](https://www.tbkc.gov.tw/upload/WebList/141/3bb52ea3-d744-43ef-a84d-b7dc2dc6c117/AllFiles/105%E4%BA%94%E7%A6%8F%E8%B7%AF%E8%BB%8A%E6%B5%81%E7%89%B9%E6%80%A7%E5%88%86%E6%9E%90%E8%88%87%E6%87%89%E7%94%A8.pdf)
	* Result : no specific congestion in traffic ( p value >= 0.05 )
	* __Method 2__ : Define peak time / off-peak time with the greatest slope : Paired samples t-test (T.TEST)
	* Result : 
	1. The red dots indicate that p value<= 0.045
	2. The numbers in the graph is the weighted average ( w.r.t. the distance of VDs ) of the speed in different spots, which represents the road speed [Average speed +T-test](https://github.com/shiny880410/helloworld/blob/master/hw1/%E6%A8%99%E8%A8%98%E9%A1%AF%E8%91%97%E9%80%9F%E5%BA%A6%E5%B7%AE%E7%95%B0.ipynb)
![image](https://github.com/shiny880410/helloworld/blob/master/hw1/%E6%95%B4%E9%AB%94%E5%B9%B3%E5%9D%87.png)
	* 小結論 : 復興路較無參考資料中車流壅塞時走走停停的狀況，因此在針對各個觀測站分別做單一樣本T檢定時，沒有顯著的情況發生。
因此我們將車速對站點距離加權平均後，依照平均速率與下一個時間窗口的平均速率做成對樣本T檢定，用兩相鄰時窗速率改變量大小來衡量尖峰時間。
並且由圖可知，復興路的壅塞時段沒有如交控中心所訂定的如此明確而侷限。上午 7:00 至 9:00 速率雖有大幅降低，但是其為一連續降低的過程，
且一路到下午，構成"日間時段"( 7:10 至 22:00 )，而 17:00 至 19:00 的下班時間則達到日均速率最低，壅塞明顯，但速率在晚間七點後有明顯回升。因此交控中心訂定的尖峰離峰時間有其代表性，
但卻不能完全描述個別路段的速率變化。透過此圖，我們可以進一步將不同站點的"日間時段"中特殊的速率值抓出來進行比較，同時也個別探討紅點標註的時刻為何有明顯速率變化。
* Q1-4 : To observe the feature of speed in rush hours of different spots.
	* Draw Box plot of different observation spots [Box plot](https://github.com/shiny880410/helloworld/blob/master/hw1/Box.ipynb)  
![image](https://github.com/shiny880410/helloworld/blob/master/hw1/boxplot.png)  
	* 小結論 : 我們用標準化之後的速率畫箱型圖，減少不同站點間的偏移，專注於速率分布。
* Q1-5 : The reason behind red dots.
	* 小結論 : 直觀來看，考量大多數公司上下班時間，以及根據經驗法則該時段搭乘捷運人數也會大幅增加，因此推論因為早上上班通勤時間壅塞，造成 7:00 至 7:30 速率連續明顯下降，17:00、19:00、21:00 亦有下班、
下課通勤人數造成車速下降。之後將考慮輔以實際捷運人流、紅綠燈個數與秒數等，根據特定時刻運用分析方法驗證。
## **2019-03-21 Week5**
* Q2-1 : Can we assume that the speed at each and every adjacent observation spots are the same?
	* Draw the heatmap of car speed of 復興路 during a day (matplotlib) [Heatmap](https://github.com/shiny880410/helloworld/blob/master/hw1/heatmap.ipynb)
![image](https://github.com/shiny880410/helloworld/blob/master/hw1/heatmap.png)
	* 小結論 : 為了在一張二維的圖表上同時呈現時間、速率、站點間的關係這三個變因，因此我們決定用熱圖來顯示較為清楚。圖中顏色深的區塊為
速率較低的時段，我們發現相鄰兩站點的速率其實並不如我們想像中相近，因此假設一個路段的速率是連續變化的似乎不太妥當。因此我們將相鄰站點的v-t圖疊圖相比較，
探討速率如何不同。
* Q2-2 : The relation of speed of adjacent observation spots.
	* Draw linegraph of adjacent observation spots. [Linegraph3](https://github.com/shiny880410/helloworld/blob/master/hw1/linePlot_TwoLines.ipynb)
	* The difference in speed between spots are subtle but important.
	* The speed curve of some adjacent observation spots share the same trend.
	* We plot the v-t curve again with z-score to vanish the gap between spots.
![image](https://github.com/shiny880410/helloworld/blob/master/hw1/%E7%9B%B8%E9%84%B0%E7%AB%99%E9%80%9F%E7%8E%87.png)![image](https://github.com/shiny880410/helloworld/blob/master/hw1/%E7%9B%B8%E9%84%B0%E7%AB%99%E9%80%9F%E7%8E%87(4%2C5%E7%AB%99).png)  
![image](https://github.com/shiny880410/helloworld/blob/master/hw1/%E7%9B%B8%E9%84%B0%E7%AB%99%E9%80%9F%E7%8E%87zscore.png)![image](https://github.com/shiny880410/helloworld/blob/master/hw1/%E7%9B%B8%E9%84%B0%E7%AB%99%E9%80%9F%E7%8E%87zscore(4%2C5%E7%AB%99).png)
	* 小結論 : 兩相鄰站點之間有一定的速率變化趨勢，但是卻有一個速度差，因此我們透過取z分數來消除差距、觀察趨勢。但我們想更進一步量化兩條曲線的相似程度，
因此想透過兩曲線間的距離來取得相似度。
* Q2-3 : Determine the distance between two curves.
	* [Fréchet distance](https://github.com/shiny880410/helloworld/blob/master/hw1/Frechet.ipynb)
	* 小結論 : 網路上查到很多衡量兩曲線的方法，選擇了這個演算法，但是還有調整的空間。知道兩曲線的相似程度，我們可以按照兩站點速率變化的相似程度，
將站點分成幾個小組別討論細部特徵。
* Q2-4 : Divide spots into several types.
	* 小結論 : 由距離分析與觀察來看，我們可以發現1、2觀測站較為相似，第4、5站較為相似，有同趨勢，且彼此之間有塞車時間延遲的現象，推測他們有相近的道路性質。第3站則是速率全日相對穩定且快速，可能
與紅綠燈與線道個數有關。之後將輔以箱型圖分析站與站之間的關係。
## **2019-03-28 Week6**
* Q3-1 : We plan to conduct Reynolds Transport Theorem to see that whether the car speeds perform fluid properties.
## **2019-04-04 Week7**
## **2019-04-11 Week8**
## **2019-04-18 Week9**
## **2019-04-25 Week10**
## **2019-05-02 Week11**
漫長的等待車流資料被爬下來的時間~
## **2019-05-09 Week12**
可悲期中考!!
## **2019-05-16 Week13**
### HW4&5&6 : 車禍資料分析
* 練習 : A1車禍與A2車禍的成因是否相似，有甚麼異同?
	* 由臺北市政府資料開放平台下載 **107年度A1及A2類交通事故明細** 與 **事故代碼對照表** 。[(資料平台網站)](https://data.taipei/dataset/search?keyword=%E4%BA%A4%E9%80%9A%E4%BA%8B%E6%95%85%E8%B3%87%E6%96%99)
		* (註: A1指造成人員當場或二十四小時內死亡之交通事故；A2指造成人員受傷或超過二十四小時死亡之交通事故。)
	* 將資料裡的代碼依照對照表換成文字，並進行資料清理。[(Data工作頁)](https://docs.google.com/spreadsheets/d/1A3V6ncj7VLNDiDkchaYPIYmqrA0trkEj8L-tHoaAyZs/edit?usp=sharing)
		* 我們保留每一筆資料的不同，不進行合併，並在之後以斷詞、找詞頻方式找到不同類型車禍主因。
	* 將資料分成A1與A2兩大類別，同時因為A2事件中死亡人數極少因此可以忽略，我們將其依序分為"死亡"與"受傷"兩大類，再分別進行斷詞。在此我們直接用jieba而不使用TF-IDF，是因為我們的資料並非一般文本有許多冗言贅字或嘆詞等，不需要依照出現次數進行篩選，並從所有文本中找出出現頻率最高的一些詞作為具代表性的特徵。在我們的資料中，出現字詞頻率高即代表其為車禍發生的重要因素。[(斷詞與共現性)](https://github.com/shiny880410/helloworld/blob/master/hw4-6/practice.ipynb)
* 心得 : 透過這個練習，我們更了解老師上課的內容，也對手上的資料更熟悉，並在做完練習後進一步對資料產生疑問，並試著提出下面的問題與想出解決的分析方法。
* 問題一 : 是否能透過了解造成死亡車禍的因素，並找到可以著手改善的地方?
	* 由臺北市政府資料開放平台下載 **107年度A1及A2類交通事故明細** 與 **事故代碼對照表** 。[(資料平台網站)](https://data.taipei/dataset/search?keyword=%E4%BA%A4%E9%80%9A%E4%BA%8B%E6%95%85%E8%B3%87%E6%96%99)
	* 將資料裡的代碼依照對照表換成文字，並進行資料清理。[(Data3工作頁)](https://docs.google.com/spreadsheets/d/1A3V6ncj7VLNDiDkchaYPIYmqrA0trkEj8L-tHoaAyZs/edit?usp=sharing)
		* 與上述不同的是，由於原始資料是將對撞的交通事故分為兩起案件紀錄(即為每一車留下一筆紀錄)，不方便我們分析，故我們以時間軸將同一場車禍資料合併，才能發現車禍與車禍之間的相關性，例如對撞車種之間的關聯性等等。另外，為了不讓資料遺失，我們將"死亡"字串出現在文本的次數，代替每起案件的死亡人數(受傷者亦同)，並以文字以十歲為區間代替年齡，讓數字資料只剩下車速以利判讀。
	* 將我們所關心的關鍵字詞列出來，並觀察彼此交互在文本(不同場車禍)之間出現的次數，最後將矩陣降維呈現，從圖中可以看出名詞之間的相關性。[(A1車禍事故明細分析)](https://github.com/shiny880410/helloworld/blob/master/hw4-6/PCA2.ipynb)
* 結論一 :  從最後所畫成的圖表，我們可以發現死亡車禍確實有和許多特定的詞彙相關，而這也對應到了特定的族群、車種、環境與道路型態。而從這些訊息可以提供相關單位改善道路的方向與進行有效的宣導或臨檢。
	* 我們可以發現以台北市而言，機車是與死亡車禍高度相關的車種之一，再進而參照文本內事發路段，可得知臺北市對外縣市交界的機車道是需要改善的重點道路之一。
	* 50km/hr明顯相較於低時速顯著，因此推論死亡車禍在事發當時車速普遍較高，而另一方面我們也可以發現快車道較慢車道與死亡關聯性更高。
	* 男性較女性更傾向以高速行駛，二十到三十歲是發生事故的主要年齡層，因此可有效的局部加強宣導相關道路安全觀念。
	* 晴天也十分容易發生死亡車禍，因此推估天氣對事故發生影響有限。 
	* 行人易在交叉路口附近發生車禍，因此有關的交通標誌可能要進行改善。
![image](https://github.com/shiny880410/helloworld/blob/master/hw4-6/q2.PNG)

* 問題二 : 是否能透過道路性質預測車速以利道路管制或規劃?
	* 由臺北市政府資料開放平台下載 **復興路** 與 **市民大道** 上各站點之車流與車速。[(資料平台網站)](https://data.taipei/dataset/detail/metadata?id=b5aaf33a-a6dc-4836-bce6-09986241fe11)
	* 透過實地走訪記錄復興路與市民大道上之**紅綠燈是否能左轉**與**車道數** (之後若要增加分析的路段，將由網路抓取相關資料)。
	* 將資料存入試算表並進行資料清理。 [(Data)](https://docs.google.com/spreadsheets/d/1abC0kNTX9YRXDCMU-v9c9aYlXSGakNKbVcIR9t-YgH0/edit?usp=sharing)
		* 由於車流與車速分別為兩個不同的資料來源，因此我們依照時間軸，在試算表中篩選同時有車流與車速資料的時刻，並將該時刻的資料抓取下來依照站點排列，再分別存入x-train data以及y-train data，以作為可放入模型中training的資料。(註 : 資料中車道數2.5為有路肩之路段)
	* 以**紅綠燈能左轉之個數**、**車道數**、**車流**為x data，**車速**為y-data，透過Neural network建模預測車速並計算誤差 [(Neural network)](https://github.com/shiny880410/helloworld/blob/master/hw4-6/NeuralNetwork.ipynb)
		* 會考慮紅綠燈是否能左轉為影響車速的主要因素，是由於我們依照過去的行車經驗，認為能左轉的路口較容易因為橫向車道之紅綠燈號不一致而使車流回堵。
* 結論二 : 我們透過架設結點與層數，預測了33筆車速，並有其中30筆達到10%以內的誤差。期望之後能以更多道路為training data使模型更完善，並在之後若要進行道路施工、捷運工程等長期縮減道路的大型工程時，能以紅綠燈號的改變與周圍道路進行分流，使路段不會長期堵塞造成行車不便(就像我家門口，每天塞車害我遲到qq)。或是在連假時的觀光景點路段，可以透過往年已知的車流，調整紅綠燈號達到分流，減少塞車時間。
## **期末專題 : 車流車速分析與預測**
### 利用 Neural Network 預測車速
* 找出與車速有關的參數 
<br />在選定 X-train data 之前，我們需要找出主要影響車速變化的重要參數。由於道路性質複雜，我們將其想像成二維平板流進行分析，並列出下列物理量，探討其是否適用流體性質。
![image](板流圖片) 		       
![image](https://github.com/shiny880410/helloworld/blob/master/final/pic.PNG) 		       

<br />其中，我們假設紅綠燈數為控制車流前進的壓力梯度，且路口左轉之車流待轉時會減速至幾乎靜止，和邊界無滑動之流體相互對應。而密度則是將車道佔有率(特定時間內一小路段被車輛佔據的時間百分比)依照下列公式進行換算，並和密度成正比 :
$$D=\frac{10K}{Lv+Ld}$$
<br />並利用 Buckingham Pi Theorem 對其進行無因次化，我們有7個物理量，而這些物理量共有3個獨立的因次，則原方程式可以寫成由4個無因次的參數 π1, π2, π3, π4組成的方程式，而這些無因次的參數是由原方程式中的物理量所組成。這個方法讓我們就算不了解參數間確切的方程式也能找出其中相關的物理量。在選取repeating variables時，因為是要找和速度的關聯性，因此要避開速度項，並分別由幾何形狀、流體性質、動力學三個方面選取獨立的參數，因此在這裡我們選擇了ρ、D、ΔP，並得到下列 π 項。

![image]()
![](http://latex.codecogs.com/gif.latex?\\pi2=\frac{L}{D})
![](http://latex.codecogs.com/gif.latex?\\pi3=\frac{V}{D^{2}}*\sqrt{\frac{\rho}{\DeltaP}})
![](http://latex.codecogs.com/gif.latex?\\pi4=\frac{\mu}{D*\sqrt{\rho\DeltaP}})
<br />
$π1=\frac{L}{D}$
$$π2=\frac{L}{D}$$
$$π3=\frac{L}{D}$$
$$π4=\frac{L}{D}$$

並得到π1與其他π之間的關係 :
$$π4=\frac{L}{D}$$
<br />由上面結果可以發現，速度和體積流率、黏滯係數、平板間距有關，呼應了我們在hw4-6中的Neural Network裡依照生活經驗選擇輸入的三個X-data : 紅綠燈能左轉之個數、車道數與車流。我們π1和pressure coefficient有關。
### 分析A1與A2交通事故原因並比較
* 在hw4-6中，我們針對A1交通事故(當場或二十四小時內死亡之交通事故)進行相關性分析並得到和A1交通事故相關的原因。在期末專題中，我們進一步依照同樣方法分析A2交通事故資料並比較。[(A2車禍事故明細分析)]()



















