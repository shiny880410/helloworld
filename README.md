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
* The data is from Taipei city government website (Update every five minutes)
* 7 observation spot on 復興路
* Average car speed in weekdays
* To know the relation between car speed and time, we do the data tidying 
to make variables forms a column, and the observation in the same timeforms a row.
* To eliminate the meaningless fluctuations, we average the speed every 15 minutes.
## **2019-03-14 Week4**
### HW2&3 : Exploratory Data Analysis (EDA) : Speed on the Roads
* Q1 : Can we assume that the speed at each and every adjacent observation spot are the same?
	* Draw the line graph of car speed on each spot during a day (matplotlib) [Line Graph](https://github.com/shiny880410/helloworld/blob/master/hw1/linegraph.ipynb)
	* Define peak time / off-peak time with the greatest slope
	*  
![image](https://github.com/shiny880410/helloworld/blob/master/hw1/linegraph.png)
* Q2 : Can we assume that the speed at each and every adjacent observation spot are the same?
	* Draw the heatmap of car speed of 復興路 during a day (matplotlib) [Heatmap](https://github.com/shiny880410/helloworld/blob/master/hw1/heatmap.ipynb)
	* Define peak time / off-peak time with the greatest slope
	*  
![image](https://github.com/shiny880410/helloworld/blob/master/hw1/heatmap.png)
* Q3 : 
	* Draw the line graph that varies with time during a day (matplotlib) [Line Graph2](https://github.com/shiny880410/helloworld/blob/master/hw1/linegraph2.ipynb)
	*



## **2019-03-21 Week5**