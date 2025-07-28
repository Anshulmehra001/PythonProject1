from tkinter import *
import tkinter.messagebox as tmsg

from scipy.constants import value

root = Tk()
root.geometry("733x566")

root.title("Pycharm")

def myfunc():
    print("etc etc ")


def help():
    print("i'll help you")
    a = tmsg.showinfo("Help","we will help you")
    print(a)

def rate():
    print("rate us")
    tmsg.askquestion("was your experience good", " you used this gui.. was your experience good")
    if value =="Yes":
        msg= "Great,rate us"
    else:
        msg= "Tell us whats wrong"

    tmsg.showinfo("experience", msg)


def yesno():
    ans = tmsg.askretrycancel("no", "never")
    if ans:
        print("no...")

    else:
        print("good")

# A non dropdown menu
# mymenu = Menu(root)
# mymenu.add_command(label="File", command=myfunc)
# mymenu.add_command(label="Exit", command=quit)
# root.config(menu=mymenu)


mainmenu = Menu(root)
# m1 = Menu(mainmenu)
m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="new", command=myfunc)
m1.add_command(label="save", command=myfunc)
m1.add_separator()
m1.add_command(label="modify", command=myfunc)
m1.add_command(label="edit", command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="main", menu=m1)

m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label="cut", command=myfunc)
m2.add_command(label="copy", command=myfunc)
m2.add_separator()
m2.add_command(label="paste", command=myfunc)
m2.add_command(label="edit", command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="file", menu=m2)

m3=Menu(mainmenu, tearoff=0)
m3.add_command(label="Help", command=help)
m3.add_command(label="Rate us", command=rate)
m3.add_command(label="I quit", command=yesno)
mainmenu.add_cascade(label="help",menu=m3)
root.config(menu=mainmenu)





root.mainloop()
