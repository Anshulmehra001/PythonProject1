from tkinter import *
import tkinter.messagebox as tmsg
root= Tk()
root.geometry("455x233")
root.title("Sliders")

# myslider = Scale(root, from_=0, to=100)
# myslider.pack()
def getnumber():
    print(f"we have credited\t{myslider2.get()}")
    tmsg.showinfo("successful", f"we have credited\t{myslider2.get()}")

Label(root, text="how much do you want?").pack()
myslider2 = Scale(root, from_=0, to=100, orient="horizontal",tickinterval=50)
myslider2.set(50)
myslider2.pack()
Button(root, text="get number", pady=10,command=getnumber).pack()

root.mainloop()