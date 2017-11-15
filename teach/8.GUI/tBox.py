#label2.py - a label and window program
#andyp 12.11.13

from tkinter import *
bob=Tk()
bob.title('Login Window')
nameWin= Entry (bob)
nameLbl = Label (bob, text='Name')
passWin= Entry (bob)
passLbl = Label (bob, text='Password')
loginButton=Button(text='login')
nameLbl.pack()
nameWin.pack()
passLbl.pack()
passWin.pack()
loginButton.pack()
bob.wm_iconbitmap('geek.ico') # only works with icon files
bob.mainloop()
