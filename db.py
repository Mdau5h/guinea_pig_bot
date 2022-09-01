import sqlite3
from typing import Dict, List


db = sqlite3.connect('diary.db')
cursor = db.cursor()


def insert(table: str, column_values: Dict):
    columns = ', '.join( column_values.keys() )
    values = [tuple(column_values.values())]
    placeholders = ", ".join( "?" * len(column_values.keys()) )
    cursor.executemany(
        f"INSERT INTO {table} "
        f"({columns}) "
        f"VALUES ({placeholders})",
        values)
    db.commit()


def fetchall(table: str, columns: List[str]):
    columns_joined = ", ".join(columns)
    cursor.execute(f"SELECT {columns_joined} FROM {table}")
    result = cursor.fetchall()
    return result


def delete(table: str, row_id: int) -> None:
    row_id = int(row_id)
    cursor.execute(f"DELETE from {table} where id={row_id}")
    db.commit()


def _init_db():
    """Инициализирует БД"""
    with open("create_db.sql", "r") as f:
        sql = f.read()
    cursor.executescript(sql)
    db.commit()


def check_db_exists():
    """Проверяет, инициализирована ли БД, если нет — инициализирует"""
    cursor.execute("SELECT name FROM sqlite_master "
                   "WHERE type='table' AND name='diary'")
    table_exists = cursor.fetchall()
    if table_exists:
        return
    _init_db()


check_db_exists()


# table_name = 'diary'
# message = {
#     'created': f'{datetime.now()}',
#     'message': 'ТЕСТ-ТЕСТ'
# }
# insert(table_name, message)
# rows = fetchall(table_name, ['*'])
# print(rows)
#
#
# for row in rows:
#     delete(table_name, row[0])
#
#
# print(fetchall(table_name, ['*']))
