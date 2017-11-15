#frame2.py some frame work 
#andyp 23.11.12

import tkinter

app=tkinter.Tk()
topframe=tkinter.Frame(app)
topframe.pack(side="top")

botframe=tkinter.Frame(app)
botframe.pack(side="bottom")


leftframe=tkinter.Frame(app)
leftframe.pack(side="left")

tplbl=tkinter.Label(topframe,text = 'label',fg='blue')
tplbl.pack()

but1=tkinter.Button(botframe,text = 'button',fg='red')
but1.pack(side="left")

but2=tkinter.Button(botframe,text = 'button',fg='green')
but2.pack(side="left")


tbox1=tkinter.Text(leftframe)
tbox1.insert(1.0,"Who is top of the championship")
tbox1.pack(side="left")


tbox2=tkinter.Text(leftframe,fg="blue")
tbox2.insert(1.0,"Who is getting relegated from the championship")
tbox2.pack(side="right")

but3=tkinter.Button(botframe,text = 'button',fg='yellow')
but3.pack(side="bottom")
 
app.mainloop()


