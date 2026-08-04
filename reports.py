from database import connect_db
from config import *
from datetime import *


def shift_prod(s_date,e_date):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("""
        SELECT shift, SUM(actual)
        FROM production
        WHERE date BETWEEN ? AND ?
        GROUP BY shift;
    """,(s_date,e_date))    
    row = cur.fetchall()
    conn.commit()
    conn.close()
    return row

            
def shift_eff(s_date,e_date):
    conn = connect_db()
    cur = conn.cursor()
    
    cur.execute("""
        SELECT shift, ROUND((SUM(actual) * 100.0) / NULLIF(SUM(target), 0), 2) AS efficiency
        FROM production
        WHERE date BETWEEN ? AND ?
        GROUP BY shift;
    """,(s_date,e_date))    
    row = cur.fetchall()
    conn.close()
    return row


def kpi_cards(s_date,e_date):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        SELECT SUM(actual),SUM(target),SUM(target)-SUM(actual), ROUND((SUM(actual) * 100.0) / NULLIF(SUM(target), 0), 2) AS efficiency
        FROM production
        WHERE date BETWEEN ? AND ?;
    """,(s_date,e_date))   
    row = cur.fetchone()
    conn.close()
    return row


def table(s_date,e_date):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        SELECT id,date,shift,target,actual,target-actual,ROUND((actual * 100.0) / NULLIF(target, 0), 2)
        FROM production
        WHERE date BETWEEN ? AND ?;
    """,(s_date,e_date))   
    row = cur.fetchall()
    conn.close()
    return row


def prod_line(s_date,e_date):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        SELECT date,SUM(actual)
        FROM production
        WHERE date BETWEEN ? AND ?
        GROUP BY date
        ORDER BY date;
    """,(s_date,e_date))   
    row = cur.fetchall()
    conn.close()
    return row
