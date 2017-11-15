#button.py producing a centred button
#andyp 12.10.13
from tkinter import *
app=Tk()
app.title('Default Button')
app.geometry('450x100+200+100')
b1=Button(app,text='click me!', width = 10, height =10)
b1.pack()
app.mainloop()
