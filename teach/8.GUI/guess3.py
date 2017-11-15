#guess3.py tkinterised guess program
#andyp 12.11.13

import tkinter
import random

def guessNums():
    first=int(firstWin.get())
    if first == guess:
        txtBx.insert(1.0,'You Guessed Good')
    else:
        txtBx.insert(1.0,'You Guessed Bad')
    

guess=random.randint(1,10) #random number betwen 1 and 10
bob=tkinter.Tk()
bob.title('guessing box')
firstWin= tkinter.Entry (bob)
firstLbl = tkinter.Label (bob, text='Enter a guess')
guessButton=tkinter.Button(text='guess',command=guessNums)
txtBx=tkinter.Text(bob,height=1,width=20)
firstLbl.pack()
firstWin.pack()
guessButton.pack()
txtBx.pack()
bob.mainloop()
