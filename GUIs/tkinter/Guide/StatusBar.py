from tkinter import *

def upload():
    statusvar.set("busy..")
    sbar.update()
    import time
    time.sleep(2)
    statusvar.set("ready Now")


root = Tk()
root.geometry("455x233")
root.title("Status Bar")




statusvar = StringVar()
statusvar.set("Ready")
sbar = Label(root, textvariable=statusvar, relief=SUNKEN, anchor="w")
sbar.pack(side=BOTTOM, fill=X)
Button(root, text="Upload", command=upload).pack()

root.mainloop()