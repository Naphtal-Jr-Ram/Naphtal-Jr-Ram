from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

DB = "campus_booking.db"


class AdminDashboard:

    def __init__(self, root, username, campus):

        self.root = root
        self.username = username
        self.campus = campus

        self.root.title("Campus Administrator Dashboard")
        self.root.geometry("1000x650")

        Label(
            self.root,
            text=f"Administrator Dashboard - {username}",
            font=("Arial", 16, "bold")
        ).pack(pady=10)

        Label(
            self.root,
            text=f"Campus: {campus}",
            font=("Arial", 12)
        ).pack()

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
            text="Add Resource",
            width=18,
            command=self.add_resource
        ).grid(row=0, column=1, padx=5)

        Button(
            button_frame,
            text="Update Resource",
            width=18,
            command=self.update_resource
        ).grid(row=0, column=2, padx=5)

        Button(
            button_frame,
            text="Delete Resource",
            width=18,
            command=self.delete_resource
        ).grid(row=0, column=3, padx=5)

        Button(
            button_frame,
            text="View Bookings",
            width=18,
            command=self.view_bookings
        ).grid(row=0, column=4, padx=5)

        Button(
            button_frame,
            text="Campus Report",
            width=18,
            command=self.campus_report
        ).grid(row=0, column=5, padx=5)

        table_frame = Frame(self.root)
        table_frame.pack(
            fill=BOTH,
            expand=True,
            padx=10,
            pady=10
        )

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

        self.view_resources()

    def clear_tree(self):

        for item in self.tree.get_children():
            self.tree.delete(item)

    def configure_resource_table(self):

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
                width=200,
                anchor=CENTER
            )

    def configure_booking_table(self):

        self.tree["columns"] = (
            "ID",
            "Lecturer",
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

    def view_resources(self):

        self.clear_tree()
        self.configure_resource_table()

        conn = sqlite3.connect(DB)
        cur = conn.cursor()

        cur.execute("""
            SELECT
                id,
                resource_code,
                resource_name,
                campus
            FROM resources
            WHERE campus=?
        """, (self.campus,))

        rows = cur.fetchall()

        conn.close()

        for row in rows:
            self.tree.insert(
                "",
                END,
                values=row
            )

    def add_resource(self):

        window = Toplevel(self.root)
        window.title("Add Resource")
        window.geometry("350x250")

        Label(
            window,
            text="Resource Code"
        ).pack(pady=5)

        code_entry = Entry(window)
        code_entry.pack()

        Label(
            window,
            text="Resource Name"
        ).pack(pady=5)

        name_entry = Entry(window)
        name_entry.pack()

        def save():

            code = code_entry.get().strip()
            name = name_entry.get().strip()

            if code == "" or name == "":

                messagebox.showerror(
                    "Validation Error",
                    "All fields required."
                )
                return

            conn = sqlite3.connect(DB)
            cur = conn.cursor()

            try:

                cur.execute("""
                    INSERT INTO resources(
                        resource_code,
                        resource_name,
                        campus
                    )
                    VALUES(?,?,?)
                """,
                (
                    code,
                    name,
                    self.campus
                ))

                conn.commit()

                messagebox.showinfo(
                    "Success",
                    "Resource added."
                )

                window.destroy()
                self.view_resources()

            except sqlite3.IntegrityError:

                messagebox.showerror(
                    "Error",
                    "Resource code already exists."
                )

            conn.close()

        Button(
            window,
            text="Save",
            command=save
        ).pack(pady=15)

    def update_resource(self):

        selected = self.tree.focus()

        if not selected:

            messagebox.showerror(
                "Error",
                "Select a resource first."
            )
            return

        values = self.tree.item(
            selected
        )["values"]

        resource_id = values[0]
        current_name = values[2]

        window = Toplevel(self.root)
        window.title("Update Resource")
        window.geometry("350x200")

        Label(
            window,
            text="New Resource Name"
        ).pack(pady=5)

        name_entry = Entry(window)
        name_entry.insert(0, current_name)
        name_entry.pack()

        def save():

            new_name = name_entry.get().strip()

            if new_name == "":

                messagebox.showerror(
                    "Validation Error",
                    "Name cannot be empty."
                )
                return

            conn = sqlite3.connect(DB)
            cur = conn.cursor()

            cur.execute("""
                UPDATE resources
                SET resource_name=?
                WHERE id=?
            """,
            (
                new_name,
                resource_id
            ))

            conn.commit()
            conn.close()

            messagebox.showinfo(
                "Success",
                "Resource updated."
            )

            window.destroy()
            self.view_resources()

        Button(
            window,
            text="Update",
            command=save
        ).pack(pady=10)

    def delete_resource(self):

        selected = self.tree.focus()

        if not selected:

            messagebox.showerror(
                "Error",
                "Select a resource."
            )
            return

        values = self.tree.item(
            selected
        )["values"]

        resource_id = values[0]

        confirm = messagebox.askyesno(
            "Confirm",
            "Delete selected resource?"
        )

        if not confirm:
            return

        conn = sqlite3.connect(DB)
        cur = conn.cursor()

        cur.execute("""
            DELETE FROM resources
            WHERE id=?
        """, (resource_id,))

        conn.commit()
        conn.close()

        messagebox.showinfo(
            "Success",
            "Resource deleted."
        )

        self.view_resources()

    def view_bookings(self):

        self.clear_tree()
        self.configure_booking_table()

        conn = sqlite3.connect(DB)
        cur = conn.cursor()

        cur.execute("""
            SELECT
                id,
                lecturer,
                resource_code,
                booking_date,
                start_time,
                duration
            FROM bookings
            WHERE campus=?
            ORDER BY booking_date
        """, (self.campus,))

        rows = cur.fetchall()

        conn.close()

        for row in rows:

            self.tree.insert(
                "",
                END,
                values=row
            )

    def campus_report(self):

        conn = sqlite3.connect(DB)
        cur = conn.cursor()

        cur.execute("""
            SELECT COUNT(*)
            FROM bookings
            WHERE campus=?
        """, (self.campus,))

        total_bookings = cur.fetchone()[0]

        cur.execute("""
            SELECT AVG(duration)
            FROM bookings
            WHERE campus=?
        """, (self.campus,))

        average_duration = cur.fetchone()[0]

        cur.execute("""
            SELECT resource_code,
                   COUNT(*)
            FROM bookings
            WHERE campus=?
            GROUP BY resource_code
            ORDER BY COUNT(*) DESC
            LIMIT 1
        """, (self.campus,))

        most_used = cur.fetchone()

        conn.close()

        if most_used:
            resource = most_used[0]
            usage_count = most_used[1]
        else:
            resource = "None"
            usage_count = 0

        report = (
            f"Campus: {self.campus}\n\n"
            f"Total Bookings: {total_bookings}\n\n"
            f"Average Duration: "
            f"{round(average_duration or 0, 2)} Hours\n\n"
            f"Most Used Resource: {resource}\n"
            f"Usage Count: {usage_count}"
        )

        messagebox.showinfo(
            "Campus Report",
            report
        )