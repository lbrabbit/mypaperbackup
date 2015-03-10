#import os
#import re
#from Tkinter import *
#import tkMessageBox
#execfile('txt_chinese.py')

url_base       ='http://www.wretch.cc/'
url_css        =''
url_css_list   =[]
url_board      ='guestbook/'
url_var        ='&page='
url_differ     =0
read_size      =1024
socket_timeout =120

def extract_items(buf,outfile,addmark):
    title=''
    pattern ='\xE4\xB8\xBB\xE9\xA1\x8C\:' 
    pattern+='.+\"side\"\scolspan\=\"3\"\s>\s*\n'
    pattern+='\s*(.+)\s*\n\s*\<\/td\>'
    pattern+='.+\xE7\x95\x99\xE8\xA8\x80\xE4\xBA\xBA'
    res=re.compile(pattern,re.S).search(buf)
    if res:
        title=res.group(1)

    name=''
    dateofmsg=''
    pattern ='\xE7\x95\x99\xE8\xA8\x80\xE4\xBA\xBA:.+' 
    pattern+='\"side\"\scolspan=\"3\">\s*\n'
    pattern+='\s*(.+\(\d\d\d\d\-\d\d\-\d\d\s\d\d:\d\d:\d\d\))'
    pattern+='.+\xE7\x95\x99\xE8\xA8\x80\xE5\x85\xA7\xE5\xAE\xB9'
    res=re.compile(pattern,re.S).search(buf)
    if res:
        buf1=res.group(1)
        pattern='(\d\d\d\d\-\d\d\-\d\d\s\d\d:\d\d:\d\d)'
        res=re.compile(pattern).search(buf1)
        dateofmsg=res.group(1)
        pattern='\(\d\d\d\d\-\d\d\-\d\d\s\d\d:\d\d:\d\d\)'
        buf1=re.compile(pattern).sub('',buf1)
        buf1=re.compile('\<[^>]+\>').sub('',buf1)
        res=re.compile('^(\S.*)[\x0D\x0A]').search(buf1)
        if res:
            name=res.group(1)
        else:
            name=buf1
        name= 'Name\t'+name+'\n'    
        dateofmsg = 'Date\t'+dateofmsg+'\n'

    Mail=''
    url=''
    pattern ='\xE7\x95\x99\xE8\xA8\x80\xE4\xBA\xBA:.+' 
    pattern+='\(\d\d\d\d\-\d\d\-\d\d\s\d\d:\d\d:\d\d\)\s*\n'
    pattern+='(.+)\n\s*\<\/td\>'
    pattern+='.+\xE7\x95\x99\xE8\xA8\x80\xE5\x85\xA7\xE5\xAE\xB9'
    res=re.compile(pattern,re.S).search(buf)
    if res:
        buf1=res.group(1)
        pattern='\<a\shref=\"mailto:\s*(\S+)\".+email\.gif'
        res=re.compile(pattern,re.S).search(buf1)
        if res:
            Mail=res.group(1)
        pattern='\<a\shref=\"(\S+)\"\starget=.+webpage\.gif'
        res=re.compile(pattern,re.S).search(buf1)
        if res:
            url=res.group(1)
    Mail= 'Mail\t'+Mail+'\n'
    url = 'URL\t'+url+'\n'

    msg=''
    pattern ='\xE7\x95\x99\xE8\xA8\x80\xE5\x85\xA7\xE5\xAE\xB9:.+' 
    pattern+='\"side\"\scolspan=\"3\">\s*\n'
    pattern+='\s*(.+)\s*\<\/td\>'
    if re.compile('\xE6\x9D\xBF\xE4\xB8\xBB\xE5\x9B\x9E\xE8\xA6\x86').search(buf):
        pattern+='.+\xE6\x9D\xBF\xE4\xB8\xBB\xE5\x9B\x9E\xE8\xA6\x86'
    else:
        pattern+='.+\<\/table\>'
    res=re.compile(pattern,re.S).search(buf)
    if res:
        msg=res.group(1)
    msg='Msg\n'+msg+'\n'

    respond=''
    if re.compile('\xE6\x9D\xBF\xE4\xB8\xBB\xE5\x9B\x9E\xE8\xA6\x86').search(buf):
        pattern ='\xE6\x9D\xBF\xE4\xB8\xBB\xE5\x9B\x9E\xE8\xA6\x86:.+' 
        pattern+='\"replyside\"\scolspan=\"3\">\s*\n'
        pattern+='\s*(.+)\s*\<\/td\>'
        pattern+='.+\<\/table\>'
        res=re.compile(pattern,re.S).search(buf)
        if res:
            respond=res.group(1)
    respond='Repsond\n'+respond+'\n'

    try:
        if addmark:    
            outfile.write(addmark+name)
            outfile.write(addmark+dateofmsg)
            outfile.write(addmark+Mail)
            outfile.write(addmark+url)
            outfile.write(addmark+msg)
            outfile.write(addmark+respond)
        else:
            outfile.write(name)
            outfile.write(dateofmsg)
            outfile.write(Mail)
            outfile.write(url)
            outfile.write(msg)
            outfile.write(respond)
        outfile.write('\n\n')
    except IOError:
        tkMessageBox.showwarning(message=txt_error_out+'\n'+fname)
        return 1
    except:
        tkMessageBox.showwarning(message=txt_error)
        raise
        return 1

def convert(fpath,userid,pageno,addmark=False):
    Apps.lbl_status['text']=txt_create+txt_txtfile+txt_no+str(pageno)+txt_page
    Apps.update()
    try:
        fname=fpath+userid+'_%(#)04d'%{'#':pageno}+'.htm'
        infile=file(fname,'r')
    except IOError:
        tkMessageBox.showwarning(message=txt_error_in+'\n'+fname)
        return 1
    except:
        tkMessageBox.showwarning(message=txt_error)
        raise
        return 1
    try:
        fname=fpath+userid+'_%(#)04d'%{'#':pageno}+'.txt'
        outfile=file (fname,'w')
    except IOError:
        tkMessageBox.showwarning(message=txt_error_out+'\n'+fname)
        return 1
    except:
        tkMessageBox.showwarning(message=txt_error)
        raise
        return 1
    flag=0
    curline=infile.readline()
    while (curline):
        if flag==1:
            buf+=htmlspecialchars(curline)
        if re.compile('\<\/table\>').search(curline):
            if flag==1:
                extract_items(buf,outfile,addmark)
                buf=''
                flag=0
        if re.compile('\<!--\sfor\srss\s--\>').search(curline):
            flag=1
            buf=''
        curline=infile.readline()
    outfile.close()
    infile.close()

#convert('E:/Haggen/script/mypaper/current/raw/','alienplanet',1)
#infile=file ('E:/Haggen/script/mypaper/current/raw/alienplanet_0001_1.txt','r')
#buf=infile.read()
#outfile=file ('E:/Haggen/script/mypaper/current/raw/alienplanet_0001_2.txt','w')
#extract_items(buf,outfile,None)