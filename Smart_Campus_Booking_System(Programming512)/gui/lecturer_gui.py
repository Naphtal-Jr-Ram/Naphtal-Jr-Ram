from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

from booking_rules import rules

DB = "campus_booking.db"


class LecturerDashboard:

    def __init__(self, root, username, campus):

        self.root = root
        self.username = username
        self.campus = campus

        self.root.title("Lecturer Dashboard")
        self.root.geometry("1000x650")

        Label(
            self.root,
            text=f"Lecturer Dashboard - {self.username}",
            font=("Arial", 16, "bold")
        ).pack(pady=10)

        Label(
            self.root,
            text=f"Current Campus: {self.campus}",
            font=("Arial", 12)
        ).pack()

        self.display_policy()

        button_frame = Frame(self.root)
        button_frame.pack(pady=10)

        Button(
            button_frame,
            text="View Resources",
            width=18,
            command=self.view_resources
        ).grid(row=0, column=0, padx=5)

        Button(
            button_frame,
            text="Create Booking",
            width=18,
            command=self.book_resource
        ).grid(row=0, column=1, padx=5)

        Button(
            button_frame,
            text="My Bookings",
            width=18,
            command=self.view_bookings
        ).grid(row=0, column=2, padx=5)

        Button(
            button_frame,
            text="Cancel Booking",
            width=18,
            command=self.cancel_booking
        ).grid(row=0, column=3, padx=5)

        table_frame = Frame(self.root)
        table_frame.pack(fill=BOTH, expand=True, padx=15, pady=15)

        self.tree = ttk.Treeview(
            table_frame,
            show="headings"
        )

        scrollbar = ttk.Scrollbar(
            table_frame,
            orient=VERTICAL,
            command=self.tree.yview
        )

        self.tree.configure(
            yscrollcommand=scrollbar.set
        )

        self.tree.pack(
            side=LEFT,
            fill=BOTH,
            expand=True
        )

        scrollbar.pack(
            side=RIGHT,
            fill=Y
        )

        self.configure_booking_view()

    def display_policy(self):

        policy = ""

        if self.campus == "Johannesburg":
            policy = "Policy: Maximum booking duration is 4 hours."

        elif self.campus == "Pretoria":
            policy = (
                "Policy: Bookings allowed only "
                "between 08:00 and 17:00."
            )

        elif self.campus == "Cape Town":
            policy = "Policy: Maximum booking duration is 2 hours."

        Label(
            self.root,
            text=policy,
            fg="blue"
        ).pack(pady=5)

    def clear_tree(self):

        for item in self.tree.get_children():
            self.tree.delete(item)

    def configure_booking_view(self):

        self.tree["columns"] = (
            "ID",
            "Resource",
            "Date",
            "Time",
            "Duration"
        )

        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(
                col,
                width=150,
                anchor=CENTER
            )

    def configure_resource_view(self):

        self.tree["columns"] = (
            "ID",
            "Code",
            "Name",
            "Campus"
        )

        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(
                col,
                width=180,
                anchor=CENTER
            )

    def view_resources(self):

        self.clear_tree()
        self.configure_resource_view()

        conn = sqlite3.connect(DB)
        cur = conn.cursor()

        cur.execute("""
            SELECT
                id,
                resource_code,
                resource_name,
                campus
            FROM resources
            WHERE campus = ?
        """, (self.campus,))

        resources = cur.fetchall()

        conn.close()

        for row in resources:
            self.tree.insert(
                "",
                END,
                values=row
            )

    def view_bookings(self):

        self.clear_tree()
        self.configure_booking_view()

        conn = sqlite3.connect(DB)
        cur = conn.cursor()

        cur.execute("""
            SELECT
                id,
                resource_code,
                booking_date,
                start_time,
                duration
            FROM bookings
            WHERE lecturer = ?
            ORDER BY booking_date
        """, (self.username,))

        bookings = cur.fetchall()

        conn.close()

        for row in bookings:
            self.tree.insert(
                "",
                END,
                values=row
            )

    def book_resource(self):

        booking_window = Toplevel(self.root)
        booking_window.title("Create Booking")
        booking_window.geometry("400x350")

        Label(
            booking_window,
            text="Resource Code"
        ).pack(pady=5)

        resource_entry = Entry(booking_window)
        resource_entry.pack()

        Label(
            booking_window,
            text="Booking Date (YYYY-MM-DD)"
        ).pack(pady=5)

        date_entry = Entry(booking_window)
        date_entry.pack()

        Label(
            booking_window,
            text="Start Hour (0-23)"
        ).pack(pady=5)

        hour_entry = Entry(booking_window)
        hour_entry.pack()

        Label(
            booking_window,
            text="Duration (Hours)"
        ).pack(pady=5)

        duration_entry = Entry(booking_window)
        duration_entry.pack()

        def save_booking():

            resource = resource_entry.get().strip()
            booking_date = date_entry.get().strip()

            if resource == "" or booking_date == "":

                messagebox.showerror(
                    "Validation Error",
                    "All fields are required."
                )
                return

            try:

                hour = int(hour_entry.get())
                duration = int(duration_entry.get())

            except ValueError:

                messagebox.showerror(
                    "Validation Error",
                    "Hour and Duration must be numbers."
                )
                return

            if duration <= 0:

                messagebox.showerror(
                    "Validation Error",
                    "Duration must be greater than zero."
                )
                return

            if hour < 0 or hour > 23:

                messagebox.showerror(
                    "Validation Error",
                    "Hour must be between 0 and 23."
                )
                return

            rule = rules[self.campus]

            valid, message = rule.validate(
                duration,
                hour
            )

            if not valid:

                messagebox.showerror(
                    "Policy Violation",
                    message
                )
                return

            conn = sqlite3.connect(DB)
            cur = conn.cursor()

            cur.execute("""
                SELECT campus
                FROM resources
                WHERE resource_code = ?
            """, (resource,))

            resource_info = cur.fetchone()

            if resource_info is None:

                messagebox.showerror(
                    "Error",
                    "Resource does not exist."
                )

                conn.close()
                return

            if resource_info[0] != self.campus:

                messagebox.showerror(
                    "Error",
                    "Resource belongs to another campus."
                )

                conn.close()
                return

            cur.execute("""
                SELECT
                    start_time,
                    duration
                FROM bookings
                WHERE resource_code = ?
                AND booking_date = ?
            """, (resource, booking_date))

            existing_bookings = cur.fetchall()

            new_start = hour
            new_end = hour + duration

            for booking in existing_bookings:

                existing_start = int(booking[0])
                existing_end = (
                    existing_start +
                    int(booking[1])
                )

                overlap = (
                    new_start < existing_end
                    and
                    new_end > existing_start
                )

                if overlap:

                    messagebox.showerror(
                        "Conflict",
                        "Overlapping booking detected."
                    )

                    conn.close()
                    return

            start_time = f"{hour:02d}"

            cur.execute("""
                INSERT INTO bookings(
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
                resource,
                self.campus,
                booking_date,
                start_time,
                duration
            ))

            conn.commit()
            conn.close()

            messagebox.showinfo(
                "Success",
                "Booking created successfully."
            )

            booking_window.destroy()
            self.view_bookings()

        Button(
            booking_window,
            text="Save Booking",
            command=save_booking
        ).pack(pady=20)

    def cancel_booking(self):

        selected = self.tree.focus()

        if not selected:

            messagebox.showerror(
                "Error",
                "Select a booking first."
            )
            return

        booking_id = self.tree.item(
            selected
        )["values"][0]

        answer = messagebox.askyesno(
            "Confirm",
            "Cancel selected booking?"
        )

        if not answer:
            return

        conn = sqlite3.connect(DB)
        cur = conn.cursor()

        cur.execute("""
            DELETE FROM bookings
            WHERE id = ?
            AND lecturer = ?
        """,
        (
            booking_id,
            self.username
        ))

        conn.commit()
        conn.close()

        messagebox.showinfo(
            "Success",
            "Booking cancelled."
        )

        self.view_bookings()