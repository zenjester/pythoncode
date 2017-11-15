#gridlay4.py test gridlayout with use of multiple columns and rows
#andyp 13.03.13

import tkinter

app= tkinter.Tk()
tkinter.Label(app,text="one",borderwidth=1).grid(row=0,column=0,columnspan=2, rowspan= 4)
tkinter.Label(app,text="two",borderwidth=1).grid(row=0,column=1,rowspan=4)
tkinter.Label(app,text="three",borderwidth=1).grid(column=0)
tkinter.Label(app,text="four",borderwidth=1).grid(column=1)

app.mainloop()
