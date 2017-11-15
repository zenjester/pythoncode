#icecream.py simple icream app
#andyp 12.09.12

import tkinter

def sel():
    selection = ' Dude you want  ' + var.get() + ' Ice Cream'
    label.config(text=selection)

app = tkinter.Tk()
var=tkinter.StringVar()

titleLbl=tkinter.Label(app,text='Welcome to the ice cream App').grid(row=0,columnspan=3)
tkinter.Radiobutton(app, text = 'Chocolate',variable=var,value="Choco",command=sel).grid(row=1,sticky=W)
tkinter.Radiobutton(app, text = 'Strawberry',variable=var,value='Straw',command=sel).grid(row=2)
tkinter.Radiobutton(app, text = 'Vanilla',variable=var,value="Van",command=sel).grid(row=3)
label =tkinter.Label(app)
label.grid(row=1,column=1) #TODO use textbox instead of label here
app.mainloop()
