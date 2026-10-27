import sqlite3

DB_NAME = "campus_booking.db"

def get_connection():
    return sqlite3.connect(DB_NAME)


def create_tables():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        role TEXT,
        campus TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS resources(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        resource_code TEXT UNIQUE,
        resource_name TEXT,
        campus TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS bookings(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        lecturer TEXT,
        resource_code TEXT,
        campus TEXT,
        booking_date TEXT,
        start_time TEXT,
        duration INTEGER
    )
    """)

    conn.commit()
    conn.close()