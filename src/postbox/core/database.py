import sqlite3

class Database:
    def __init__(self):
        conn = sqlite3.connect("/home/anshu/postbox.db")
        cursor = conn.cursor()
        print(cursor.execute("SELECT 1"))
        print(cursor.fetchone())
        conn.close()


