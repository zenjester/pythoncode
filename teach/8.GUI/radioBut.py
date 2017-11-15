#radioBut.py simple radio buttons
#andyp 12.09.12

import tkinter

def sel():
    selection = ' Dude you want  ' + str(var.get()) + ' Ice Cream'
    label.config(text=selection)

app = tkinter.Tk()
var=tkinter.IntVar()

r1= tkinter.Radiobutton(app, text = 'Chocolate',variable=var,value=1,command=sel,anchor='w')
r2=tkinter.Radiobutton(app, text = 'Strawberry',variable=var,value=2,command=sel)
r3= tkinter.Radiobutton(app, text = 'Vanilla',variable=var,value=3,command=sel)
r1.pack()
r2.pack()
r3.pack()

label=tkinter.Label(app)
label.pack()
app.mainloop()
