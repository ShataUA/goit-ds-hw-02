import sqlite3
import faker
from random import randint, choice


NUMBER_USERS = 5
NUMER_TASKS = 15


def generate_fake_data(number_users, number_tasks) -> tuple:
    fake_users = []
    fake_tasks = []
    fake_data = faker.Faker()
    for _ in range (NUMBER_USERS):
        fake_users.append((fake_data.name(), fake_data.email()))
    for _ in range (NUMER_TASKS):
        fake_tasks.append((
            fake_data.sentence(nb_words=10),
            fake_data.text(max_nb_chars=2000),
            randint(1, 3),
            randint(1, number_users)
        ))
    return fake_users, fake_tasks


def prepare_data(users, tasks) -> tuple:
    for_users = []
    for user in users:
        for_users.append(user)
    for_tasks = []
    for task in tasks:
        for_tasks.append(task)
    return for_users, for_tasks


def insert_data_to_db(users, tasks) -> None:
    with sqlite3.connect('tasks.db') as con:
        cur = con.cursor()
        sql_to_users = '''INSERT INTO users(fullname, email)
                            VALUES (?,?)'''
        cur.executemany(sql_to_users, users)
        sql_to_tasks = '''INSERT INTO tasks(title, description, status_id, user_id)
                            VALUES (?,?,?,?)'''
        cur.executemany(sql_to_tasks, tasks)
        con.commit()


if __name__ == '__main__':
    users, tasks = prepare_data(*generate_fake_data(NUMBER_USERS, NUMER_TASKS))
    insert_data_to_db(users, tasks)
