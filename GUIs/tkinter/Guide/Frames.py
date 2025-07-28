from tkinter import *
root =Tk()
root.geometry("655x333")
f1 = Frame(root, bg="grey", borderwidth=6, relief="sunken")
f1.pack(side="left", fill="y",pady=122)

f2 = Frame(root, borderwidth=8, bg="grey",relief="sunken")
f2.pack(side="top",fill="x")

l= Label(f1, text="program Tkinter - Pycharm")
l.pack(pady=142)

l= Label(f2, text="welcome to subline text",font="Helvetica 16 bold"
                                                 "")
l.pack()

root.mainloop()
