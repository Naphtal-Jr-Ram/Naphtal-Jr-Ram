from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import sqlite3

from auth import hash_password

DB = "campus_booking.db"


class RegisterWindow:

    def __init__(self, root):

        self.root = root

        root.title("Lecturer Registration")
        root.geometry("400x350")

        Label(
            root,
            text="REGISTER",
            font=("Arial",16,"bold")
        ).pack(pady=15)

        Label(root,text="Username").pack()

        self.username = Entry(root)
        self.username.pack()

        Label(root,text="Password").pack()

        self.password = Entry(
            root,
            show="*"
        )

        self.password.pack()

        Label(root,text="Campus").pack()

        self.campus = ttk.Combobox(
            root,
            values=[
                "Johannesburg",
                "Pretoria",
                "Cape Town"
            ]
        )

        self.campus.pack()

        Button(
            root,
            text="Register",
            command=self.register
        ).pack(pady=20)

    def register(self):

        username = self.username.get().strip()

        password = self.password.get()

        campus = self.campus.get()

        if (
            username == ""
            or password == ""
            or campus == ""
        ):

            messagebox.showerror(
                "Error",
                "All fields required"
            )

            return

        conn = sqlite3.connect(DB)

        cur = conn.cursor()

        try:

            cur.execute("""
                INSERT INTO users(
                    username,
                    password,
                    role,
                    campus
                )
                VALUES(?,?,?,?)
            """,
            (
                username,
                hash_password(password),
                "Lecturer",
                campus
            ))

            conn.commit()

            messagebox.showinfo(
                "Success",
                "Registration completed"
            )

            self.root.destroy()

        except sqlite3.IntegrityError:

            messagebox.showerror(
                "Error",
                "Username already exists"
            )

        conn.close()