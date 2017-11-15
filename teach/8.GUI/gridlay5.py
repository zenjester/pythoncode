#gridlay5.py test gridlayout with padding
#andyp 13.03.13

import tkinter

app= tkinter.Tk()
tkinter.Label(app,text="one",borderwidth=1,padx=20,pady=20).grid(row=0,column=0)
tkinter.Label(app,text="two",borderwidth=1).grid(row=0,column=1,pady=50)
tkinter.Label(app,text="three",borderwidth=1).grid(row=1,column=0)
tkinter.Label(app,text="four",borderwidth=1).grid(row=1,column=1)
tbox=tkinter.Text(app)
tbox.grid(row=2,column=0)
bob = "Blackburn suck\n" + "Campbell or gamble"
tbox.insert(11.12,bob)
app.mainloop()
