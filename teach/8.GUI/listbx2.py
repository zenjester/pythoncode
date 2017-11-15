#listbx2.py simple tkinter list box generated from a tuple
#andyp 20.03.13

import tkinter
#import tkinter.messagebox

app=tkinter.Tk()

colors={'1:red','2:green','3:blue'}
lbox=tkinter.Listbox(app)
lbox.insert(10,colors)

lbox.pack()

app.mainloop()

