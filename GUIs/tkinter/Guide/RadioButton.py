from tkinter import *
import tkinter.messagebox as tmsg


root = Tk()
root.geometry('544x233')
root.title("radiobutton")

def Enter():
    tmsg.showinfo("Received!", f"We have received your answer {var.get()}. Thanks")
# var = IntVar()
var = StringVar()
var.set("Radio")
# var.set(1)
Label(root, text= "Enter the answer",font='lucida 19 bold', justify=LEFT, padx=14).pack()
radio = Radiobutton(root, text="A", padx=14, variable=var, value="A").pack(anchor='w')
radio = Radiobutton(root, text="B", padx=14, variable=var, value="B").pack(anchor='w')
radio = Radiobutton(root, text="C", padx=14, variable=var, value="C").pack(anchor='w')
radio = Radiobutton(root, text="D", padx=14, variable=var, value="D").pack(anchor='w')

Button(text='Enter now', command=Enter).pack()

root.mainloop()