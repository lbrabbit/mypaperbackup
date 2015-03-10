from string import replace
import re

outfile=file('txt_chinese.py','w+')
outfile.write("txt_backstage=['','','']\n")
outfile.write("txt_userid2=['','','']\n")

mapping={
'txt_backstage[0]': '�ӤH�s�D�x��x�ƥ�',
'txt_backstage[1]': 'Taipeilink�d�����ƥ�',
'txt_backstage[2]': '�L�W�d���O�ƥ�',
'txt_error_noid'  : '�п�J�b��',
'txt_error_start' : '�п�J�}�l����',
'txt_error_end'   : '�п�J��������',
'txt_error_bigger': '�}�l���Ƥ񵲧����Ƥj',
'txt_error_fpath' : '�ƥ����|�����T',
'txt_error_IO'    : '�����s���W��',
'txt_error_in'    : 'Ū�����ɮת�',
'txt_error_out'   : '�g�����ɮת�',
'txt_error_proxy' : "Proxy�]�w�����D\n���ˬdproxy�O�_��'http://proxy.abc.com:8080/'",
'txt_error'       : '�����D�� -.-\n(�p�ƥ����|�����T)',
'txt_userid1'     : '�x���b��',
'txt_userid2[0]'  : '(�Ҧppchome2004)',
'txt_userid2[1]'  : '(�Ҧpmollyabc)',
'txt_userid2[2]'  : '(�Ҧplbrabbit)',
'txt_browse'      : '�s��',
'txt_stop'        : '�Ȱ�',
'txt_quit'        : '���}',
'txt_title'       : '�d�����ƥ�',
'txt_start'       : '�}�l����',
'txt_end'         : '��������',
'txt_backup'      : '�ƥ�',
'txt_path'        : '�ƥ��x�s��m',
'txt_mark'        : '�аO',
'txt_tech'        : '(�޳N�H����)',
'txt_askquit'     : '�n���}��?',
'txt_no'          : '��',
'txt_page'        : '��',
'txt_complete'    : '����',
'txt_break'       : '���~�פ�',
'txt_create'      : '�s�@',
'txt_txtfile'     : '��r��',
'txt_allin1'      : 'All in 1������',
'txt_help'        : '����',
'txt_not_ava'     : "���{�����@�̤��i�F\n�S�}�o�o�ӥ\��\n���L�{������X�O���}��\n�p�G�A���s�{\n�i�H������� *^_^*"
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
