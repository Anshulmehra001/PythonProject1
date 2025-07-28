from tkinter import *
import tkinter.messagebox as tmsg


root = Tk()
root.geometry('544x233')
root.title("Scrollbar")

# for connecting scrollbar to a widget
# 1. widget(vscrollcoommand = scrollbar.set)
# 2. scrollbar.config(command=widget.yview)


scrollbar = Scrollbar(root)
scrollbar.pack(side= RIGHT,fill=Y)
listbox = Listbox(root, yscrollcommand= scrollbar.set)
for i in range(344):
    listbox.insert(END, f"Item {i}")
listbox.pack(fill="both", padx =22)
scrollbar.config(command=listbox.yview)

#For notepad
# text= Text(root, yscrollcommand= scrollbar.set)
# text.pack(fill=BOTH)
# scrollbar.config(command=text.yview)
#
root.mainloop()