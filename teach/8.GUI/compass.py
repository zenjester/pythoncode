#2button.py producing two buttons and a change the windfows icon
#andyp 12.10.13
from tkinter import *
app=Tk()
app.title('Compass Dude')
app.geometry('200x200+200+200')
b1=Button(app,text='West', width = 10)
b1.pack(side='left')
b2=Button(app,text='East', width = 10)
b2.pack(side='right')
b3=Button(app,text='South', width = 10)
b3.pack(side='bottom')
b4=Button(app,text='North', width = 10)
b4.pack(side='top')
app.wm_iconbitmap('geek.ico') # only works with icon files
app.mainloop()
