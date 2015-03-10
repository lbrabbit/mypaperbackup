import os
import re
import urllib
import socket
from Tkinter import *
import tkFileDialog
import tkMessageBox
from string import replace
execfile('txt_chinese.py')
execfile('textbox.py')
execfile('parameters.py')

big_font=('Courier',20)
norm_font=('Courier',12)
small_font=('Courier',10)

global abort_flag

def setupgetpage (proxy,directory):
    if proxy:
        if not os.getenv("http_proxy"):
            os.environ["http_proxy"]=proxy
    for fname in url_css_list:
        Apps.update()
        if not os.path.exists(directory+fname):
            Apps.lbl_status['text']=txt_backup+' '+fname
            Apps.update()
            try:
                urllib.urlretrieve(url_base+url_css+fname,directory+fname)
            except socket.error:
                tkMessageBox.showwarning(message=txt_error_IO)
                return 1
            except IOError:
                tkMessageBox.showwarning(message=txt_error_out+'\n'+fname)
                return 1
            except TypeError:
                tkMessageBox.showwarning(message=txt_error_proxy)
                return 1
            except:
                tkMessageBox.showwarning(message=txt_error)
                raise
                return 1

def getpage(userid,pageno,directory):
    Apps.lbl_status['text']=txt_backup+' '+txt_no+str(pageno)+txt_page
    Apps.update()
    url = url_base+url_board+userid
    url = url+url_var+str(pageno-url_differ)
    try:
        page=urllib.urlopen(url)
    except socket.error:
        tkMessageBox.showwarning(message=txt_error_IO)
        return 1
    except TypeError:
        tkMessageBox.showwarning(message=txt_error_proxy)
        return 1
    except:
        tkMessageBox.showwarning(message=txt_error)
        raise
        return 1
    buffer=''
    i=0
    try:
        onebit=page.read(read_size)
        while (onebit):
            buffer+=onebit
            Apps.update()
            onebit=page.read(read_size)
        page.close()
    except socket.error:
        tkMessageBox.showwarning(message=txt_error_IO)
        return 1
    except IOError:
        tkMessageBox.showwarning(message=txt_error_IO)
        return 1
    except:
        tkMessageBox.showwarning(message=txt_error)
        raise
        return 1
    Apps.update()
    buffer=replace (buffer,'href="/'+url_css,'href="')
    fname=directory+userid+'_%(#)04d'%{'#':pageno}+'.htm'
    try:
        outfile=file(fname,'w')
        outfile.write(buffer)
        outfile.close()
    except IOError:
        tkMessageBox.showwarning(message=txt_error_out+'\n'+fname)
        return 1
    except:
        tkMessageBox.showwarning(message=txt_error)
        raise
        return 1
    Apps.update()

def htmlspecialchars(instr):
    instr=replace(instr,'&amp;','&')
    instr=replace(instr,'&quot;','"')
    instr=replace(instr,'&lt;','<')
    instr=replace(instr,'&gt;','>')
    return instr

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
                try:
                    if addmark:    
                        outfile.write(addmark+name)
                        outfile.write(addmark+dateofmsg)
                        outfile.write(addmark+Mail)
                        outfile.write(addmark+url)
                        outfile.write(addmark+msg)
                    else:
                        outfile.write(name)
                        outfile.write(dateofmsg)
                        outfile.write(Mail)
                        outfile.write(url)
                        outfile.write(msg)
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

