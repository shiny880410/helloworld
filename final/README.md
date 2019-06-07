# DataScience_期末專題 : 車流車速分析與預測
## 透過規劃道路使交通更順暢_利用 Neural Network 預測車速
* 網路爬蟲抓取資料
	* 由臺北市政府資料開放平台抓取資料
	<br />經過討論，我們的期末專題所需要的數據不只車流車速，然而為了保持時間軸的一致性，我們重新抓取資料。較特別的是因為我們發現測站會隨著時間不同而有開啟或關閉等狀態改變，導致在政府網頁上並非依照固定欄位呈現，因此我們調整抓取資料的方式，先判別測站名稱再抓資料，以確保資料的正確性。 [(台北市政府資料開放平台](https://data.taipei/#/dataset/detail?id=b5aaf33a-a6dc-4836-bce6-09986241fe11)/[程式碼)](https://script.google.com/d/MkB5D-mxRFlsVQUA70Tq1n_RWp2vJfyNW/edit?mid=ACjPJvGNqDEAWEKcgpe9iFvj8Rk_xubtqxJCBUQo6A3zcncTWhsvwpewYuxSAtNAp5aKHzhZfnKixDrrCV2H79caQT1OVHsvXbiEnAMzPRyhTzO35Brrj5v5YyvEq-HVmlyYtDPX6Ltkdls&uiv=2)
	* 抓下來的動態資料原始數據
	<br />我們將動態資料爬下來，包括車流、車速、車道佔有率。[(原始數據_工作頁speeddata/occdata/voldata)](https://docs.google.com/spreadsheets/d/1ACNaFULWc7k1iO9GCjpcKbu3RB0O81z2xHdDfjymZeM/edit?usp=sharing)
	* 用Google map查看站點靜態資料
	<br />我們藉由站點位置的經緯度在Google map上查看相對應的站點實際位置，並依照空拍圖蒐集站點靜態資訊。
* 資料清洗與補齊缺漏
	* 合併動態資料與站點靜態資料
	<br />將每個對應站點所抓取的動態資料結合靜態資料，例如長度、車道數、紅綠燈數等，成為新的一筆完整資料以利分析。[(工作頁data)](https://docs.google.com/spreadsheets/d/1ACNaFULWc7k1iO9GCjpcKbu3RB0O81z2xHdDfjymZeM/edit?usp=sharing)
	* 補齊缺失資料
	<br />最後將上述整理好的數據一併排到新的試算表，但是因為觀測站有時候會故障或是停止運行，因此我們在準備進行之後的運算之前，也將數據是零或缺漏的資料刪掉。[(TrainingData)](https://docs.google.com/spreadsheets/d/1_L_CG5WhF5oZUvpmJTWEbEmHHGJ1-boQ9oxyfILFJyU/edit?usp=sharing)/[(程式碼)](https://script.google.com/d/M2x1ULQ30kOKELKOaxGGBf_RWp2vJfyNW/edit?mid=ACjPJvGaMJuseqNPx-WiVnCth5OJfkgoc1EFCmRAp-uIE4QSZXgJUL0E6__4iX91mwSlq3v1FRB8OdfEnhls7EbXY6I1vtCdOI06EJEOJQfkj6WTgYfrgaWaevd5nmhVEcRs-p4su0fbCj4&uiv=2)
* 找出與車速有關的參數 
	* 瀏覽交通相關文章
	<br />在進入分析之前，我們也上網看了許多交通分析的資料，發現一個道路的交通狀況可以用巨觀、中觀、微觀的方法進行分析。其中，巨觀的方式著重流量、密度及速率間的關係，主要分析某一段時間內或某一路段內之車流總量或平均的總體行為，較符合我們的分析方式，因此我們也先分別將資料進行作圖並與理論比較。
	* (分別看是符合單一階段車流模式還是多階段車流模式)
![image](數據與理論圖們)(補圖片)
	* 用流體力學觀點加入黏滯係數進行討論
	<br />從圖中我可以發現，我們的資料和理論有差異，我們推論是因為理論是在描述比較理想的情況，例如沒有考慮路口、轉彎車、車道縮減等等實際道路上的狀況，因此我們試圖從另一個角度進行分析，以選定放入Neural Network的 X-train data 。我們需要找出主要影響車速變化的重要參數，但由於道路性質複雜難以以理論滿足，經過討論之後，我們將其想像成二維平板流進行分析，並列出下列物理量，探討其是否適用流體性質。
<div align=center><img  src="https://github.com/shiny880410/helloworld/blob/master/final/files/plate.PNG"/></div>
<div align=center><img  src="https://github.com/shiny880410/helloworld/blob/master/final/files/pic.PNG"/></div>		       
	<br />其中，我們假設紅綠燈數為控制車流前進的壓力梯度，且路口左轉之車流待轉時會減速至幾乎靜止，和邊界無滑動之流體相互對應。而密度則是以車道佔有率(特定時間內一小路段被車輛佔據的時間百分比)表示，因為兩者呈正比。
	* 利用 Buckingham Pi Theorem 進行無因次化
		<br />我們有7個物理量，而這些物理量共有3個獨立的因次，則原方程式可以寫成由4個無因次的參數 π1, π2, π3, π4組成的方程式，而這些無因次的參數是由原方程式中的物理量所組成。這個方法讓我們就算不用理論找出參數間確切的方程式也能找出其中和我們關心的車速相關的物理量，是較經濟也較方便的做法。在選取repeating variables時，因為是要找和速度的關聯性，因此要避開速度項，並分別由幾何形狀、流體性質、動力學三個方面選取獨立的參數，因此在這裡我們選擇了ρ、D、ΔP，並得到下列 π 項。
<div align=center><img  src="https://github.com/shiny880410/helloworld/blob/master/final/files/pi1.gif"/></div>
<div align=center><img  src="https://github.com/shiny880410/helloworld/blob/master/final/files/pi2.gif"/></div>
<div align=center><img  src="https://github.com/shiny880410/helloworld/blob/master/final/files/pi3.gif"/></div>
<div align=center><img  src="https://github.com/shiny880410/helloworld/blob/master/final/files/pi4.gif"/></div>
		<br />並得到無因次的π1與其他π之間的關係 :
		<br />
	<div align=center><img  src="https://github.com/shiny880410/helloworld/blob/master/final/files/pis.gif"/></div>
		<br />由上面結果可以發現，速度和體積流率、黏滯係數、平板間距有關，呼應了我們在hw4-6中的Neural Network裡依照生活經驗選擇輸入的三個X-data : 車流、紅綠燈能左轉之個數與車道數。同時，我們也發現π1平方之後就是流體裡的pressure coefficient (Cp)，而Cp又是在描述一個流體裡的Static pressure 與 Dynamic pressure 的關係，就像在一段路上，若紅綠燈提供壓力阻止車子前進，而車子在沒有阻礙的情況下會很自然地想往前，那車子最後前進的速度就會跟紅綠燈有關了。
	<div align=center><img  src="https://github.com/shiny880410/helloworld/blob/master/final/files/CP.PNG"/></div>
* 作圖並找相關係數
		<br />由於其中的理論很複雜，難以進行分析得到解析解，因此我們將π1(含有速度項)對不同的π作圖，並求其相關係數，來得道我們預期的車速與其他參數間的關係。因為π2是車道數，不連續，因此我們只和π3、π4作圖，希望能透過運算讓不同π之間是接近線性的，以提高之後預測的準確度。π1和π3之間，代表速度與流量之間的關係，由於從理論可以知道速度與密度是線性關係，且密度與流量呈二次曲線，所以速率與流量也應呈拋物線，我們將π3開根號之後，得到與π1線性相關，且相關係數為0.86。
	<div align="center"><img width="400" height="250" src="https://github.com/shiny880410/helloworld/blob/master/final/files/p1p3.PNG"/><img width="400" height="250" src="https://github.com/shiny880410/helloworld/blob/master/final/files/p1sp3.PNG"/></div>
	<div align="center"><img width="400" height="250" src="https://github.com/shiny880410/helloworld/blob/master/final/files/p1p4.PNG"/><img width="400" height="250" src="https://github.com/shiny880410/helloworld/blob/master/final/files/p1sp4.PNG"/></div>
	<br />(補pi4)
* 將資料放入Neural Network進行訓練
	* (倒數等等:我們以 π2, π3, π4為輸入預測 π1，再由 π1換出車速。)[(Neurai network final_1)](https://github.com/shiny880410/helloworld/blob/master/final/files/final_nw.ipynb)
	<br />(training history 跟之前比較準確率大幅提升 如何設計節點數)
* 提升準確率
* 我們嘗試透過不同方法調整輸入值讓預測進步。(補pi4新數據)

## 降低死亡車禍率_分析A1與A2交通事故原因並比較

* 在hw4-6中，我們針對A1交通事故(當場或二十四小時內死亡之交通事故)進行相關性分析並得到和A1交通事故相關的原因。在期末專題中，我們進一步依照同樣方法分析A2交通事故資料並比較。[(A2車禍事故明細分析)](https://github.com/shiny880410/helloworld/blob/master/final/files/PCA3.ipynb)
<br />(補分組)



















