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
* Q1 : How does the speed varies with time?
	* We listed the data according to the location of the spots on the road and time.
	* More convenient to make v-t graph.
	* Draw the line graph of car speed on each spot during a day (matplotlib) [Line Graph](https://github.com/shiny880410/helloworld/blob/master/hw1/linegraph.ipynb)
![image](https://github.com/shiny880410/helloworld/blob/master/hw1/linegraph.png)
	* 小結論 : 難以從單一 v-t 折線圖觀察出明顯趨勢，故我們試圖改變資料呈現方式。
* Q1-1 : Using gif to make the results more clear. 
	* Draw the line graph that varies with time during a day (matplotlib) [Line Graph2](https://github.com/shiny880410/helloworld/blob/master/hw1/復興南路2.ipynb)
![image](https://github.com/shiny880410/helloworld/blob/master/hw1/%E5%BE%A9%E8%88%88%E5%BE%80%E5%8D%97.gif)
	* 小結論 : 從動圖中我們可以發現，復興路的壅塞時段沒有如交控中心所訂定的如此明確而侷限。上午 7:00 至 9:00 速率沒有大幅降低，反而是連續降低的過程，且一路到下午，構成"日間時段"，而 17:00 至 19:00 的下班時間則有明顯壅塞，速率最後會於晚間回升。有了這些初步觀察，我們想知道是否能透過分析訂定出適合復興路的尖峰、離峰時段，讓交控更彈性更有效率。
* Q1-2 : How to define rush hour of 復興路 ?
	* Method 1 : Define peak time / off-peak time with the greatest slope : Paired samples t-test
	* Result : 
	1. The red spots indicate that p value<= 0.045
	2. The numbers in the graph is the weighted average ( w.r.t. the distance of VDs ) of the speed in different spots, which represents the road speed [Average speed +T-test](https://github.com/shiny880410/helloworld/blob/master/hw1/%E6%A8%99%E8%A8%98%E9%A1%AF%E8%91%97%E9%80%9F%E5%BA%A6%E5%B7%AE%E7%95%B0.ipynb)
![image](https://github.com/shiny880410/helloworld/blob/master/hw1/%E6%95%B4%E9%AB%94%E5%B9%B3%E5%9D%87.png)
	* Method 2 : Define peak time / off-peak time with outliers : One sample t-test
	* Reference : 
	1. [高雄市區建國路段旅行時間差異性檢定與推估](https://research.kcg.gov.tw/upload/RelFile/Research/1069/635852659299120887.pdf)
	2. [五福路車流特性分析與應用](https://www.tbkc.gov.tw/upload/WebList/141/3bb52ea3-d744-43ef-a84d-b7dc2dc6c117/AllFiles/105%E4%BA%94%E7%A6%8F%E8%B7%AF%E8%BB%8A%E6%B5%81%E7%89%B9%E6%80%A7%E5%88%86%E6%9E%90%E8%88%87%E6%87%89%E7%94%A8.pdf)
	* Result : no specific congestion in traffic ( p value >= 0.05 )
	* 小結論 : 在前兩分參考資料中，它們都是拿單一觀測站的資料，以一個小時為單位交錯後，做單一樣本T檢定來區隔尖峰離峰時段。但是當我們用同樣的方法分析之後卻發現，復興南北路似乎沒有明顯的壅塞情況。後來我們就想到，因為我們在同一條路上其實就有7個觀測站，如果把7個站的速度當作一組數據，經過10分鐘後的速度當另一組數據，這樣就可以對前後兩個時刻的速度做成對樣本T檢定，來判斷是否有顯著差異。我們直接用試算表內的T.TEST函式進行運算，只要P值小於0.05就視為顯著速度差異，並將這些時間點標註在整條路段平均速度與時間的折線圖上。(因為半夜的車速不太穩定，分析起來沒有太大意義，所以我們只分析5:00~23:00的數據)
* Q1-3 : To observe the feature of speed in rush hours of different spots.
	* 箱形圖
* Q2 : Can we assume that the speed at each and every adjacent observation spot are the same?
	* The difference in speed between spots are subtle but important
	
* Q2-1 : The relation between adjacent observation spots
	* We found that the speed curve of some adjacent observation spots  have the same trend
	* We plot the v-t curve again with z-score to vanish the gap between spots 
![image](https://github.com/shiny880410/helloworld/blob/master/hw1/%E5%BE%A9%E8%88%88%E5%8C%97%E8%B7%AF479%E5%B7%B7-%E6%B0%91%E6%97%8F%E6%9D%B1%E8%B7%AF(%E7%B4%85)%E3%80%81%E6%B0%91%E6%97%8F%E6%9D%B1%E8%B7%AF-%E6%B0%91%E7%94%9F%E6%9D%B1%E8%B7%AF(%E8%97%8D).png)
![image](https://github.com/shiny880410/helloworld/blob/master/hw1/Z-score.png)
	* Describe how two curves close to each other [Fréchet distance](https://github.com/shiny880410/helloworld/blob/master/hw1/Frechet.ipynb)
## **2019-03-21 Week5**

* Q6 : Heat map of speed
	* Draw the heatmap of car speed of 復興路 during a day (matplotlib) [Heatmap](https://github.com/shiny880410/helloworld/blob/master/hw1/heatmap.ipynb)
![image](https://github.com/shiny880410/helloworld/blob/master/hw1/heatmap.png)
## **2019-03-28 Week6**
* Q7 : We plan to conduct Leibniz integral rule to see that whether the car speeds perform fluid properties
## **2019-04-04 Week7**