from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

from booking_rules import campus_rules

DB = "campus_booking.db"


class LoginWindow:

    def __init__(self, root):

        self.root = root
        root.title("Smart Campus Resource Booking")

        Label(root,text="Username").pack()

        self.username = Entry(root)
        self.username.pack()

        Label(root,text="Password").pack()

        self.password = Entry(root,show="*")
        self.password.pack()

        Button(
            root,
            text="Login",
            command=self.login
        ).pack(pady=10)

    def login(self):

        conn = sqlite3.connect(DB)
        cur = conn.cursor()

        cur.execute("""
        SELECT role,campus
        FROM users
        WHERE username=?
        AND password=?
        """,
        (
            self.username.get(),
            self.password.get()
        ))

        user = cur.fetchone()
        conn.close()

        if user:

            role,campus = user

            messagebox.showinfo(
                "Success",
                f"{role} login successful"
            )

            Dashboard(
                Toplevel(self.root),
                self.username.get(),
                role,
                campus
            )

        else:
            messagebox.showerror(
                "Error",
                "Invalid login"
            )


class Dashboard:

    def __init__(self, root, username, role, campus):

        self.root = root
        self.role = role
        self.username = username
        self.campus = campus

        root.title(role + " Dashboard")

        Label(
            root,
            text=f"Campus: {campus}",
            font=("Arial",14,"bold")
        ).pack()

        if role == "Lecturer":

            Button(
                root,
                text="Book Resource",
                command=self.book_resource
            ).pack()

            Button(
                root,
                text="My Bookings",
                command=self.view_bookings
            ).pack()

        elif role == "Admin":

            Button(
                root,
                text="Manage Resources",
                command=self.manage_resources
            ).pack()

        elif role == "Operator":

            Button(
                root,
                text="System Reports",
                command=self.system_reports
            ).pack()

    def book_resource(self):

        booking = Toplevel(self.root)

        Label(booking,text="Resource Code").grid(row=0,column=0)
        code = Entry(booking)
        code.grid(row=0,column=1)

        Label(booking,text="Date YYYY-MM-DD").grid(row=1,column=0)
        date = Entry(booking)
        date.grid(row=1,column=1)

        Label(booking,text="Start Hour").grid(row=2,column=0)
        hour = Entry(booking)
        hour.grid(row=2,column=1)

        Label(booking,text="Duration").grid(row=3,column=0)
        duration = Entry(booking)
        duration.grid(row=3,column=1)

        def save():

            h = int(hour.get())
            d = int(duration.get())

            rule = campus_rules[self.campus]

            valid,msg = rule.validate(d,h)

            if not valid:
                messagebox.showerror(
                    "Rule Violation",
                    msg
                )
                return

            conn = sqlite3.connect(DB)
            cur = conn.cursor()

            cur.execute("""
            SELECT *
            FROM bookings
            WHERE resource_code=?
            AND booking_date=?
            AND start_time=?
            """,
            (
                code.get(),
                date.get(),
                hour.get()
            ))

            if cur.fetchone():

                messagebox.showerror(
                    "Error",
                    "Resource already booked"
                )

            else:

                cur.execute("""
                INSERT INTO bookings
                (
                lecturer,
                resource_code,
                campus,
                booking_date,
                start_time,
                duration
                )
                VALUES(?,?,?,?,?,?)
                """,
                (
                    self.username,
                    code.get(),
                    self.campus,
                    date.get(),
                    hour.get(),
                    d
                ))

                conn.commit()

                messagebox.showinfo(
                    "Success",
                    "Booking created"
                )

            conn.close()

        Button(
            booking,
            text="Save Booking",
            command=save
        ).grid(row=4,column=1)

    def view_bookings(self):

        conn = sqlite3.connect(DB)
        cur = conn.cursor()

        cur.execute("""
        SELECT *
        FROM bookings
        WHERE lecturer=?
        """,
        (self.username,))

        rows = cur.fetchall()

        output = ""

        for row in rows:
            output += str(row) + "\n"

        conn.close()

        messagebox.showinfo(
            "My Bookings",
            output
        )

    def manage_resources(self):

        resource_window = Toplevel(self.root)

        Label(resource_window,text="Code").grid(row=0,column=0)
        code = Entry(resource_window)
        code.grid(row=0,column=1)

        Label(resource_window,text="Name").grid(row=1,column=0)
        name = Entry(resource_window)
        name.grid(row=1,column=1)

        def add():

            conn = sqlite3.connect(DB)
            cur = conn.cursor()

            try:

                cur.execute("""
                INSERT INTO resources
                (
                resource_code,
                resource_name,
                campus
                )
                VALUES(?,?,?)
                """,
                (
                    code.get(),
                    name.get(),
                    self.campus
                ))

                conn.commit()

                messagebox.showinfo(
                    "Success",
                    "Resource Added"
                )

            except:

                messagebox.showerror(
                    "Error",
                    "Duplicate Resource"
                )

            conn.close()

        Button(
            resource_window,
            text="Add Resource",
            command=add
        ).grid(row=2,column=1)

    def system_reports(self):

        messagebox.showinfo(
            "Reports",
            "Cross-campus reporting area"
        )