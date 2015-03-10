#This textbox routine is taken from EasyGui
#version : version 0.66 2004-03-05
#author  : Stephen Ferg (steve@ferg.org)
#location: http://www.ferg.org/easygui/index.html
#
#Since the author did not put any license on the code,
#it is OK to put the code under GPL, but of course
#you can download the code at the location above and do otherwise.

rootWindowPosition = "+300+200"
import string

DEFAULT_FONT_FAMILY   = ("MS", "Sans", "Serif")
MONOSPACE_FONT_FAMILY = ("Courier")
DEFAULT_FONT_SIZE     = 10
BIG_FONT_SIZE         = 12
SMALL_FONT_SIZE       =  9
CODEBOX_FONT_SIZE     =  9
TEXTBOX_FONT_SIZE     = DEFAULT_FONT_SIZE

def denyWindowManagerClose():
	""" don't allow WindowManager close
	"""
	x = Tk()
	x.withdraw()
	x.bell()
	x.destroy()

#-------------------------------------------------------------------
# textbox
#-------------------------------------------------------------------
def textbox(message="", title="", text="", codebox=0):
	"""Display some text in a proportional font with line wrapping at word breaks.
	This function is suitable for displaying general written text.

	The text parameter should be a string, or a list or tuple of lines to be
	displayed in the textbox.
	"""

	if message == None: message = ""
	if title == None: title = ""

	global root, __replyButtonText, __widgetTexts, buttonsFrame
	choices = ["0K"]
	__replyButtonText = choices[0]


	root = Tk()

	root.protocol('WM_DELETE_WINDOW', denyWindowManagerClose )

	screen_width = root.winfo_screenwidth()
	screen_height = root.winfo_screenheight()
	root_width = int((screen_width * 0.8))
	root_height = int((screen_height * 0.5))
	root_xpos = int((screen_width * 0.1))
	root_ypos = int((screen_height * 0.05))

	root.title(title)
	root.iconname('Dialog')
	rootWindowPosition = "+0+0"
	root.geometry(rootWindowPosition)
	root.expand=NO
	root.minsize(root_width, root_height)
	rootWindowPosition = "+" + str(root_xpos) + "+" + str(root_ypos)
	root.geometry(rootWindowPosition)


	mainframe = Frame(root)
	mainframe.pack(side=TOP, fill=BOTH, expand=YES)

	# ----  put frames in the window -----------------------------------
	# we pack the textboxFrame first, so it will expand first
	textboxFrame = Frame(mainframe, borderwidth=3)
	textboxFrame.pack(side=BOTTOM , fill=BOTH, expand=YES)

	message_and_buttonsFrame = Frame(mainframe)
	message_and_buttonsFrame.pack(side=TOP, fill=X, expand=NO)

	messageFrame = Frame(message_and_buttonsFrame)
	messageFrame.pack(side=LEFT, fill=X, expand=YES)

	buttonsFrame = Frame(message_and_buttonsFrame)
	buttonsFrame.pack(side=RIGHT, expand=NO)

	# -------------------- put widgets in the frames --------------------

	# put a textbox in the top frame
	if codebox:
		character_width = int((root_width * 0.6) / CODEBOX_FONT_SIZE)
		textbox = Text(textboxFrame,height=25,width=character_width, padx="2m", pady="1m")
		textbox.configure(wrap=NONE)
		textbox.configure(font=(MONOSPACE_FONT_FAMILY, CODEBOX_FONT_SIZE))

	else:
		character_width = int((root_width * 0.6) / SMALL_FONT_SIZE)
		textbox = Text(
			textboxFrame
			, height=25
			,width=character_width
			, padx="2m"
			, pady="1m"
			)
		textbox.configure(wrap=WORD)
		textbox.configure(font=(DEFAULT_FONT_FAMILY,TEXTBOX_FONT_SIZE))


	# add a vertical scrollbar to the frame
	rightScrollbar = Scrollbar(textboxFrame, orient=VERTICAL, command=textbox.yview)
	textbox.configure(yscrollcommand = rightScrollbar.set)

	# add a horizontal scrollbar to the frame
	bottomScrollbar = Scrollbar(textboxFrame, orient=HORIZONTAL, command=textbox.xview)
	textbox.configure(xscrollcommand = bottomScrollbar.set)

	# pack the textbox and the scrollbars.  Note that although we must define
	# the textbox first, we must pack it last, so that the bottomScrollbar will
	# be located properly.

	# Note that we need a bottom scrollbar only for code.
	# Text will be displayed with wordwrap, so we don't need to have a horizontal
	# scroll for it.
	if codebox:
		bottomScrollbar.pack(side=BOTTOM, fill=X)
	rightScrollbar.pack(side=RIGHT, fill=Y)

	textbox.pack(side=LEFT, fill=BOTH, expand=YES)


	# ---------- put a message widget in the message frame-------------------
	messageWidget = Message(messageFrame, anchor=NW, text=message, width=int(root_width * 0.9))
	messageWidget.configure(font=(DEFAULT_FONT_FAMILY,DEFAULT_FONT_SIZE))
	messageWidget.pack(side=LEFT, expand=YES, fill=BOTH, padx='1m', pady='1m')

	# put the buttons in the buttonsFrame
	okButton = Button(buttonsFrame, takefocus=YES, text="OK", height=1, width=6)
	okButton.pack(expand=NO, side=TOP,  padx='2m', pady='1m', ipady="1m", ipadx="2m")
	okButton.bind("<Return>", __textboxOK)
	okButton.bind("<Button-1>",__textboxOK)


	# ----------------- the action begins ----------------------------------------
	try:
		# load the text into the textbox
		if type(text) == type("abc"): pass
		else:
			try:
				text = "".join(text)  # convert a list or a tuple to a string
			except:
				msgbox("Exception when trying to convert "+ str(type(text)) + " to text in textbox")
				sys.exit(16)
		textbox.insert(END,text, "normal")

		# disable the textbox, so the text cannot be edited
		textbox.configure(state=DISABLED)
	except:
		msgbox("Exception when trying to load the textbox.")
		sys.exit(16)

	try:
		okButton.focus_force()
	except:
		msgbox("Exception when trying to put focus on okButton.")
		sys.exit(16)

	root.mainloop()
	root.destroy()
	return __replyButtonText

def __textboxOK(event):
	global root

	root.quit()

