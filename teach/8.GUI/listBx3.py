#listbx.py simple tkinter list box
#andyp 20.03.13
import tkinter
#import tkinter.messagebox


app=tkinter.Tk()

txtBx=tkinter.Text(app)
lbox=tkinter.Listbox(app)
lbox.insert(1, "Tes")
lbox.insert(2, 'Run')
lbox.insert(3, 'Save')

lbox.pack()
txtBx.pack()
picked=lbox.curselection()
txtBx.insert(1.0,str(picked))
app.mainloop()

