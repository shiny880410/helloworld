# DataScience_期末專題 : 車流車速分析與預測
## 透過規劃道路使交通更順暢_利用 Neural Network 預測車速
* 網路爬蟲抓取資料
	* 由**臺北市政府資料開放平台**抓取資料
	<br />經過討論，我們的期末專題所需要的數據不只車流車速，然而為了保持時間軸的一致性，我們重新抓取資料。較特別的是因為我們發現測站會隨著時間不同而有開啟或關閉等狀態改變，導致在政府網頁上並非依照固定欄位呈現，因此我們調整抓取資料的方式，先判別測站名稱再抓資料，以確保資料的正確性。 [(臺北市政府資料開放平台)](https://data.taipei/#/dataset/detail?id=b5aaf33a-a6dc-4836-bce6-09986241fe11)/[(程式碼)](https://script.google.com/d/MkB5D-mxRFlsVQUA70Tq1n_RWp2vJfyNW/edit?mid=ACjPJvGNqDEAWEKcgpe9iFvj8Rk_xubtqxJCBUQo6A3zcncTWhsvwpewYuxSAtNAp5aKHzhZfnKixDrrCV2H79caQT1OVHsvXbiEnAMzPRyhTzO35Brrj5v5YyvEq-HVmlyYtDPX6Ltkdls&uiv=2)
	* 抓下來的**動態資料**原始數據
	<br />我們將動態資料爬下來，包括車流、車速、車道佔有率。[(原始數據_工作頁speeddata/occdata/voldata)](https://docs.google.com/spreadsheets/d/1ACNaFULWc7k1iO9GCjpcKbu3RB0O81z2xHdDfjymZeM/edit?usp=sharing)
	* 用Google map查看站點**靜態資料**
	<br />我們藉由站點位置的經緯度在Google map上查看相對應的站點實際位置，並依照空拍圖蒐集站點靜態資訊。
* 資料清洗與補齊缺漏
	* 合併動態資料與站點靜態資料
	<br />將每個對應站點所抓取的動態資料結合靜態資料，例如長度、車道數、紅綠燈數等，成為新的一筆完整資料以利分析。[(工作頁data)](https://docs.google.com/spreadsheets/d/1ACNaFULWc7k1iO9GCjpcKbu3RB0O81z2xHdDfjymZeM/edit?usp=sharing)
	* 補齊缺失資料
	<br />最後將上述整理好的數據一併排到新的試算表，但是因為觀測站有時候會故障或是停止運行，因此我們在準備進行之後的運算之前，也將數據是零或缺漏的資料刪掉。[(TrainingData)](https://docs.google.com/spreadsheets/d/1_L_CG5WhF5oZUvpmJTWEbEmHHGJ1-boQ9oxyfILFJyU/edit?usp=sharing)/[(程式碼)](https://script.google.com/d/M2x1ULQ30kOKELKOaxGGBf_RWp2vJfyNW/edit?mid=ACjPJvGaMJuseqNPx-WiVnCth5OJfkgoc1EFCmRAp-uIE4QSZXgJUL0E6__4iX91mwSlq3v1FRB8OdfEnhls7EbXY6I1vtCdOI06EJEOJQfkj6WTgYfrgaWaevd5nmhVEcRs-p4su0fbCj4&uiv=2)
* 找出與車速有關的參數 
	* 瀏覽交通相關文章
	<br />在進入分析之前，我們也上網看了許多交通分析的資料，發現一個道路的交通狀況可以用巨觀、中觀、微觀的方法進行分析。其中，巨觀的方式著重流量、密度及速率間的關係，主要分析某一段時間內或某一路段內之車流總量或平均的總體行為，較符合我們的分析方式，因此我們也先分別將資料進行作圖並與理論比較。
	* 多階段車流模式
	<br />巨觀分析又分為兩個模式，單一與多階段車流模式。多階段車流模式為車流行為在自由車流與擁擠車流狀態時候，因為表現不同，所以利用多條函數關係描述不同交通狀態。我們將流量、密度及速率作圖並與理論曲線比較，如下圖 : [(程式碼)](https://github.com/shiny880410/helloworld/blob/master/final/files/%E6%95%A3%E4%BD%88%E5%9C%96.ipynb)
		<div align=center><img width="400" height="250" src="https://github.com/shiny880410/helloworld/blob/master/final/files/%E5%AF%86%E5%BA%A6-%E6%B5%81%E9%87%8F.png"/></div>
		<div align=center><img width="400" height="250" src="https://github.com/shiny880410/helloworld/blob/master/final/files/%E5%AF%86%E5%BA%A6-%E9%80%9F%E7%8E%87.png"/></div>
		<div align=center><img  src="https://github.com/shiny880410/helloworld/blob/master/final/files/%E6%B5%81%E9%87%8F-%E5%AF%86%E5%BA%A6.png"/></div>	
		<br />由上圖可以看到我們的數據跟理論還是有蠻大的落差，因我們希望能換個角度思考。
	* 用流體力學觀點加入**黏滯係數**與**壓力差**進行討論
		<br />從圖中我可以發現，我們的資料和理論有差異，我們推論是因為理論是在描述比較理想的情況，例如沒有考慮路口、轉彎車、車道縮減等等實際道路上的狀況，因此我們試圖從另一個角度進行分析，以選定放入Neural Network的 X-train data 。我們需要找出主要影響車速變化的重要參數，但由於道路性質複雜難以以理論滿足，經過討論之後，我們將其想像成二維平板流進行分析，並列出下列物理量，探討其是否適用流體性質。如下圖，我們假設車流流過一條路就像以速度U，流經上下兩片不記寬度、有限長度L的平行板之間的流體，且平行板間相距D，並在單位時間流過體積V。我們假設驅動流體的壓力差ΔP是由紅綠燈造成，只是紅綠燈提供的是阻力。就像在一段路上，若紅綠燈提供壓力阻止車子前進，而車子在沒有阻礙的情況下會很自然地想往前，那車子最後前進的速度就會跟紅綠燈有關了，所以我們假設紅綠燈數為控制車流前進的壓力梯度。而流體密度則是以車道佔有率(特定時間內一小路段被車輛佔據的時間百分比)表示，因為兩者呈正比。且路口左轉之車流待轉時會減速至幾乎靜止，和邊界無滑動之流體相互對應，因此我們以黏滯係數代表紅綠燈能左轉造成的回堵程度。
		<div align=center><img  src="https://github.com/shiny880410/helloworld/blob/master/final/files/plate.PNG"/></div>
		<div align=center><img  src="https://github.com/shiny880410/helloworld/blob/master/final/files/pic.PNG"/></div>		       
		* 利用 **Buckingham Pi Theorem** 進行無因次化
		<br />確定好了7個物理量後，由於這些物理量共有3個獨立的因次，則原方程式可以寫成由4個無因次的參數 π1, π2, π3, π4組成的方程式，而這些無因次的參數是由原方程式中的物理量所組成。這個方法讓我們就算不用理論找出參數間確切的方程式也能找出其中和我們關心的車速相關的物理量，是較經濟也較方便的做法。在選取repeating variables時，因為是要找和速度的關聯性，因此要避開速度項，並分別由幾何形狀、流體性質、動力學三個方面選取獨立的參數，因此在這裡我們選擇了**ρ**、**D**、**ΔP**，並得到下列 π 項。
		<div align=center><img  src="https://github.com/shiny880410/helloworld/blob/master/final/files/pi1.gif"/></div>
		<div align=center><img  src="https://github.com/shiny880410/helloworld/blob/master/final/files/pi2.gif"/></div>
		<div align=center><img  src="https://github.com/shiny880410/helloworld/blob/master/final/files/pi3.gif"/></div>
		<div align=center><img  src="https://github.com/shiny880410/helloworld/blob/master/final/files/pi4.gif"/></div>
		<br />並得到無因次的π1與其他π之間的關係 :
		<br />
		<div align=center><img  src="https://github.com/shiny880410/helloworld/blob/master/final/files/pis.gif"/></div>
		<br />由上面結果可以發現，速度和**體積流率**、**黏滯係數**、**平板間距**有關，呼應了我們在hw4-6中的Neural Network裡依照生活經驗選擇輸入的三個X-data : 車流、紅綠燈能左轉之個數與車道數。同時，我們也發現π1平方之後就是流體裡的pressure coefficient (Cp)，而Cp又是在描述一個流體裡的Static pressure 與 Dynamic pressure 的關係，因此可以用來形容紅綠燈數目與車速之間相互影響的狀況與比例關係。
		<div align=center><img  src="https://github.com/shiny880410/helloworld/blob/master/final/files/CP.PNG"/></div>
	* 作圖並找相關係數
		<br />由於其中的理論很複雜，難以進行分析得到解析解，因此我們將π1(含有速度項)對不同的π作圖，並求其相關係數，來得道我們預期的車速與其他參數間的關係。因為π2是車道數，不連續，因此我們只和π3、π4作圖，希望能透過運算讓不同π之間是接近線性的，以提高之後預測的準確度。π1和π3之間，代表速度與流量之間的關係，由於從理論可以知道速度與密度是線性關係，且密度與流量呈二次曲線，所以速率與流量也應呈拋物線，我們將π3開根號之後，得到與π1線性相關，且相關係數為0.86。而我們最後透過反覆嘗試，將π4倒數開根號，並發現圖形分支成許多斜率不同的直線。因此我們推論應該是由於我們所選用的對應道路性質並不是能最佳描述這個狀態的參數，不然應該會重合成一條線，但由於其中的線性關係依然成立，我們依然將其放入x-train data，並由NN依照差別進行預測。
		<div align="center"><img width="400" height="250" src="https://github.com/shiny880410/helloworld/blob/master/final/files/pi3-pi1.png"/><img width="400" height="250" src="https://github.com/shiny880410/helloworld/blob/master/final/files/sqrt_pi3-pi1.png"/></div>
		<div align="center"><img width="400" height="250" src="https://github.com/shiny880410/helloworld/blob/master/final/files/pi4-pi1.png"/><img width="400" height="250" src="https://github.com/shiny880410/helloworld/blob/master/final/files/sqrt_pi4^-1-pi1.png"/></div>
* 將資料放入Neural Network進行訓練
	* 讓過程自動化 [(程式碼)](https://github.com/shiny880410/helloworld/blob/master/final/files/downloadcsv.ipynb)
	<br />由於在每次training前，都要將整理好的數據再分別存成要train的數據以及要用來預測的數據。經過上次hw4-6的training之後，我們覺得其中的過程耗時又繁瑣，當資料量大時就會容易出錯，因此我們到後期讓雲端試算表中的資料分別自動存成要訓練的csv檔與用來預測的csv檔，並在存完之後自動上傳至雲端，讓我們只需要將檔案下載至程式碼中，就可以進行training，並在結束之後將模型保存下來。
	* 放入變換後的資料進行訓練
	<br />我們將變換過後的 π2, π3, π4 ,π1匯入進行訓練，不斷調整節數與層數，再由模型輸出 π1 並計算誤差。(training history ，如何設計節點數)[(Neural network final_2)](https://github.com/shiny880410/helloworld/blob/master/final/files/Final_NN2.ipynb)
		<div align=center><img  src="https://github.com/shiny880410/helloworld/blob/master/final/files/nodes.PNG"/></div>
	* 調整batch size
	<br />我們由batch size=128 (Neural network final_2) 開始調整，再經過多次調整，直到模型不能再進步為止，最後得到batch size=100。[(Neural network final_1)](https://github.com/shiny880410/helloworld/blob/master/final/files/Final_NN1.ipynb)
* 將預測的數據作圖與結論

## 降低死亡車禍率_分析A1與A2交通事故原因並比較
* 下載與取得資料
	* 由臺北市政府資料開放平台下載 107年度A1及A2類交通事故明細、事故代碼對照表[(臺北市政府資料開放平台)](https://data.taipei/#/dataset/detail?id=2f238b4f-1b27-4085-93e9-d684ef0e2735)
	<br />A1指造成人員當場或二十四小時內死亡之交通事故；A2指造成人員受傷或超過二十四小時死亡之交通事故。
	* 由內政資料開放平台下載全國路名資料[(內政資料開放平台)](https://data.moi.gov.tw/MoiOD/data/DataDetail.aspx?oid=E2EDC47D-2D3F-4EB1-878A-4DEB6160FD4C)
	<br />我們想得知臺北市所有道路名稱以利後續對龐大的交通事故數分類。
* 整理資料成適合分析的格式
	* 將資料裡的代碼依照對照表換成文字[(工作頁_Data3)](https://docs.google.com/spreadsheets/d/1A3V6ncj7VLNDiDkchaYPIYmqrA0trkEj8L-tHoaAyZs/edit?usp=sharing)
	<br />由於原始資料是將對撞的交通事故分為兩起案件紀錄(即為每一車留下一筆紀錄)，不方便我們分析，故我們以時間軸將同一場車禍資料合併，才能發現車禍與車禍之間的相關性，例如對撞車種之間的關聯性等等。另外，為了不讓資料遺失，我們將"死亡"字串出現在文本的次數，代替每起案件的死亡人數(受傷者亦同)，並用文字以十歲為區間代替年齡，讓數字資料只剩下車速以利判讀。
	* 將臺北市各路段依照A2交通事故發生頻率排列
	<br />因為A2交通事故高達兩萬多筆，相較於A1七十四筆數量多很多，因此不利直接進行共現性分析，所以我們將其依照路段發生事故的頻率列出，找出最常發生事故之路段。 [(程式碼)](https://github.com/shiny880410/helloworld/blob/master/final/files/%E9%95%B7%E6%A2%9D%E5%9C%96.ipynb)
	<div align=center><img  src="https://github.com/shiny880410/helloworld/blob/master/final/files/bar.png"/></div>
	<br />由上圖可知，忠孝東路位居第一，市民大道位居第二，在A2交通事故中，我們以忠孝東路、市民大道與復興南北路進行分析。
* 進行共現性分析與呈現
	* A1交通事故
	<br />將所關心的關鍵字詞列出來，並觀察彼此交互在文本(不同場車禍)之間出現的次數，最後將矩陣降維呈現，並剔除多數影響較不顯著的因素，留下影響車禍發生的主因，從圖中可以看出名詞之間的相關性。[(A1車禍事故明細分析)](https://github.com/shiny880410/helloworld/blob/master/hw4-6/PCA2.ipynb)
	<br />從最後所畫成的圖表，我們可以發現死亡車禍確實有和許多特定的詞彙相關，而這也對應到了特定的族群、車種、環境與道路型態。而從這些訊息可以提供相關單位改善道路的方向與進行有效的宣導或臨檢。
		* 我們可以發現以台北市而言，機車是與死亡車禍高度相關的車種之一，再進而參照文本內事發路段，可得知臺北市對外縣市交界的機車道是需要改善的重點道路之一。
		* 50km/hr明顯相較於低時速顯著，因此推論死亡車禍在事發當時車速普遍較高，而另一方面我們也可以發現快車道較慢車道與死亡關聯性更高。
		* 男性較女性更傾向以高速行駛，二十到三十歲是發生事故的主要年齡層，因此可有效的局部加強宣導相關道路安全觀念。
		* 晴天也十分容易發生死亡車禍，因此推估天氣對事故發生影響有限。 
		* 行人易在交叉路口附近發生車禍，因此有關的交通標誌可能要進行改善。
		![image](https://github.com/shiny880410/helloworld/blob/master/hw4-6/q2.PNG)
	* A2交通事故
	<br />我們依照上述方法對分組過後的A2交通事故進行分析。
	<br />1. **忠孝東路** [(程式碼)](https://github.com/shiny880410/helloworld/blob/master/final/files/Zhongxiao.ipynb)
		<div align=center><img width="600" height="600"  src="https://github.com/shiny880410/helloworld/blob/master/final/files/Zhongxiao.png"/></div>
	<br />2. **市民大道** [(程式碼)](https://github.com/shiny880410/helloworld/blob/master/final/files/ShiMin.ipynb)
		<div align=center><img width="600" height="600"  src="https://github.com/shiny880410/helloworld/blob/master/final/files/ShiMin.png"/></div>
	<br />3. **復興南北路** [(程式碼)](https://github.com/shiny880410/helloworld/blob/master/final/files/Fuxing.ipynb)
		<div align=center><img width="600" height="600"  src="https://github.com/shiny880410/helloworld/blob/master/final/files/Fuxing.png"/></div>
	由結果來看，我們可以發現一些A2交通事故共同享有的特徵 :	
	<br />和A1交通事故相同，機車皆和事故的發生十分相關，且多為年輕族群，A2交通事故涵蓋車種較豐富。另外，忠孝東路與市民大道分別為臺北市發生事故次數前兩名的路段，除了道路較長、為重要幹道之外，我們可以藉由與同樣是重要道路的復興南北路相比，發現他們較復興南北路多了交叉路口與四岔路等較為複雜的道路型態，且他們與受傷的共現性也較單純的路段多，因此我們應重視路口安全與道路規劃。
* A1事故與A2事故比較與結論
	<br /> 由上述分析，我們可以發現其實發生A1、A2事故的特徵大同小異，不論是容易發生車禍的道路型態、年齡層等都十分相似，天氣的影響也十分有限，主要有些微差異的是死亡類型的車禍的主因中有快車道與行人，而受傷類型車禍則無。因此推論發生事故條件相似的情況下，一旦發生事故，車速高致死率也較高。而行人相較於駕駛與乘客，處於較無防護的狀態，因此事故後也較易傾向有重大傷勢甚至死亡。




















