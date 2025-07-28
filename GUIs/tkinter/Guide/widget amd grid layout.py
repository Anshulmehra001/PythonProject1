
from tkinter import *

def getvals():
    print(uservalue.get())
    print(passvalue.get())
root=Tk()
root.geometry("655x333")

user = Label(root, text="username")
password =Label(root,text="password")
user.grid()
password.grid(row=1)

#variable classes in tkinter
#booleanVar, DoubleVar , IntVar, StrVar

uservalue=StringVar()
passvalue=StringVar()
userentry=Entry(root, textvariable=uservalue)
passentry=Entry(root,textvariable=passvalue)
userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)
Button(text="submit",command=getvals).grid(column=0)

root.mainloop()
