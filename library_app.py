import sqlite3
import os

def create_table():
    conn = sqlite3.connect('my_library.db')
    cursor = conn.cursor()
     
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS documents(
                   book_id PRIMARY KEY,
                   book_title TEXT NOT NULL,
                   book_author TEXT NOT NULL,
                   book_description TEXT NOT NULL,
                   book_subject TEXT NOT NULL,
                   curriculum TEXT NOT NULL,
                   book_class TEXT NOT NULL)
                
                ''')
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS teachers(
                   t_id PRIMARY KEY,
                   t_name TEXT NOT NULL,
                   t_phone INTEGER,
                   t_email TEXT NOT NULL,
                   t_subject TEXT NOT NULL
                   )
                    ''')
    conn.commit()
    conn.close()
if __name__ == "__main__":
    create_table()
