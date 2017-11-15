#label2.py - a label and window program
#andyp 12.11.13

from tkinter import *
bob=Tk()
bob.title('Login Window')
koan=Text(bob)
koan.insert(INSERT,'Lightning flashes ,\n Sparks shower, \nIn one blink of your eyes, \nYou have missed seeing.')
koan.pack()
bob.wm_iconbitmap('geek.ico') # only works with icon files
bob.mainloop()
