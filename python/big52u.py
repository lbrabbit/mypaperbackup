from string import replace
import re

outfile=file('txt_chinese.py','w+')
outfile.write("txt_backstage=['','','']\n")
outfile.write("txt_userid2=['','','']\n")

mapping={
'txt_backstage[0]': '個人新聞台後台備份',
'txt_backstage[1]': 'Taipeilink留言版備份',
'txt_backstage[2]': '無名留言板備份',
'txt_error_noid'  : '請輸入帳號',
'txt_error_start' : '請輸入開始頁數',
'txt_error_end'   : '請輸入結束頁數',
'txt_error_bigger': '開始頁數比結束頁數大',
'txt_error_fpath' : '備份路徑不正確',
'txt_error_IO'    : '網路連不上喔',
'txt_error_in'    : '讀不到檔案阿',
'txt_error_out'   : '寫不到檔案阿',
'txt_error_proxy' : "Proxy設定有問題\n請檢查proxy是否似'http://proxy.abc.com:8080/'",
'txt_error'       : '有問題喔 -.-\n(如備份路徑不正確)',
'txt_userid1'     : '台長帳號',
'txt_userid2[0]'  : '(例如pchome2004)',
'txt_userid2[1]'  : '(例如mollyabc)',
'txt_userid2[2]'  : '(例如lbrabbit)',
'txt_browse'      : '瀏覽',
'txt_stop'        : '暫停',
'txt_quit'        : '離開',
'txt_title'       : '留言版備份',
'txt_start'       : '開始頁數',
'txt_end'         : '結束頁數',
'txt_backup'      : '備份',
'txt_path'        : '備份儲存位置',
'txt_mark'        : '標記',
'txt_tech'        : '(技術人員用)',
'txt_askquit'     : '要離開嗎?',
'txt_no'          : '第',
'txt_page'        : '頁',
'txt_complete'    : '完成',
'txt_break'       : '中途終止',
'txt_create'      : '製作',
'txt_txtfile'     : '文字檔',
'txt_allin1'      : 'All in 1全備檔',
'txt_help'        : '說明',
'txt_not_ava'     : "本程式的作者太懶了\n沒開發這個功能\n不過程式的原碼是公開的\n如果你懂編程\n可以來幫手阿 *^_^*"
}

#print "\n"
#for k, v in mapping.items():
#	print k,' = ',repr(unicode(v,'big5_tw'))

for k, v in mapping.items():
	outstr = k+' = '+repr(unicode(v,'big5_tw'))+'\n'
	outfile.write(outstr)


infile=file('readme.txt','r+')
buf=infile.read()
buf=repr(unicode(buf,'big5'))
buf=re.compile('\\\u').sub(' \u',buf)
outstr='readme_uni = '+buf+'\n'
outfile.write(outstr)
outfile.close()
