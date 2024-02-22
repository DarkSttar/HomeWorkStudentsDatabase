import sqlite3
from create_db import DATABASE
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--query", "-q", type=int, help="QueryNumber")
args = parser.parse_args()
query = args.query
query_dict = {
    1: "./SQL_Scripts/query_1.sql",
    2: "./SQL_Scripts/query_2.sql",
    3: "./SQL_Scripts/query_3.sql",
    4: "./SQL_Scripts/query_4.sql",
    5: "./SQL_Scripts/query_5.sql",
    6: "./SQL_Scripts/query_6.sql",
    7: "./SQL_Scripts/query_7.sql",
    8: "./SQL_Scripts/query_8.sql",
    9: "./SQL_Scripts/query_9.sql",
    10: "./SQL_Scripts/query_10.sql",
}


def execute_query(sql_file) -> list:
    with open(sql_file, "r") as file:
        sql = file.read()
    with sqlite3.connect(DATABASE) as conn:
        cur = conn.cursor()
        cur.execute(sql)
        return cur.fetchall()


result = execute_query(query_dict[query])
for item in result:
    print(item)