class Application(Frame):
    def FDialogDir(self): 
	if self.ent_path.get():
		fpath=self.ent_path.get()
	else:
		fpath='c:/'
	fpath=tkFileDialog.askdirectory(initialdir=fpath)
	if fpath:
            self.ent_path.delete(0,END)
            self.ent_path.insert(0,fpath)
            self.update()
        self.fixpath()

    def fixpath(self):
        fpath=self.ent_path.get()
        if fpath:
            fpath=replace (fpath,'\\','/')
            if not (fpath[-1]=='/'):
                fpath=fpath+'/'
            self.ent_path.delete(0,END)
            self.ent_path.insert(0,fpath)  
            self.update()      

    def abort_retrieve(self):
        global abort_flag
        abort_flag=1

    def go_validate(self):

        # Validation
        self.fixpath()
        fpath=self.ent_path.get()
        if not os.path.exists(fpath):
            tkMessageBox.showwarning(message=txt_error_fpath)
            return 1

        userid=self.ent_userid.get()
	if not userid:
            tkMessageBox.showwarning(message=txt_error_noid)
            return 1
            
	startpage=self.ent_start.get()
        try:
            startpage=int(startpage)
        except ValueError:
            tkMessageBox.showwarning(message=txt_error_start)
            return 1

	startpage=self.ent_start.get()
        try:
            startpage=int(startpage)
        except ValueError:
            tkMessageBox.showwarning(message=txt_error_start)
            return 1

	endpage=self.ent_end.get()
        try:
            endpage=int(endpage)
        except ValueError:
            tkMessageBox.showwarning(message=txt_error_end)
            return 1

	if startpage > endpage:
            tkMessageBox.showwarning(message=txt_error_bigger)
            return 1

    def go_backup(self):
        global abort_flag
        self.update()
        abort_flag=0

        socket.setdefaulttimeout(socket_timeout)
        if self.go_validate():
            return
        fpath=self.ent_path.get()
        userid=self.ent_userid.get()
	startpage=int(self.ent_start.get())
	endpage=int(self.ent_end.get())

        # Do the Stuff
        self.update() 
        if setupgetpage (self.ent_proxy.get(),fpath) :
            self.lbl_status['text']=txt_break
            self.update() 
            return
        self.update() 
        if abort_flag:
            self.lbl_status['text']=txt_break
            self.update() 
            return

        for pageno in range (startpage,(endpage+1)) :
            self.update() 
            if abort_flag or getpage(userid,pageno,fpath):
                self.ent_start.delete(0,END)
                self.ent_start.insert(0,pageno)  
                self.lbl_status['text']=txt_break
                self.update() 
                return
            self.update() 

        # Completed
        self.lbl_status['text']=txt_complete
        self.update()
  
    def go_txt (self):
        global abort_flag
        self.update()
        abort_flag=0

        if self.go_validate():
            return
        fpath=self.ent_path.get()
        userid=self.ent_userid.get()
	startpage=int(self.ent_start.get())
	endpage=int(self.ent_end.get())
	addmark=self.ent_addmark.get()

        # Do the Stuff
        for pageno in range (startpage,(endpage+1)) :
            self.update()
            if abort_flag or convert(fpath,userid,pageno,addmark):
                self.lbl_status['text']=txt_break
                self.update() 
                return
            self.update() 

        try: 
            outfname=fpath+'%(start)04dto%(end)04d_'%{'start':startpage,'end':endpage}
            outfname=outfname+userid+'.txt'
            outfile= file(outfname,'w')
        except IOError:
            tkMessageBox.showwarning(message=txt_error_out+'\n'+outfname)
            self.lbl_status['text']=txt_break
            self.update() 
            return
        except:
            tkMessageBox.showwarning(message=txt_error)
            raise
            self.lbl_status['text']=txt_break
            self.update() 
            return
        for pageno in range (startpage,(endpage+1)):
            self.lbl_status['text']=txt_create+txt_allin1+txt_no+str(pageno)+txt_page
            self.update() 
            if abort_flag:
                try:
                    outfile.close()
                except:
                    raise
                self.lbl_status['text']=txt_break
                self.update() 
                try:
                    os.remove (outfname)
                except:
                    raise
                return
            try: 
                infname=fpath+userid+'_%(#)04d'%{'#':pageno}+'.txt'
                infile = file(infname,'r')
                buf=infile.read()
            except IOError:
                tkMessageBox.showwarning(message=txt_error_in+'\n'+infname)
                abort_flag=1
            except:
                tkMessageBox.showwarning(message=txt_error)
                raise
                abort_flag=1
            try: 
                outfile.write(buf)
            except IOError:
                tkMessageBox.showwarning(message=txt_error_out+'\n'+outfname)
                abort_flag=1
            except:
                tkMessageBox.showwarning(message=txt_error)
                raise
                abort_flag=1
        outfile.close()

        # Completed
        self.lbl_status['text']=txt_complete
        self.update()

    def showhelp(self):
        textbox('',txt_help,readme_uni)

    def endprogram(self):
        if tkMessageBox.askyesno(message=txt_askquit):
            self.quit ()

    def createWidgets(self):
        self.lbl_title = Label(self,font=big_font)
        self.lbl_title["text"] = txt_backstage
        self.lbl_title.grid(row=0,column=0,columnspan=10,sticky=W)

        self.lbl_proxy = Label(self,font=norm_font)
        self.lbl_proxy["text"] = 'Proxy'
        self.lbl_proxy.grid(row=1,column=0,columnspan=2,sticky=W)

        self.ent_proxy = Entry(self,width=50,font=norm_font)
        proxy=os.getenv('http_proxy')
        if proxy:
            self.ent_proxy.insert(0,proxy)              
        self.ent_proxy.grid(row=1,column=2,columnspan=7,sticky=W)

        self.lbl_path = Label(self,font=norm_font)
        self.lbl_path["text"] = txt_path
        self.lbl_path.grid(row=2,column=0,columnspan=2,sticky=W)

        self.ent_path = Entry(self,width=40,font=norm_font)
