#2button.py producing two buttons and a change the windfows icon
#andyp 12.10.13
from tkinter import *
app=Tk()
app.title('Two buttons yo')
app.geometry('450x100+200+100')
b1=Button(app,text='click me!', width = 10)
b1.pack(side='top')
b2=Button(app,text='push it!', width = 15)
b2.pack(side='top')
#app.wm_iconbitmap('geek.ico') # only works with icon files
app.mainloop()
