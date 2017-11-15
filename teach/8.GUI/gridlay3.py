#gridlay3.py test gridlayout with use of multiple columns 
#andyp 13.03.13

import tkinter

app= tkinter.Tk()
tkinter.Label(app,text="one",borderwidth=1).grid(row=0,column=0,columnspan=2)
tkinter.Label(app,text="two",borderwidth=1).grid(row=0,column=1)
tkinter.Label(app,text="three",borderwidth=1).grid(row=1,column=0)
tkinter.Label(app,text="four",borderwidth=1).grid(row=1,column=1,rowspan=2)

app.mainloop()
