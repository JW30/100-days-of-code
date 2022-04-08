import tkinter as tk
from tkinter import messagebox
import string
import secrets
import pyperclip

EMAIL = "someone@example.com"


class MyPassApp(tk.Tk):

    def __init__(self):
        super().__init__()

        # Main Window
        self.title("Password Manager")
        self.rowconfigure(0, weight=1)
        self.rowconfigure(7, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(5, weight=1)
        self.config(padx=50, pady=50)

        # Canvas
        self.canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
        self.logo_img = tk.PhotoImage(file="logo.png")
        self.canvas.create_image(100, 100, image=self.logo_img)
        self.canvas.grid(row=1, column=2)

        # Labels
        self.website_label = tk.Label(text="Website:")
        self.website_label.grid(row=2, column=1)

        self.email_label = tk.Label(text="Email/Username:")
        self.email_label.grid(row=3, column=1)

        self.pw_label = tk.Label(text="Password:")
        self.pw_label.grid(row=4, column=1)

        # Entries
        self.website_entry = tk.Entry()
        self.website_entry.grid(row=2, column=2, columnspan=3, sticky=tk.E + tk.W)
        self.website_entry.focus_set()

        self.email_entry = tk.Entry()
        self.email_entry.insert(0, EMAIL)
        self.email_entry.grid(row=3, column=2, columnspan=3, sticky=tk.E + tk.W)

        self.pw_entry = tk.Entry(width=21, show="*")
        self.pw_entry.grid(row=4, column=2)

        # Buttons
        self.show_hide_btn = tk.Button(text="Show", width=2, height=1, command=self.show_hide_switch)
        self.show_hide_btn.grid(row=4, column=3)

        self.copy_btn = tk.Button(text="Copy", width=2, height=1, command=self.copy_pw)
        self.copy_btn.grid(row=4, column=4)

        self.generate_btn = tk.Button(text="Generate Password", command=self.generate_password)
        self.generate_btn.grid(row=5, column=2, columnspan=3, sticky=tk.E + tk.W)

        self.save_btn = tk.Button(text="Save", command=self.save_password)
        self.save_btn.grid(row=6, column=2, columnspan=3, sticky=tk.E + tk.W)

    # Logic
    def copy_pw(self):
        pw = self.pw_entry.get()
        if pw:
            pyperclip.copy(self.pw_entry.get())
            focus = self.focus_get()
            messagebox.showinfo(title="Copied!", message="Password copied!")
            self.focus_set()
            focus.focus_set()

    def show_hide_switch(self):
        if self.show_hide_btn.cget(key="text") == "Show":
            self.pw_entry.config(show="")
            self.show_hide_btn.config(text="Hide")
        else:
            self.pw_entry.config(show="*")
            self.show_hide_btn.config(text="Show")

    def save_password(self):
        website = self.website_entry.get()
        email = self.email_entry.get()
        pw = self.pw_entry.get()
        if website and email and pw:
            with open("data.txt", "a") as f:
                f.write(f"{website} {email} {pw}\n")
            messagebox.showinfo(title=website, message="Password saved successfully!")
            self.focus_set()
            self.reset_entries()
        else:
            focus = self.focus_get()
            messagebox.showwarning(title="Error", message="Please don't leave any fields empty!")
            self.focus_set()
            focus.focus_set()

    def reset_entries(self):
        self.website_entry.delete(0, tk.END)
        self.website_entry.focus_set()
        self.email_entry.delete(0, tk.END)
        self.email_entry.insert(0, EMAIL)
        self.pw_entry.delete(0, tk.END)

    def generate_password(self):
        alphabet = string.ascii_letters + string.digits + string.punctuation
        while True:
            password = "".join(secrets.choice(alphabet) for _ in range(20))
            at_least_one_upper = any(symbol in string.ascii_uppercase for symbol in password)
            at_least_one_special = any(symbol in string.punctuation for symbol in password)
            if at_least_one_upper and at_least_one_special:
                break
        self.pw_entry.delete(first=0, last=tk.END)
        self.pw_entry.insert(tk.END, password)


if __name__ == "__main__":
    app = MyPassApp()
    app.mainloop()
