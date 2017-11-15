#label1.py - alabel program
#andyp 12.11.13

from tkinter import *
bob=Tk()
bob.title('Labels')
lbl = Label (bob, text='Label', image= 'geek.ico')
lbl.pack()
bob.wm_iconbitmap('geek.ico') # only works with icon files
bob.mainloop()
