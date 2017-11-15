#firstGui.py first test gui
#andyp 12.10.13
from tkinter import *
app=Tk()
app.title('Your Tkinter App')
app.geometry('450x100+200+100')
b1=Button(app,text='click me!', width = 10)
b1.pack(side='left')
app.mainloop()
