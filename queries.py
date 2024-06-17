import sqlite3


def query_execution(sql: str) -> list:    
    with sqlite3.connect('tasks.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()
    

sql_1 = '''SELECT *
            FROM tasks
            WHERE user_id=1
        '''


sql_2 = '''SELECT tasks.id, tasks.title
            FROM tasks
            WHERE status_id = (SELECT id FROM status WHERE name = 'new')
        '''


sql_3 = '''UPDATE tasks
            SET status_id = (SELECT id FROM status WHERE name = 'in progress')
            WHERE id = 2
        '''


sql_4 = '''SELECT fullname
            FROM users
            WHERE id NOT IN (SELECT user_id FROM tasks)
        '''


sql_5 = '''INSERT INTO tasks(title, description, status_id, user_id)
            VALUES('Task', 'Task description', (SELECT id FROM status WHERE name='new'), 2)
        '''


sql_6 = '''SELECT tasks.id, tasks.title
            From tasks
            WHERE status_id NOT IN (SELECT id FROM status WHERE name='completed')
        '''

sql_7 = '''DELETE FROM tasks WHERE id=16
        '''


sql_8 = '''SELECT u.id, u.fullname, u.email
            FROM users as u
            WHERE u.email LIKE '%example.org%'
        '''


sql_9 = '''UPDATE users
            SET fullname = "Misha Grisha"
            WHERE id = 1
        '''


sql_10 = '''SELECT COUNT(*) AS t_count, s.name AS s_name
            FROM tasks AS t
            LEFT JOIN status AS s ON t.status_id=s.id
            GROUP BY s.name;
        '''


sql_11 = '''SELECT t.title AS title, u.fullname AS user_name, u.email AS u_email
            FROM tasks AS t
            LEFT JOIN users AS u ON t.user_id=u.id
            WHERE u_email LIKE '%example.org%'
        '''


sql_12 = '''SELECT title 
            FROM tasks
            WHERE description IS NULL
        '''


sql_13 = '''SELECT t.title AS title, u.fullname AS user_name, s.name AS status
            FROM tasks AS t
            INNER JOIN users AS u ON t.user_id = u.id
            INNER JOIN status AS s ON t.status_id = s.id
            WHERE s.name = 'in progress';
        '''


sql_14 = '''SELECT u.fullname AS user_name, COUNT(t.id) AS task_count
            FROM users AS u
            LEFT JOIN tasks AS t ON u.id = t.user_id
            GROUP BY u.id, u.fullname
        '''


if __name__ == '__main__':
    print(query_execution(sql_14))
