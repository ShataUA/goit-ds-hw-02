import sqlite3


def create_db() -> None:
    with open('add_tables.sql', 'r') as fn:
        sql = fn.read()
    with sqlite3.connect('tasks.db') as con:
        cur = con.cursor()
        cur.executescript(sql)


if __name__ == '__main__':
    create_db()
