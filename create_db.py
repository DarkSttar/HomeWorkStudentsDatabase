import sqlite3

DATABASE = "Database/StudentsDB.db"
SQL_SCRIPT_FOR_TABLE_CREATEING = "SQL_Scripts/Create_tables.sql"


def create_db():
    with open(SQL_SCRIPT_FOR_TABLE_CREATEING, "r") as file:
        sql = file.read()

    with sqlite3.connect(DATABASE) as conn:
        cur = conn.cursor()
        cur.executescript(sql)
