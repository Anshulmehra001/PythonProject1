from tkinter import *
root=Tk()
def getvals():
    print("submitting the form")
    print(f"{name.get(), phone.get(), roll_no.get(), Gender.get(), Student_var.get()}")

    with open("records.txt","a") as f:
        f.write(f"{name.get(), phone.get(), roll_no.get(), Gender.get(), Student_var.get()}\n")


root.geometry("644x344")
Label(root,text="welcome",font="comicsansms 13 bold", pady=15).grid(row=0,column=3)
#text for our form
name=Label(root,text="Name")
phone=Label(root,text="Phone")
roll_no=Label(root,text="Roll no.")
Gender=Label(root,text="Gender")
# pack text
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
roll_no.grid(row=3,column=2)
Gender.grid(row=4,column=2)
#variable for starting entries
name= StringVar()
phone= StringVar()
roll_no= StringVar()
Gender= StringVar()
Student_var= IntVar()
#entring for form
nameentry=Entry(root,textvariable=name)
phoneentry=Entry(root,textvariable=phone)
roll_noentry=Entry(root,textvariable=roll_no)
Genderentry=Entry(root,textvariable=Gender)
# packing
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
roll_noentry.grid(row=3,column=3)
Genderentry.grid(row=4,column=3)
#checkbox
Student=Checkbutton(text="Student?",variable=Student_var)
Student.grid(row=6,column=3)

# button and packing it and assigning it a command
Button(text="submit to",command=getvals).grid(row=7,column=3)
root.mainloop()
