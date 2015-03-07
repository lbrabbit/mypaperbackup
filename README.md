# mypaperbackup
Backup Tools for a Variety of Message Board一個能將幾種留言版備份的軟體

This is a record of the project hosted previously on OpenFoundry 
https://www.openfoundry.org/of/projects/99

Description：	一個能將幾種留言版備份的軟體

Maturity：	PREALPHA

Programming Language：	Perl, Python

Created at：	2004-03-19 12:34 +08:00

留言板備份軟體  
作者：小兔黑黑(蘇孝恆)

簡介
--------
PChome個人新聞台在二零零四年初曾要強行砍掉所有過千則以外的後台留言，很多網友要匆忙地找網頁備份軟體，不過大部份的軟體是跟著連結去備份，會把他人的後台也抓回來。本軟體因為是為個人新聞台度身製作，令這個問題得到糾正，而且還可以把內容轉為文字檔。當內容轉為文字檔後，可以除去PChome的廣告和更容易尋找留言，並可以減少一些法律上的麻煩。

跟著Taipeilink在2005年三月17日關閉，大家如果未轉去Photolink，留言版的留言不知何時會消失。相片大概也有備份，不過朋友的留言就很珍貴囉。我就將軟體改了一點來作Taipeilink的備份。

之後我又改了一點來作無名留言板的備份，所以這軟體現在可以做三個站的備份。

本軟體另一個特色就是它是自由軟體(GNU GPL授權)。自由軟體包括有四方面的自由：
 * 任意使用的自由；
 * 研究及修改以符合自己用途的自由；
 * 拷貝給親朋好友的自由；
 * 散布修改後的軟體的自由。

如果想多點認識自由軟體，可以參考洪老師和藹可親的介紹文章阿 ^^
http://www.cyut.edu.tw/~ckhung/ (見「短文 [articles]」和「演講摘要 [slides]」)

本軟體是v0.1版，還有很多地方需要改善，請多多指教。

本軟體的網站在無名，可以來看看留個言。
(http://www.wretch.cc/blog/lbrabbit&category_id=907623)
程式的開發網站在中研院資訊所的自由軟體鑄造場，可利用「待辦事項」報告錯誤和你想要的新功能。
(http://rt.openfoundry.org/Foundry/Project/index.html?Queue=99)

功能介紹
--------
本軟體有兩大功能，第一是把個人新聞台後台的留言一頁一頁的拷貝至電腦的硬碟中，另一個就是把留言內容抽出來，放在文字檔。

要這軟體乖乖的為你服務，你先要告訴它一些必要的資料：

Proxy : 先留空白，如果備份時有錯誤訊息，可以在微軟的瀏覽器Internet Explorer的網際網路選項->「連線」->「區域網路(Lan)設定」->「Proxy何服器」中找出來的。

備份儲存位置 : 就是你想把拷貝放在硬碟的什麼地方，可以鍵入路徑，也可按「瀏覽」去找。請先設好資料夾，在「瀏覽」中沒有設定新資料夾的機會阿 :P

台長帳號、開始頁數、結束頁數 : 這幾個不難明白吧 ;)

標記(技術人員用) : 在製作文字檔時，可以把一些標記在每一項的前頭，如%或^，以方便其他程式讀入。

填好了資料後就可以叫軟體為你辦事了 ^^

要用第一大功能請按「備份」，在後台的網頁就會逐頁被拷貝下來。
要用第二大功能請按「製作文字檔」(Taipeilink沒有)，程式就會由被拷貝下來的後台網頁抽出留言內容，轉為文字檔。所有的文字檔會匯合為一個All in 1 全備檔，以方便搜查。
如果要中途停止，可按「暫停」。
要結束，請按「離開」。

程式輸出的檔案名稱：

拷貝下來的網頁　　台長帳號_XXXX.htm
留言文字檔　　　　台長帳號_XXXX.txt
全備檔　　　　　　XXXXtoYYYY_台長帳號.txt

Linux
--------
Linux用戶可直接執行Python的原始碼，不過需先安裝Tkinter library。而安裝Tkinter可能要先安裝tcl,tk,itcl和tix等library，視乎貴電腦所用的Linux版本。

個人新聞台上的法律考慮
--------
在個人新聞台的使用條款中有兩條有關版權的條款：

3. 使用者上載於 PChome Online「個人新聞台」之所有著作及資料，其著作權或其他智慧財產權仍然歸使用者或授權使用者使用之合法權利人所有。
2. PChome Online「個人新聞台」所提供的所有網頁設計、介面、URL、商標或標識、電腦程式、資料庫等，其商標、著作權、其他智慧財產權及資料所有權等，均屬於 PChome Online「個人新聞台」或授權 PChome Online「個人新聞台」使用之合法權利人所有。

在網上後台的每一頁也是網頁設計、介面和使用者著作的混合體，所以如果把後台的留言一頁一頁的拷貝至電腦的硬碟中，就是把一些PChome Online「個人新聞台」慧財產權的東西抄回來。只有把內容轉為文字檔，不用網頁形式，才可脫離PChome慧財產權範圍。文字檔中的用詞和編排也特別跟後台的不同，以免有抄襲後台外觀之嫌。如果真的有一天PChome要在慧財產權上搞事，用戶只要刪去網頁拷貝即可，留言的內容仍然會在文字檔中。

鳴謝
--------
中研院資訊所自由軟體鑄造場 (http://rt.openfoundry.org/)
EasyGUI by Stephen Ferg (http://www.ferg.org/easygui/index.html)
無名小站 (http://www.wretch.cc/)
心靈小憩的藝文與科技生活園地 (http://he.cycu.edu.tw/phpBB21/)
雨漣
小地震








This program is superceded by the littleext FIrefox extension

留言板備份軟體已經停止更新，PChome個人新聞台的後台留言因為網址更改而不能使用。無名留言版備份由我寫的火狐「我的小擴充套件  」取代，請參考http://littleext.openfoundry.org/
