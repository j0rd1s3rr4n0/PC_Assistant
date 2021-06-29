from tkinter import *
from tkinter import messagebox
top = Tk()
top.resizable(False, False)
top.overrideredirect(True)
top.parent = parent
C = Canvas(top, bg="blue", height=153, width=250)
filename = PhotoImage(file = "imagen.png")
background_label = Label(top, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

C.pack()
top.mainloop()