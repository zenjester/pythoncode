#add2.py - a label and window program
#andyp 12.11.13

import tkinter

def addNums():
    first=int(firstWin.get())
    second=int(secoWin.get())
    answer=first+second
    txtBx.insert(1.0,str(answer))

#answer=4
bob=tkinter.Tk()
bob.title('adding box')
firstWin= tkinter.Entry (bob)
firstLbl = tkinter.Label (bob, text='Enter first  number')
secoWin= tkinter.Entry (bob)
secoLbl = tkinter.Label (bob, text='Password')
addButton=tkinter.Button(text='add',command=addNums)
txtBx=tkinter.Text(bob,height=1,width=6)
firstLbl.pack()

firstWin.pack()
secoLbl.pack()
secoWin.pack()
addButton.pack()
txtBx.pack()
bob.mainloop()
