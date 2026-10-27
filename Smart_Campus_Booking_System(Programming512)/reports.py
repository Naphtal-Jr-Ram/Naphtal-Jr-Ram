import sqlite3

DB_NAME = "campus_booking.db"

def total_bookings(campus):

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
    SELECT COUNT(*)
    FROM bookings
    WHERE campus=?
    """, (campus,))

    result = cur.fetchone()[0]
    conn.close()

    return result


def average_duration(campus):

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
    SELECT AVG(duration)
    FROM bookings
    WHERE campus=?
    """, (campus,))

    result = cur.fetchone()[0]
    conn.close()

    return round(result or 0, 2)


def most_used_resource(campus):

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
    SELECT resource_code,
           COUNT(*)
    FROM bookings
    WHERE campus=?
    GROUP BY resource_code
    ORDER BY COUNT(*) DESC
    LIMIT 1
    """, (campus,))

    result = cur.fetchone()

    conn.close()

    return result