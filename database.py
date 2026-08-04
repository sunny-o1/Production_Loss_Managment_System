import sqlite3
from config import DATABASE_NAME
import pandas as pd



def connect_db():
    connection = sqlite3.connect(DATABASE_NAME)
    return connection


def create_table():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS production (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            shift TEXT NOT NULL,
            target INTEGER NOT NULL,
            actual INTEGER NOT NULL,
            reason TEXT NOT NULL,
            operator TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def add_record(date,shift,target,actual,reason,operator):
    
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO production (
            date,
            shift,
            target,
            actual,
            reason,
            operator
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        date,
        shift,
        target,
        actual,
        reason,
        operator
    ))


    connection.commit()
    connection.close()





def view_all_records():
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM production order by date")
    rows =cur.fetchall()

    conn.close()
    return rows

   

def search_by_date(s_date):

    conn = connect_db()
    cur = conn.cursor()

    cur.execute(("SELECT * FROM production WHERE date = ? "),(s_date,))
    rows = cur.fetchall()

    conn.close()
    return rows


def search_by_shift(s_shift):

    conn = connect_db()
    cur = conn.cursor()

    cur.execute(("SELECT * FROM production WHERE shift = ? "),(s_shift,))
    rows = cur.fetchall()

    conn.close()
    return rows


def search_by_operator(s_operator):
    
    conn = connect_db()
    cur = conn.cursor()

    cur.execute(("SELECT * FROM production WHERE operator = ? "),(s_operator,))
    rows = cur.fetchall()

    conn.close()
    return rows


