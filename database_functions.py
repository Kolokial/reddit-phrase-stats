import sqlite3
from venv import create

def setup_database(cursor):
    schema = open("schema.sql").read()
    cursor.executescript(schema)

def create_connection():
    dbfile = 'phrases.db'
    conn = None
    try:
        conn = sqlite3.Connection(dbfile, isolation_level=None)
        cursor = conn.cursor()
        setup_database(cursor)
        return cursor
    except OSError as e:
        print(e)

    return conn

def insert_into_post_read_table(postId):
    conn = create_connection()
    conn.execute('INSERT INTO read_posts (postId) VALUES(?);', [postId])
    conn.close()

def get_posts_read_list():
    conn = create_connection()
    conn.execute('SELECT postId FROM read_posts')
    results = conn.fetchall()
    conn.close()
    return results
