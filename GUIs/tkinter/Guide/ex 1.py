from tkinter import *
from PIL import ImageTk , Image

def every_100(text):
    final_text =""
    for i in range (0,len(text)):
        final_text+= text[i]
        if i% 100==0 and i!=0:
            final_text += "\n"
    return final_text
root=Tk()
root.title("none")
root.geometry("1000x700")
texts = []
photo = []
for i in range(0,3):
    with open(f"{i+1}.txt") as f:
        text = f.read()
        texts.append(every_100(text))

    image =Image.open(f"{i+1}.jpg")

    # TODO Resize the image
    image = image.resize((200,200),)

    photo.append(ImageTk.PhotoImage(image))

f0 = Frame(root, width=800, height=70)
Label(f0, text="THE COD GHOST", font="lucida 33 bold").pack()
Label(f0, text="2023", font="lucida 13 bold").pack()
f0.pack()


f1 = Frame(root, width=900, height=200, pady=2)
Label(f1, text=texts[0], padx=22, pady=14).pack(side="left")
Label(f1,image=photo[0],anchor="e").pack()
f1.pack(anchor="w")

f2 = Frame(root, width=900, height=200, pady=2, padx=22)
Label(f2, text=texts[1], padx=22, pady=14).pack(side="right")
Label(f2,image=photo[1],anchor="w").pack()
f2.pack(anchor="w")

f3 = Frame(root, width=900, height=200, pady=2)
Label(f3, text=texts[2], padx=22, pady=14).pack(side="left")
Label(f3,image=photo[2],anchor="e").pack()
f3.pack(anchor="w")








root.mainloop()
