from database import connect_db
from utils import *
from config import *



def overall_production_analysis():

    conn = connect_db()
    cur = conn.cursor()

    cur.execute("""
    SELECT COUNT(*), SUM(target), SUM(actual)
    FROM production
    """)

    result  = cur.fetchone()
    conn.close()

    return result

    

def shift_wise_analysis():

    conn = connect_db()
    cur = conn.cursor()

    rows=[]
    
    for shift in SHIFTS :        
        cur.execute("""
            SELECT COUNT(*), SUM(target), SUM(actual)
            FROM production
            WHERE shift = ?
            """, (shift,))

        count, target, actual = cur.fetchone()
        rows.append((shift, count, target, actual))

    conn.close()
    return tuple(rows)
    


def downtime_analysis():
    
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("SELECT reason ,COUNT(*) FROM production GROUP BY reason ORDER BY COUNT(*) DESC")
    rows = cur.fetchall()
    
    conn.close()
    return rows
    

