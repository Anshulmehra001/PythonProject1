from tkinter import *
root = Tk()

 # width x height
root.geometry("364x364")



# labeling
sgsd = Label(text="this is a GUI Program")
sgsd.pack()
root.title("my GUI")

# Important Label option
''''text - adds the text
bd - background
fg - foreground
font - sets the font
1. font=("comicsansms",19, "bold")
2. font=comicsansms 19 bold
padx - x padding
pady y padding
relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE
'''

title_label= Label(text='''dgasngoeringoeirgeamegeringenigregpermgknaegonrognringrenmar
anrgoirnggonanfoingoirngoiwngowianoneokmfokamwemfow\ngoinwognwokemfowkemmfowenfownfokmfokmweofnweonfowmfokewfmokwenefiawn''' , bg="black", fg="white", padx=200, pady=110, font="comicsansms 19 bold", borderwidth=3,
                   relief=SUNKEN )

# Important packs options
#anchor =nw
# side = top, bottom, left, right #comment
# padx
# pady
#title_label.pack(side="bottom",anchor='sw', fill=X)
title_label.pack(side=LEFT, fill=Y, padx=34,pady=34)
title_label.pack()


root.mainloop()
