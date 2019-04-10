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
	__Method 1__ : Define peak time / off-peak time with outliers : One sample t-test (T.TEST)
	* Reference : 
	1. [高雄市區建國路段旅行時間差異性檢定與推估](https://research.kcg.gov.tw/upload/RelFile/Research/1069/635852659299120887.pdf)
	2. [五福路車流特性分析與應用](https://www.tbkc.gov.tw/upload/WebList/141/3bb52ea3-d744-43ef-a84d-b7dc2dc6c117/AllFiles/105%E4%BA%94%E7%A6%8F%E8%B7%AF%E8%BB%8A%E6%B5%81%E7%89%B9%E6%80%A7%E5%88%86%E6%9E%90%E8%88%87%E6%87%89%E7%94%A8.pdf)
	* Result : no specific congestion in traffic ( p value >= 0.05 )
	__Method 2__ : Define peak time / off-peak time with the greatest slope : Paired samples t-test (T.TEST)
	* Result : 
	1. The red spots indicate that p value<= 0.045
	2. The numbers in the graph is the weighted average ( w.r.t. the distance of VDs ) of the speed in different spots, which represents the road speed [Average speed +T-test](https://github.com/shiny880410/helloworld/blob/master/hw1/%E6%A8%99%E8%A8%98%E9%A1%AF%E8%91%97%E9%80%9F%E5%BA%A6%E5%B7%AE%E7%95%B0.ipynb)
![image](https://github.com/shiny880410/helloworld/blob/master/hw1/%E6%95%B4%E9%AB%94%E5%B9%B3%E5%9D%87.png)
	* 小結論 : 復興路較無參考資料中車流壅塞時走走停停的狀況，因此在針對各個觀測站分別做單一樣本T檢定時，沒有顯著的情況發生。
因此我們將車速對站點距離加權平均後，依照平均速率與下一個時間窗口的平均速率做成對樣本T檢定，用兩相鄰時窗速率改變量大小來衡量尖峰時間。
並且由圖可知，復興路的壅塞時段沒有如交控中心所訂定的如此明確而侷限。上午 7:00 至 9:00 速率雖有大幅降低，但是其為一連續降低的過程，
且一路到下午，構成"日間時段"( 7:10 至 19:30 )，而 17:00 至 19:00 的下班時間則達到日均速率最低，壅塞明顯，但速率在晚間七點後有明顯回升。因此交控中心訂定的尖峰離峰時間有其代表性，
但卻不能完全描述個別路段的速率變化。透過此圖，我們可以進一步將不同站點的"日間時段"中特殊的速率值抓出來進行比較，同時也個別探討紅點標註的時刻為何有明顯速率變化。
* Q1-4 : To observe the feature of speed in rush hours of different spots.
	* 箱形圖
* Q1-5 : 紅點時間 詳細

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
![image](https://github.com/shiny880410/helloworld/blob/master/hw1/%E7%9B%B8%E9%84%B0%E7%AB%99%E9%80%9F%E7%8E%87.png)
![image](https://github.com/shiny880410/helloworld/blob/master/hw1/%E7%9B%B8%E9%84%B0%E7%AB%99%E9%80%9F%E7%8E%87zscore.png)
	* 小結論 : 
* Q2-3 : Determine the distance between two curves.
	* 小結論 : 
* Q2-4 : Divide spots into several types.
	* 小結論 : 

## **2019-03-28 Week6**
* Q3-1 : We plan to conduct Reynolds Transport Theorem to see that whether the car speeds perform fluid properties.
## **2019-04-04 Week7**