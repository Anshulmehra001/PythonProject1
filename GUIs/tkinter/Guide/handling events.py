from tkinter import *

def function1(event):
    print(f"you clicked\n{event.x},{event.y}")
root=Tk()
root.title("Events in tkinter")
root.geometry("644x334")
widget = Button(root, text='click me')
widget.pack()

widget.bind('<Button-1>', function1)
widget.bind('<Double-1>', quit)

root.mainloop()