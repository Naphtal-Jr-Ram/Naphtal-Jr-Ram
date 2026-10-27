from tkinter import *
from tkinter import messagebox
import sqlite3

from auth import verify_password
from register_gui import RegisterWindow
from lecturer_gui import LecturerDashboard
from admin_gui import AdminDashboard
from operator_gui import OperatorDashboard

DB = "campus_booking.db"


class LoginWindow:

    def __init__(self, root):

        self.root = root

        root.title("Smart Campus Resource Booking System")
        root.geometry("400x300")

        Label(
            root,
            text="LOGIN",
            font=("Arial", 16, "bold")
        ).pack(pady=15)

        Label(root, text="Username").pack()

        self.username_entry = Entry(root)
        self.username_entry.pack()

        Label(root, text="Password").pack()

        self.password_entry = Entry(
            root,
            show="*"
        )
        self.password_entry.pack()

        Button(
            root,
            text="Login",
            width=15,
            command=self.login
        ).pack(pady=10)

        Button(
            root,
            text="Register Lecturer",
            width=15,
            command=self.open_register
        ).pack()

    def open_register(self):
        RegisterWindow(
            Toplevel(self.root)
        )

    def login(self):

        username = self.username_entry.get().strip()
        password = self.password_entry.get()

        if username == "" or password == "":
            messagebox.showerror(
                "Error",
                "All fields required"
            )
            return

        conn = sqlite3.connect(DB)
        cur = conn.cursor()

        cur.execute("""
            SELECT password, role, campus
            FROM users
            WHERE username=?
        """, (username,))

        result = cur.fetchone()

        conn.close()

        if result is None:

            messagebox.showerror(
                "Login Failed",
                "User not found"
            )
            return

        stored_password, role, campus = result

        if not verify_password(
                password,
                stored_password
        ):

            messagebox.showerror(
                "Login Failed",
                "Incorrect password"
            )
            return

        messagebox.showinfo(
            "Success",
            f"Welcome {username}"
        )

        if role == "Lecturer":

            LecturerDashboard(
                Toplevel(self.root),
                username,
                campus
            )

        elif role == "Admin":

            AdminDashboard(
                Toplevel(self.root),
                username,
                campus
            )

        elif role == "Operator":

            OperatorDashboard(
                Toplevel(self.root),
                username
            )