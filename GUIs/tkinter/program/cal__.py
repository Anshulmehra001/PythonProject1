import customtkinter as ctk

# Setup appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class Calculator(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("GUI Calculator")
        self.geometry("400x500")
        self.expr = ""
        self._build_ui()

    def _build_ui(self):
        # Display entry
        self.display = ctk.CTkEntry(self, font=("Consolas", 32), justify="right")
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

        # Button layout
        buttons = [
            ['7','8','9','/'],
            ['4','5','6','*'],
            ['1','2','3','-'],
            ['0','.','=','+'],
            ['C','±','%','🌓']
        ]

        for r, row in enumerate(buttons, start=1):
            for c, char in enumerate(row):
                btn = ctk.CTkButton(self, text=char, font=("Arial", 20),
                                    fg_color=("#FFA500", "#FF8C00"),
                                    hover_color=("#FFB733", "#FFA733"),
                                    text_color=("#000000", "#FFFFFF"),
                                    command=lambda ch=char: self._on_click(ch))
                btn.grid(row=r, column=c, sticky="nsew", padx=5, pady=5)

        # Make grid cells uniform so buttons stay square
        for i in range(4):
            self.grid_columnconfigure(i, weight=1, uniform="button")
        for i in range(6):  # includes display row
            self.grid_rowconfigure(i, weight=1, uniform="button")

    def _on_click(self, key):
        try:
            if key == 'C':
                self.expr = ""
            elif key == '±':
                self.expr = str(-float(self.expr))
            elif key == '%':
                self.expr = str(float(self.expr) / 100)
            elif key == '=':
                self.expr = str(eval(self.expr))
            elif key == '🌓':
                mode = "light" if ctk.get_appearance_mode() == "dark" else "dark"
                ctk.set_appearance_mode(mode)
            else:
                self.expr += key
        except Exception:
            self.expr = "Error"
        self.display.delete(0, "end")
        self.display.insert("end", self.expr)

if __name__ == "__main__":
    Calculator().mainloop()
