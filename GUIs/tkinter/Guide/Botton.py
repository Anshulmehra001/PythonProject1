from tkinter import *
root=Tk()
root.geometry("655x333")
def hello():
    print("hello tkinter buttons")
def name():
    print("name is aniket")
def branch():
    print("CSE")
def roll_no():
    print("7")

frame= Frame(root, borderwidth=6,bg="grey",relief="sunken")
frame.pack(side="left", anchor="nw")

b1= Button(frame, fg="blue",text="print now",command=hello)
b1.pack(side="left",padx=23)
b2= Button(frame, fg="blue",text="name",command=name)
b2.pack(side="left",padx=23)
b3= Button(frame, fg="blue",text="Branch",command=branch)
b3.pack(side="left",padx=23)
b4= Button(frame, fg="blue",text="roll no",command=roll_no)
b4.pack(side="left",padx=23)


root.mainloop()