import sqlite3
from create_db import DATABASE
import argparse


class ConsoleColors:
    RESET = "\033[0m"
    GREEN = "\033[92m"
    BLUE = "\033[94m"


parser = argparse.ArgumentParser()

parser.add_argument("--query", "-q", type=int, help="QueryNumber")
args = parser.parse_args()
query = args.query
query_dict = {
    1: [
        {"path": "./SQL_Scripts/query_1.sql"},
        {"query_name": "query_1.sql"},
        {"descript": "Виконує Пошук 5 студентів з найкращим середнім балом."},
        {"param": None},
    ],
    2: [
        {"path": "./SQL_Scripts/query_2.sql"},
        {"query_name": "query_2.sql"},
        {
            "descript": "Виконує Пошук студента з найкращим серендім балом по заданому предмету"
        },
        {"param": None},
    ],
    3: [
        {"path": "./SQL_Scripts/query_3.sql"},
        {"query_name": "query_3.sql"},
        {"descript": "Знаходить середній бал у групах з певного предмету"},
        {"param": None},
    ],
    4: [
        {"path": "./SQL_Scripts/query_4.sql"},
        {"query_name": "query_4.sql"},
        {"descript": "Знаходить середній бал по всій таблиці оцінок"},
        {"param": None},
    ],
    5: [
        {"path": "./SQL_Scripts/query_5.sql"},
        {"query_name": "query_5.sql"},
        {"descript": "Знаходить які курси читає певний викладач."},
        {"param": None},
    ],
    6: [
        {"path": "./SQL_Scripts/query_6.sql"},
        {"query_name": "query_6.sql"},
        {"descript": "Знаходить список студентів в певній групі."},
        {"param": None},
    ],
    7: [
        {"path": "./SQL_Scripts/query_7.sql"},
        {"query_name": "query_7.sql"},
        {"descript": "Знаходить оцінки студентів в певній групі з певного предмета."},
        {"param": None},
    ],
    8: [
        {"path": "./SQL_Scripts/query_8.sql"},
        {"query_name": "query_8.sql"},
        {
            "descript": "Знаходить середній бал який певний викладач ставить зі своїх предметів."
        },
        {"param": None},
    ],
    9: [
        {"path": "./SQL_Scripts/query_9.sql"},
        {"query_name": "query_9.sql"},
        {"descript": "Знаходить список курсів які відвідує студент"},
        {"param": None},
    ],
    10: [
        {"path": "./SQL_Scripts/query_10.sql"},
        {"query_name": "query_10.sql"},
        {"descript": "Знаходить предмети які певному студентові читає певний викладач"},
        {"param": None},
    ],
    11: [
        {"path": "./SQL_Scripts/query_11.sql"},
        {"query_name": "query_11.sql"},
        {
            "descript": "Знаходить середній бал який певному студентові ставить певний викладач."
        },
        {"param": None},
    ],
}


def execute_query(param_dict) -> list:
    sql_file = param_dict[0]["path"]
    query_name = param_dict[1]["query_name"]
    descript = param_dict[2]["descript"]
    print(
        ConsoleColors.BLUE
        + "|{:<15}|{:<100}".format("PATH", f"{sql_file}")
        + ConsoleColors.RESET
    )
    print(
        ConsoleColors.BLUE
        + "|{:<15}|{:<100}".format("QUERY NAME", f"{query_name}")
        + ConsoleColors.RESET
    )
    print(
        ConsoleColors.BLUE
        + "|{:<15}|{:<100}".format("DESCRIPTION", f"{descript}")
        + ConsoleColors.RESET
    )
    if query_name == "query_2.sql" or query_name == "query_3.sql":
        param_dict[3]["param"] = (int(input("Input SubjectID (INT): ")),)
    if query_name == "query_5.sql" or query_name == "query_8.sql":
        param_dict[3]["param"] = (int(input("Input ProfessorID (INT): ")),)
    if query_name == "query_6.sql":
        param_dict[3]["param"] = (int(input("Input GroupID (INT): ")),)
    if query_name == "query_7.sql":
        param_dict[3]["param"] = (
            int(input("Input GroupID (INT): ")),
            int(input("Input SubjectID (INT): ")),
        )
    if query_name == "query_9.sql":
        param_dict[3]["param"] = (int(input("Input StudentID (INT): ")),)
    if query_name == "query_10.sql" or query_name == "query_11.sql":
        param_dict[3]["param"] = (
            int(input("Input StudentID (INT): ")),
            int(input("Input ProfessorID (INT): ")),
        )
    param = param_dict[3]["param"]

    with open(sql_file, "r") as file:
        sql = file.read()

    with sqlite3.connect(DATABASE) as conn:
        cur = conn.cursor()
        if param != None:
            cur.execute(sql, param)
        else:
            cur.execute(sql)
        results = cur.fetchall()
        counter = 1
        for result in results:
            print(
                ConsoleColors.GREEN
                + f"Result {counter}: {result}"
                + ConsoleColors.RESET
            )
            counter += 1


if __name__ == "__main__":
    result = execute_query(query_dict[query])
