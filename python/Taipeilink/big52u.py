from string import replace
import re

mapping={
'txt_error_noid'  : '�п�J�b��',
'txt_error_start' : '�п�J�}�l����',
'txt_error_end'   : '�п�J��������',
'txt_error_bigger': '�}�l���Ƥ񵲧����Ƥj',
'txt_error_fpath' : '�ƥ����|�����T',
'txt_error_IO'    : '�����s���W��',
'txt_error_in'    : 'Ū�����ɮת�',
'txt_error_out'   : '�g�����ɮת�',
'txt_error_proxy' : "Proxy�]�w�����D\n���ˬdproxy�O�_��'http://proxy.abc.com:8080/'",
'txt_error'       : '�ƥ����|�����T',
'txt_userid1'     : '�x���b��',
'txt_userid2'     : '(�Ҧpmollyabc)',
'txt_browse'      : '�s��',
'txt_stop'        : '�Ȱ�',
'txt_quit'        : '���}',
'txt_title'       : 'Taipeilink�ƥ�',
'txt_backstage'   : 'Taipeilink�d�����ƥ�',
'txt_start'       : '��x�}�l����',
'txt_end'         : '��x��������',
'txt_backup'      : '�ƥ�',
'txt_path'        : '�ƥ��x�s��m',
'txt_mark'        : '�L��',
'txt_tech'        : '',
'txt_askquit'     : '�n���}��?',
'txt_no'          : '��',
'txt_page'        : '��',
'txt_complete'    : '����',
'txt_break'       : '���~�פ�',
'txt_create'      : '�L��',
'txt_txtfile'     : '',
'txt_allin1'      : 'All in 1������',
'txt_help'        : '����'
}

#print "\n"
#for k, v in mapping.items():
#	print k,' = ',repr(unicode(v,'big5_tw'))

outfile=file('txt_chinese.py','w+')
for k, v in mapping.items():
	outstr = k+' = '+repr(unicode(v,'big5_tw'))+'\n'
	outfile.write(outstr)

infile=file('readme.txt','r+')
buf=infile.read()
buf=repr(unicode(buf,'big5_tw'))
buf=re.compile('\\\u').sub(' \u',buf)
outstr='readme_uni = '+buf+'\n'
outfile.write(outstr)
outfile.close()
