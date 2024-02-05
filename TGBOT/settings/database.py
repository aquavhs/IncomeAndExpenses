import os
import sqlite3

from TGBOT.settings.config import PATH_DATABASE


def createdbx():
    # Check if the database file exists
    if not os.path.exists(PATH_DATABASE):
        # If it doesn't exist, create the file and the user_table
        with sqlite3.connect(PATH_DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE userRegister_table (
                    id INTEGER PRIMARY KEY,
                    userID INTEGER,
                    userFirstName TEXT NOT NULL,
                    userName TEXT NOT NULL,
                    userTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            print(f"Database file '{PATH_DATABASE}' and table 'userRegister_table' created successfully.")
    else:
        print(f"Database file '{PATH_DATABASE}' already exists. Doing nothing.")


def add_user_data(user_id, user_firstName, user_name, user_time):
    # user_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with sqlite3.connect(PATH_DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO userRegister_table (userID, userFirstName, userName, userTime)
            VALUES (?, ?, ?, ?)
        ''', (user_id, user_firstName, user_name, user_time))
        print("User data added successfully.")

def is_user_in_table(user_id):
    with sqlite3.connect(PATH_DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT userID FROM userRegister_table WHERE userID = ?', (user_id,))
        return cursor.fetchone() is not None