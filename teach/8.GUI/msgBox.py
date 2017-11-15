#button.py producing a centred button
#andyp 12.10.13
import tkinter 
import tkinter.messagebox

app=tkinter.Tk()

def showMsgBx():
	tkinter.messagebox.showinfo('Hello Peeps','muppet')


app.title('Your Tkinter App')
app.geometry('450x100+200+100')

b1=tkinter.Button(app,text='click me!', width = 10,command =showMsgBx)
b1.pack()
app.mainloop()
