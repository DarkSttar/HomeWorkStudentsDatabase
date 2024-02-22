import sqlite3
from contextlib import contextmanager



@contextmanager
def create_connection(database):
    conn = sqlite3.connect(database)
    yield conn
    conn.rollback()
    conn.close()

    
