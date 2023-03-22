import sqlite3


class BaseDao:
    def __init__(self) -> None:
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()

    def close_conn(self):
        self.conn.close()
