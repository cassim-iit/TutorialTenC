import sqlite3 as db
def table():
    con = db.connect("database\\ballot.db")
    cur = con.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS ballot(voterId INTEGER PRIMARY KEY,first_pref INTEGER NOT NULL, second_pref INTEGER NULL,third_pref INTEGER NULL)")
    con.commit()

    # row by row
    cur.close()
    con.close()

table()