# from tkinter import *
#
# def click(event):
#     global scvalue
#     text = event.widget.cget("text")
#     print(text)
#     if text == "=":
#         if scvalue.get().isdigit():
#             value = int(scvalue.get())
#         else:
#             value = eval(screen.get())
#
#         scvalue.set(value)
#         screen.update()
#
#     elif text =="C":
#         scvalue.set("")
#         screen.update()
#     else:
#         scvalue.set(scvalue.get()+text)
#         screen.update()
#
# root = Tk()
# root.geometry("644x700")
# root.title("GUI CALCULATOR")
#
# scvalue = StringVar()
# scvalue.set('')
# screen= Entry(root, textvariable=scvalue, font="lucida 40 bold")
# screen.pack(fill = X , ipadx=8, pady=10, padx=10)
#
# f = Frame(root, bg="grey")
#
# b = Button(f, text="7", padx=28, pady=10,font="lucida 35 bold")
# b.pack(side=LEFT,padx=18, pady=12)
# b.bind("<Button-1>",click)
#
# b = Button(f, text="8", padx=28, pady=10,font="lucida 35 bold")
# b.pack(side=LEFT,padx=18, pady=12)
# b.bind("<Button-1>",click)
#
# b = Button(f, text="9", padx=28, pady=10,font="lucida 35 bold")
# b.pack(side=LEFT,padx=18, pady=12)
# b.bind("<Button-1>",click)
#
# f.pack()
#
# f = Frame(root, bg="grey")
#
# b = Button(f, text="4", padx=28, pady=10,font="lucida 35 bold")
# b.pack(side=LEFT,padx=18, pady=12)
# b.bind("<Button-1>",click)
#
# b = Button(f, text="5", padx=28, pady=10,font="lucida 35 bold")
# b.pack(side=LEFT,padx=18, pady=12)
# b.bind("<Button-1>",click)
#
# b = Button(f, text="6", padx=28, pady=10,font="lucida 35 bold")
# b.pack(side=LEFT,padx=18, pady=12)
# b.bind("<Button-1>",click)
#
# f.pack()
# f = Frame(root, bg="grey")
#
# b = Button(f, text="1", padx=28, pady=10,font="lucida 35 bold")
# b.pack(side=LEFT,padx=18, pady=12)
# b.bind("<Button-1>",click)
#
# b = Button(f, text="2", padx=28, pady=10,font="lucida 35 bold")
# b.pack(side=LEFT,padx=18, pady=12)
# b.bind("<Button-1>",click)
#
# b = Button(f, text="3", padx=28, pady=10,font="lucida 35 bold")
# b.pack(side=LEFT,padx=18, pady=12)
# b.bind("<Button-1>",click)
#
# f.pack()
#
# f = Frame(root, bg="grey")
#
# b = Button(f, text="C", padx=28, pady=10,font="lucida 35 bold")
# b.pack(side=LEFT,padx=18, pady=12)
# b.bind("<Button-1>",click)
#
# b = Button(f, text="0", padx=28, pady=10,font="lucida 35 bold")
# b.pack(side=LEFT,padx=18, pady=12)
# b.bind("<Button-1>",click)
#
# b = Button(f, text="=", padx=28, pady=10,font="lucida 35 bold")
# b.pack(side=LEFT,padx=18, pady=12)
# b.bind("<Button-1>",click)
#
# f.pack()
# f = Frame(root, bg="grey")
#
# b = Button(f, text="-", padx=28, pady=10,font="lucida 35 bold")
# b.pack(side=LEFT,padx=18, pady=12)
# b.bind("<Button-1>",click)
#
# b = Button(f, text="*", padx=28, pady=10,font="lucida 35 bold")
# b.pack(side=LEFT,padx=18, pady=12)
# b.bind("<Button-1>",click)
#
# b = Button(f, text="+", padx=28, pady=10,font="lucida 35 bold")
# b.pack(side=LEFT,padx=18, pady=12)
# b.bind("<Button-1>",click)
#
# f.pack()
#
# # f = Frame(root, bg="grey")
# #
# # b = 10tton(f, text="C", padx=28, pady=18,font="lucida 35 bold")
# # b.pack(side=LEFT,padx=18, pady=12)
# # b.bind("<Button-1>",click)
# #
# # b = Button(f, text="", padx=28, pady=18,font="lucida 35 bold")
# # b.pack(side=LEFT,padx=18, pady=12)
# # b.bind("<Button-1>",click)
# #
# # b = Button(f, text="7", padx=28, pady=18,font="lucida 35 bold")
# # b.pack(side=LEFT,padx=18, pady=12)
# # b.bind("<Button-1>",click)
# #
# # f.pack()
# root.mainloop()



import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("400x500")
        self.resizable(False, False)

        self.display_var = tk.StringVar()
        self._create_display()
        self._create_buttons()

    def _create_display(self):
        entry = tk.Entry(self, textvariable=self.display_var,
                         font=("Arial", 24), bd=5, relief=tk.RIDGE,
                         justify="right")
        entry.grid(row=0, column=0, columnspan=4, sticky="we", padx=10, pady=10)

    def _create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0, 4)  # 'C' spans 4 columns
        ]
        for btn in buttons:
            text = btn[0]
            row = btn[1]
            col = btn[2]
            colspan = btn[3] if len(btn) == 4 else 1

            action = (self._calculate if text == '=' else
                      self._clear if text == 'C' else
                      lambda t=text: self._append(t))
            b = tk.Button(self, text=text, font=("Arial", 18),
                          command=action, width=5, height=2)
            b.grid(row=row, column=col, columnspan=colspan,
                   padx=5, pady=5, sticky="nsew")

        # make columns expand equally
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
        for i in range(1, 6):
            self.grid_rowconfigure(i, weight=1)

    def _append(self, char):
        self.display_var.set(self.display_var.get() + char)

    def _clear(self):
        self.display_var.set("")

    def _calculate(self):
        try:
            result = eval(self.display_var.get())
        except Exception:
            result = "Error"
        self.display_var.set(str(result))

if __name__ == "__main__":
    Calculator().mainloop()