#        self.ent_path.bind("<Leave>",self.fixpath)
        self.ent_path.grid(row=2,column=2,columnspan=6,sticky=W)

        self.browse = Button(self,font=small_font)
        self.browse["text"] = ' '+txt_browse+' '
        self.browse["command"] = self.FDialogDir
        self.browse.grid(row=2,column=8,sticky=W)

        self.lbl_userid1 = Label(self,font=norm_font)
        self.lbl_userid1["text"] = txt_userid1
        self.lbl_userid1.grid(row=3,column=0,columnspan=2,sticky=W)

        self.ent_userid = Entry(self,width=20,font=norm_font)
        self.ent_userid.grid(row=3,column=2,columnspan=6,sticky=W)

        self.lbl_userid2 = Label(self,font=norm_font)
        self.lbl_userid2["text"] = txt_userid2
        self.lbl_userid2.grid(row=4,column=0,columnspan=2,sticky=W)

        self.lbl_start = Label(self,font=norm_font)
        self.lbl_start["text"] = txt_start
        self.lbl_start.grid(row=5,column=0,columnspan=2,sticky=W)

        self.ent_start = Entry(self,width=5,font=norm_font)
        self.ent_start.grid(row=5,column=2,columnspan=2,sticky=W)

        self.lbl_end = Label(self,font=norm_font)
        self.lbl_end["text"] = txt_end
        self.lbl_end.grid(row=6,column=0,columnspan=2,sticky=W)

        self.ent_end = Entry(self,width=5,font=norm_font)
        self.ent_end.grid(row=6,column=2,columnspan=2,sticky=W)

        self.lbl_addmark = Label(self,font=norm_font)
        self.lbl_addmark["text"] = txt_mark+txt_tech
        self.lbl_addmark.grid(row=7,column=0,columnspan=2,sticky=W)

        self.ent_addmark = Entry(self,width=5,font=norm_font)
        self.ent_addmark.grid(row=7,column=2,columnspan=2,sticky=W)

        self.lbl_status = Label(self,font=norm_font)
        self.lbl_status.grid(row=8,column=0,columnspan=10,sticky=W)

        self.backup = Button(self,font=small_font)
        self.backup["text"] = ' '+txt_backup+' '
        self.backup["fg"]   = "red"
        self.backup["command"] = self.go_backup
        self.backup.grid(row=9,column=0,sticky=W)

        self.txtfile = Button(self,font=small_font)
        self.txtfile["text"] = ' '+txt_create+txt_txtfile+' '
        self.txtfile["fg"]   = "red"
#        self.txtfile["command"] = self.go_txt
        self.txtfile.grid(row=9,column=1,sticky=W)

        self.stop = Button(self,font=small_font)
        self.stop["text"] = ' '+txt_stop+' '
        self.stop["command"] = self.abort_retrieve
        self.stop.grid(row=9,column=2,sticky=W)

        self.QUIT = Button(self,font=small_font)
        self.QUIT["text"] = ' '+txt_quit+' '
        self.QUIT["command"] = self.endprogram
        self.QUIT.grid(row=9,column=3,sticky=W)

        self.help = Button(self,font=small_font)
        self.help["bitmap"] = 'question'
        self.help["command"] = self.showhelp
        self.help.grid(row=9,column=9,sticky=E)

    def __init__(self, title):
        Frame.__init__(self,takefocus=TRUE)
        self.master.title(title)
        self.pack()
        self.createWidgets()

Apps=Application(txt_backstage)
Apps.mainloop()