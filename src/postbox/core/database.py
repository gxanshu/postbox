import os
import sqlite3

from gi.repository import GLib

class Database:
    def __init__(self):
        dir = GLib.get_user_data_dir()
        os.makedirs(dir, exist_ok=True)

        conn = sqlite3.connect(os.path.join(dir, "postbox.db"))
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        print(cursor.fetchone())
        conn.close()


