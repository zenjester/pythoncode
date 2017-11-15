#donut.py the attempt at the first year problem
#andyp 12.12.13

import tkinter

app=tkinter.Tk()

choiceFrame=tkinter.Frame(app)
labelFrame=tkinter.Frame(app)
specialFrame=tkinter.Frame(app)
appleLabel=tkinter.Label(labelFrame,text='Apple Cinnamon')
appleSpin=tkinter.Spinbox(choiceFrame,from_ = 0, to = 9,width=2)
specialRandom=tkinter.Checkbutton(specialFrame,text='Random Donuts' )

appleLabel.pack(side='top')
appleSpin.pack(side='top')
specialRandom.pack()
tkinter.Label(app,text='Make a choice',bg='white').grid(row=0,column=0,columnspan=2)
tkinter.Label(app,text='Specials Board').grid(row=0,column=2)
labelFrame.grid(row=1,column=0)
choiceFrame.grid(row=1,column=1)
specialFrame.grid(row=1,column=2)
app.mainloop()

#TODO rest of Donuts
#TODO order total box
#TODO running total box