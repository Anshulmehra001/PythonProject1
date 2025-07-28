from tkinter import *
#from PIL import Image, ImageTk # pillow Package for jpg
root = Tk()

 # width x height
root.geometry("364x364")

# w,h
root.minsize(200,200)

#w,h
root.maxsize(1200,900)

#Displaying image
#photo = PhotoImage(file="1.png") # for png
'''#for jpg images
image = Image.open("ghost.jpg")
photo = ImageTk.PhotoImage(image)
'''
root1= Label(image=photo)
root1.pack()



root.mainloop()



