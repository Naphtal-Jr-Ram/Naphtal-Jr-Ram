from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

DB = "campus_booking.db"


class OperatorDashboard:

    def __init__(self, root, username):

        self.root = root
        self.username = username

        self.root.title("System Operator Dashboard")
        self.root.geometry("1100x700")

        Label(
            self.root,
            text=f"System Operator Dashboard - {username}",
            font=("Arial", 16, "bold")
        ).pack(pady=10)

        Label(
            self.root,
            text="Institution-Wide Access",
            font=("Arial", 12)
        ).pack()

        button_frame = Frame(self.root)
        button_frame.pack(pady=10)

        Button(
            button_frame,
            text="All Bookings",
            width=20,
            command=self.view_all_bookings
        ).grid(row=0, column=0, padx=5)

        Button(
            button_frame,
            text="All Resources",
            width=20,
            command=self.view_all_resources
        ).grid(row=0, column=1, padx=5)

        Button(
            button_frame,
            text="Campus Comparison",
            width=20,
            command=self.campus_comparison
        ).grid(row=0, column=2, padx=5)

        Button(
            button_frame,
            text="Institution Report",
            width=20,
            command=self.institution_report
        ).grid(row=0, column=3, padx=5)

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

    def clear_tree(self):

        for item in self.tree.get_children():
            self.tree.delete(item)

    def configure_booking_table(self):

        self.tree["columns"] = (
            "ID",
            "Lecturer",
            "Resource",
            "Campus",
            "Date",
            "Time",
            "Duration"
        )

        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(
                col,
                width=140,
                anchor=CENTER
            )

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
                width=220,
                anchor=CENTER
            )

    def view_all_bookings(self):

        self.clear_tree()
        self.configure_booking_table()

        conn = sqlite3.connect(DB)
        cur = conn.cursor()

        cur.execute("""
            SELECT
                id,
                lecturer,
                resource_code,
                campus,
                booking_date,
                start_time,
                duration
            FROM bookings
            ORDER BY campus, booking_date
        """)

        rows = cur.fetchall()

        conn.close()

        for row in rows:

            self.tree.insert(
                "",
                END,
                values=row
            )

    def view_all_resources(self):

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
            ORDER BY campus
        """)

        rows = cur.fetchall()

        conn.close()

        for row in rows:

            self.tree.insert(
                "",
                END,
                values=row
            )

    def campus_comparison(self):

        conn = sqlite3.connect(DB)
        cur = conn.cursor()

        cur.execute("""
            SELECT
                campus,
                COUNT(*)
            FROM bookings
            GROUP BY campus
        """)

        results = cur.fetchall()

        conn.close()

        if not results:

            messagebox.showinfo(
                "Campus Comparison",
                "No booking data available."
            )

            return

        report = "BOOKINGS PER CAMPUS\n\n"

        for campus, total in results:

            report += (
                f"{campus}: {total} bookings\n"
            )

        messagebox.showinfo(
            "Campus Comparison",
            report
        )

    def institution_report(self):

        conn = sqlite3.connect(DB)
        cur = conn.cursor()

        cur.execute("""
            SELECT COUNT(*)
            FROM bookings
        """)

        total_bookings = cur.fetchone()[0]

        cur.execute("""
            SELECT COUNT(*)
            FROM resources
        """)

        total_resources = cur.fetchone()[0]

        cur.execute("""
            SELECT AVG(duration)
            FROM bookings
        """)

        average_duration = cur.fetchone()[0]

        cur.execute("""
            SELECT
                resource_code,
                COUNT(*)
            FROM bookings
            GROUP BY resource_code
            ORDER BY COUNT(*) DESC
            LIMIT 1
        """)

        resource_info = cur.fetchone()

        conn.close()

        if resource_info:

            top_resource = resource_info[0]
            usage_count = resource_info[1]

        else:

            top_resource = "None"
            usage_count = 0

        report = (
            "INSTITUTION REPORT\n\n"
            f"Total Bookings: {total_bookings}\n\n"
            f"Total Resources: {total_resources}\n\n"
            f"Average Booking Duration: "
            f"{round(average_duration or 0, 2)} Hours\n\n"
            f"Most Used Resource: {top_resource}\n"
            f"Usage Count: {usage_count}"
        )

        messagebox.showinfo(
            "Institution Report",
            report
        )