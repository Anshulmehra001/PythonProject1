from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import  askopenfilename,asksaveasfilename
import os

def newfile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)


def openfile():
    global file
    file = askopenfilename(defaultextension=".txt",filetypes=[("All Files", "*.*"),('Text Documents',"*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0,END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


def savefile():
    global file
    if file ==None:
        file = asksaveasfilename(initialfile='Untitled.txt',filetypes=[("All Files", "*.*"),('Text Documents',"*.txt")])

        if file =="":
            file = None

        else:
            #save as a new file
            f = open(file, 'w')
            f.write(TextArea.get(1.0,END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")

    else:
        # save as a new file
        f = open(file, 'w')
        f.write(TextArea.get(1.0, END))
        f.close()


def quitapp():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))


def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    showinfo('Notepad', 'Notepad by Aniket Mehra')
    showinfo('Version', '1')


if __name__== '__main__':
    # basic tkinter setup
    root = Tk()
    root.title('Untitled - Notepad')
    # root.wm_iconbitmap('notepad.ico')
    root.geometry("644x600")

    #add text area
    TextArea = Text(root, font='lucida 13')
    file = None
    TextArea.pack(expand=True, fill=BOTH)


    # lets create a menubar

    Menubar = Menu(root)

    #file menu starts
    FileMenu = Menu( Menubar, tearoff=0)

    # open new file
    FileMenu.add_command(label='New', command=newfile)

    # open already existing file
    FileMenu.add_command(label="Open", command=openfile)

    # save the current file

    FileMenu.add_command(label="Save", command=savefile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=quitapp)
    Menubar.add_cascade(label = "File", menu= FileMenu)
    # file menu ends


    # edit menu starts
    EditMenu = Menu(Menubar, tearoff=0)
    # to give a feature of cut, copy and paste
    EditMenu.add_command(label='cut', command=cut)
    EditMenu.add_command(label='copy', command=copy)
    EditMenu.add_command(label='paste', command=paste)

    Menubar.add_cascade(label="Edit", menu= EditMenu)

    # Edit Menu Ends

    # help menu starts
    HelpMenu = Menu(Menubar, tearoff=0)
    HelpMenu.add_command(label= "About Notepad", command=about)
    Menubar.add_cascade(label="Help", menu=HelpMenu)



    root.config(menu=Menubar)

    Scroll = Scrollbar(TextArea)
    Scroll.pack(side= RIGHT, fill="y")
    Scroll.config(command= TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)






    root.mainloop()


























