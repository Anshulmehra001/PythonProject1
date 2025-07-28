import customtkinter as ctk
import os
import json
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from tkinter import messagebox

VAULT_DIR = "vaults"
SALT_FILE = "vault_salt.bin"

if not os.path.exists(VAULT_DIR):
    os.makedirs(VAULT_DIR)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class Calculator(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("GUI Calculator")
        self.geometry("400x500")
        self.expr = ""
        self._build_ui()

        self.bind("<Key>", self._on_key_press)
        self.bind("<Return>", lambda e: self._on_click('='))
        self.bind("<BackSpace>", lambda e: self._on_click('\u232b'))

    def _build_ui(self):
        about_btn = ctk.CTkButton(self, text="About", width=10, command=self._show_about,
                                  fg_color=("#FFA500", "#FF8C00"), text_color=("#000000", "#FFFFFF"))
        about_btn.grid(row=0, column=3, sticky="ne", padx=10, pady=10)
        self.display = ctk.CTkEntry(self, font=("Consolas", 32), justify="right")
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

        buttons = [
            ['7','8','9','/'],
            ['4','5','6','*'],
            ['1','2','3','-'],
            ['0','.','=','+'],
            ['C','±','%','⌫']
        ]

        for r, row in enumerate(buttons, start=1):
            for c, char in enumerate(row):
                btn = ctk.CTkButton(self, text=char, font=("Arial", 20),
                                    fg_color=("#FFA500", "#FF8C00"),
                                    hover_color=("#FFB733", "#FFA733"),
                                    text_color=("#000000", "#FFFFFF"),
                                    command=lambda ch=char: self._on_click(ch))
                btn.grid(row=r, column=c, sticky="nsew", padx=5, pady=5)

        for i in range(4):
            self.grid_columnconfigure(i, weight=1, uniform="button")
        for i in range(6):
            self.grid_rowconfigure(i, weight=1, uniform="button")

    def _on_click(self, key):
        try:
            if key == 'C':
                self.expr = ""
            elif key == '\u232b':
                self.expr = self.expr[:-1]
            elif key == '\u00b1':
                self.expr = str(-float(self.expr))
            elif key == '%':
                self.expr = str(float(self.expr) / 100)
            elif key == '=':
                expr_clean = self.expr.strip()
                if expr_clean == "12345":
                    self._vault_menu()
                    self.expr = ""
                elif expr_clean == "0000":
                    self._show_about()
                    self.expr = ""
                else:
                    try:
                        self.expr = str(eval(self.expr))
                    except Exception:
                        self.expr = "Error"
            else:
                self.expr += key
        except Exception:
            self.expr = "Error"
        self.display.delete(0, "end")
        self.display.insert("end", self.expr)

    def _show_about(self):
        messagebox.showinfo("About", "This calculator and vault app is created by Aniket Mehra.")

    def _on_key_press(self, event):
        key = event.char
        if key in '0123456789+-*/.%':
            self._on_click(key)
        elif key == '\r' or key == '\n':
            self._on_click('=')
        elif key == '\x08':
            self._on_click('\u232b')

    def _vault_menu(self):
        menu = ctk.CTkToplevel(self)
        menu.title("🔐 Vault Menu")
        menu.geometry("300x350")

        vaults = [f for f in os.listdir(VAULT_DIR) if f.endswith(".json")]

        vault_list = ctk.CTkComboBox(menu, values=vaults, state="readonly")
        vault_list.pack(pady=5)
        vault_list.set("Select vault file")

        def open_selected():
            selected = vault_list.get()
            if selected and selected != "Select vault file":
                menu.destroy()
                self._open_vault(os.path.join(VAULT_DIR, selected))

        ctk.CTkButton(menu, text="Open Selected Vault", command=open_selected).pack(pady=5)
        ctk.CTkButton(menu, text="Create New Vault File", command=lambda: [menu.destroy(), self._new_vault_file()]).pack(pady=5)
        ctk.CTkButton(menu, text="Delete Selected Vault", command=lambda: self._delete_vault_file(vault_list)).pack(pady=5)

    def _open_vault(self, path):
        password = ctk.CTkInputDialog(text="Enter vault password:", title="Vault Access").get_input()
        if not password:
            return

        salt = self._load_salt()
        key = self._derive_key(password.encode(), salt)
        fernet = Fernet(key)

        try:
            with open(path, "rb") as f:
                decrypted_data = fernet.decrypt(f.read())
                notes = json.loads(decrypted_data)
        except Exception:
            messagebox.showerror("Error", "Invalid password or corrupted vault.")
            return

        self._vault_window(notes, fernet, path)

    def _new_vault_file(self):
        name = ctk.CTkInputDialog(text="Enter new vault file name:", title="New Vault").get_input()
        if not name:
            return

        path = os.path.join(VAULT_DIR, name + ".json")
        if os.path.exists(path):
            messagebox.showerror("Error", "File already exists.")
            return

        password = ctk.CTkInputDialog(text="Set vault password:", title="New Vault").get_input()
        if not password:
            return

        salt = self._load_salt()
        key = self._derive_key(password.encode(), salt)
        fernet = Fernet(key)

        notes = {}
        self._vault_window(notes, fernet, path)

    def _delete_vault_file(self, vault_list):
        selected = vault_list.get()
        if selected and selected != "Select vault file":
            path = os.path.join(VAULT_DIR, selected)
            if os.path.exists(path):
                confirm = messagebox.askyesno("Confirm", f"Are you sure you want to delete '{selected}'?")
                if confirm:
                    os.remove(path)
                    messagebox.showinfo("Deleted", f"Deleted {selected}")
                    vault_list.configure(values=[f for f in os.listdir(VAULT_DIR) if f.endswith(".json")])
                    vault_list.set("Select vault file")

    def _vault_window(self, notes, fernet, path):
        vault = ctk.CTkToplevel(self)
        vault.title("🔐 Vault")
        vault.geometry("400x500")

        note_list = ctk.CTkComboBox(vault, values=list(notes.keys()), state="readonly")
        note_list.pack(pady=5)
        note_list.set("Select a note")
        note_list.bind("<<ComboboxSelected>>", lambda e: open_note())

        text_box = ctk.CTkTextbox(vault, width=300, height=200)
        text_box.pack(pady=10)

        def open_note():
            title = note_list.get()
            if title in notes:
                text_box.delete("1.0", "end")
                text_box.insert("1.0", notes[title])

        def save_note():
            title = note_list.get()
            if title and title != "Select a note":
                notes[title] = text_box.get("1.0", "end").strip()
                data = json.dumps(notes).encode()
                encrypted = fernet.encrypt(data)
                with open(path, "wb") as f:
                    f.write(encrypted)
                note_list.configure(values=list(notes.keys()))
                messagebox.showinfo("Saved", f"Note '{title}' saved.")

        def new_note():
            new_title = ctk.CTkInputDialog(text="Enter note title:", title="New Note").get_input()
            if new_title:
                notes[new_title] = ""
                note_list.configure(values=list(notes.keys()))
                note_list.set(new_title)
                text_box.delete("1.0", "end")

        def delete_note():
            title = note_list.get()
            if title in notes:
                confirm = messagebox.askyesno("Confirm", f"Are you sure you want to delete note '{title}'?")
                if confirm:
                    del notes[title]
                    data = json.dumps(notes).encode()
                    encrypted = fernet.encrypt(data)
                    with open(path, "wb") as f:
                        f.write(encrypted)
                    note_list.configure(values=list(notes.keys()))
                    note_list.set("Select a note")
                    text_box.delete("1.0", "end")
                    messagebox.showinfo("Deleted", f"Note '{title}' deleted.")

        ctk.CTkButton(vault, text="Open Note", command=open_note).pack(pady=5)
        ctk.CTkButton(vault, text="New Note", command=new_note).pack(pady=5)
        ctk.CTkButton(vault, text="Save Note", command=save_note).pack(pady=5)
        ctk.CTkButton(vault, text="Delete Note", command=delete_note).pack(pady=5)
        ctk.CTkButton(vault, text="Close Vault", command=vault.destroy).pack(pady=5)

    def _load_salt(self):
        if os.path.exists(SALT_FILE):
            with open(SALT_FILE, "rb") as f:
                return f.read()
        salt = os.urandom(16)
        with open(SALT_FILE, "wb") as f:
            f.write(salt)
        return salt

    def _derive_key(self, password: bytes, salt: bytes):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=390000,
            backend=default_backend()
        )
        return base64.urlsafe_b64encode(kdf.derive(password))

if __name__ == "__main__":
    Calculator().mainloop()
