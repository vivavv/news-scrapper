import sqlite3


def db_create_table(conn):
    conn.execute('''CREATE TABLE IF NOT EXISTS ARTICLES 
                    (
                    TITLE          TEXT    NOT NULL,
                    LINK           TEXT    PRIMARY KEY NOT NULL,
                    DESCRIPTION    TEXT    NOT NULL,
                    PAGE_URL       TEXT    NOT NULL,
                    PAGE_NAME      TEXT    NOT NULL);''')


def get_connection():
    conn = sqlite3.connect('test.db')
    return conn


def db_schema():
    conn = get_connection()
    print("Creating database schema")
    db_create_table(conn)
    conn.close()
