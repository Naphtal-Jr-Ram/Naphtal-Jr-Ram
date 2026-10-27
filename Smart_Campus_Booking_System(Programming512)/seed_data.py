# seed_data.py

import sqlite3
from auth import hash_password

DB = "campus_booking.db"


def create_default_data():

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    default_users = [

        (
            "operator",
            hash_password("1234"),
            "Operator",
            "All"
        ),

        (
            "admin_jhb",
            hash_password("1234"),
            "Admin",
            "Johannesburg"
        ),

        (
            "admin_pta",
            hash_password("1234"),
            "Admin",
            "Pretoria"
        ),

        (
            "admin_ct",
            hash_password("1234"),
            "Admin",
            "Cape Town"
        )

    ]

    for user in default_users:

        try:

            cur.execute("""
                INSERT INTO users
                (
                    username,
                    password,
                    role,
                    campus
                )
                VALUES (?, ?, ?, ?)
            """, user)

        except sqlite3.IntegrityError:

            # User already exists
            pass

    default_resources = [

        ("LAB_JHB_01", "Computer Lab A", "Johannesburg"),
        ("PROJ_JHB_01", "Projector A", "Johannesburg"),

        ("LAB_PTA_01", "Computer Lab B", "Pretoria"),
        ("PROJ_PTA_01", "Projector B", "Pretoria"),

        ("LAB_CT_01", "Computer Lab C", "Cape Town"),
        ("PROJ_CT_01", "Projector C", "Cape Town")

    ]

    for resource in default_resources:

        try:

            cur.execute("""
                INSERT INTO resources
                (
                    resource_code,
                    resource_name,
                    campus
                )
                VALUES (?, ?, ?)
            """, resource)

        except sqlite3.IntegrityError:

            # Resource already exists
            pass

    conn.commit()
    conn.close()


if __name__ == "__main__":

    create_default_data()

    print("Default users and resources created successfully.")