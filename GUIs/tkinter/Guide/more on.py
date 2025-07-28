from tkinter import *

# from pygame.examples.video import backgrounds

root = Tk()
root.geometry('655x444')

# for title
root.title('Title - My GUI')

# for icon
root.wm_iconbitmap("snake-game-625208.ico")

# for background
root.configure(background="grey")

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

print(f"{width}x{height}")
Button(text="close", command=root.destroy).pack()
root.mainloop()