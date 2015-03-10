url_base       ='http://mypaper.pchome.com.tw/'
url_css        ='css/'
url_css_list   =['font.css','splitpage.css']
url_board      ='board/index.htm?s_id='
url_var        ='&Page='
url_differ     =1
read_size      =256
socket_timeout =120

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
        if re.compile('\<\/table').search(curline) and flag >0 :
            if flag==1 :
                res=re.compile('\xA6\x57\xA1\x47\s*\n\s+(\S+)\s').search(buf)
                if res:
                    mtch=res.group(1)
                else:
                    mtch=''
                name= 'Name\t'+mtch+'\n'
                res=re.compile('mail\xA1\x47\s\<a\shref=\"mailto:(\S+)\"').search(buf)
                if res:
                    mtch=res.group(1)
                else:
                    mtch=''
                Mail= 'Mail\t'+mtch+'\n'
            else:
                buf=re.compile('\<br\s\/\>').sub('',buf)
                buf=re.compile('\<BR\>',re.I).sub('\n',buf)
    
                pattern='\<!--\xAF\x64\xA8\xA5\s--\>(.+)\<!--\xAF\x64\xA8\xA5\send--\>'
                res=re.compile(pattern,re.S).search(buf)
                if res:
                    mtch=res.group(1)
                else:
                    mtch=''
                mtch=mtch[3:]
                mtch=re.compile('^\s+').sub('',mtch)
                mtch=re.compile('\<FONT\ssize=\"-2\"\scolor=\"\#FFFFFF\">').sub('',mtch)
                mtch=re.compile('\<\/FONT\>\s+$').sub('',mtch)
                msg = 'Msg\n'+mtch+'\n'
    
                pattern='\<!--\xA4\xE9\xB4\xC1\s--\>.+--(.+\d)\s+--.+\<\/div'
                res=re.compile(pattern,re.S).search(buf)
                if res:
                    mtch=res.group(1)
                else:
                    mtch=''
                mtch=mtch[3:]
                mtch=re.compile('^\s+').sub('',mtch)
                mtch=re.compile('\s+').sub(' ',mtch)
                dateofmsg = 'Date\t'+mtch+'\n'
    
                res=re.compile('\<!--homepage\s--\>(.+)\s+<\/a>',re.S).search(buf)
                if res:
                    mtch=res.group(1)
                else:
                    mtch=''
                mtch=mtch[3:]
                mtch=re.compile('^\s+').sub('',mtch)
                mtch=re.compile('\s+').sub(' ',mtch)
                url = 'URL\t'+mtch+'\n'
                respond = 'Respond\n'
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
            flag=0
        if flag >0:
            buf=buf+htmlspecialchars(curline)
        if re.compile('F4FBFF').search(curline):
            flag=1
            buf=''
        if re.compile('\<td class=\"tb2\"\>').search(curline):
            flag=2
            buf=''
        curline=infile.readline()
    outfile.close()
    infile.close()
