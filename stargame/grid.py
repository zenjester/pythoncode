import Tkinter
root = Tkinter.Tk(  )
for r in range(10):
    for c in range(10):
        Tkinter.Label(root, text='R%s/C%s'%(r,c),
            borderwidth=1 ).grid(row=r,column=c, ipadx=10,ipady=10)
root.mainloop(  )
