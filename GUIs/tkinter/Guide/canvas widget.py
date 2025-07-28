from tkinter import *
root = Tk()
canvas_width = 800
canvas_height = 400
root.geometry(f"{canvas_width}x{canvas_height}")
root.title("my GUI")
can_widget= Canvas(root, width = canvas_width, height= canvas_height)
can_widget.pack()

# the line goes from the point x1,x2 to x2, y2
can_widget.create_line(0, 0, 800, 400, fill="blue")
can_widget.create_line(0, 400, 800, 0, fill="blue")

# top left to bottom right
#can_widget.create_rectangle(3, 4, 700, 300, fill="black")

can_widget.create_text(200, 200, text="python")

can_widget.create_oval(200,250, 300, 350)




root.mainloop()