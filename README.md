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
* Q2 : Using gif to make the results more clear. 
	* Draw the line graph that varies with time during a day (matplotlib) [Line Graph2](https://github.com/shiny880410/helloworld/blob/master/hw1/復興南路2.ipynb)
![image](https://github.com/shiny880410/helloworld/blob/master/hw1/%E5%BE%A9%E8%88%88%E5%BE%80%E5%8D%97.gif)
	* 小結論 : 從動圖中我們可以發現，復興路的壅塞時段沒有如交控中心所訂定的如此明確而侷限。上午 7:00 至 9:00 速率沒有大幅降低，反而是連續降低的過程，且一路到下午，構成"日間時段"，而 17:00 至 19:00 的下班時間則有明顯壅塞，速率最後會於晚間回升。有了這些初步觀察，我們想知道是否能透過分析訂定出適合復興路的尖峰、離峰時段，讓交控更彈性更有效率。
* Q3 : How to define rush hour of 復興路 ?
	Method 1. Define peak time / off-peak time with the greatest slope : Paired samples t-test
	* The rad spots indicate that p value<= 0.045
	* The numbers in the graph is the weighted average ( w.r.t. the distance of VDs ) of the speed in different spots, which represents the road speed [Average speed +T-test](https://github.com/shiny880410/helloworld/blob/master/hw1/%E6%A8%99%E8%A8%98%E9%A1%AF%E8%91%97%E9%80%9F%E5%BA%A6%E5%B7%AE%E7%95%B0.ipynb)
![image](https://github.com/shiny880410/helloworld/blob/master/hw1/%E6%95%B4%E9%AB%94%E5%B9%B3%E5%9D%87.png)
	* Define peak time / off-peak time with outliers : One sample t-test
	* Result : no specific congestion in traffic ( p value >= 0.05 )
* Q5 : To observe the feature of speed in rush hour of different spots
	* 箱形圖

* Q3 : Can we assume that the speed at each and every adjacent observation spot are the same?
	
	* The difference in speed between spots are subtle but important
	
* Q3 : The relation between adjacent observation spots
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