import sqlite3 as db

def initializeDatabase():
    sql = "CREATE TABLE IF NOT EXISTS candidate(candidateID NUMERIC PRIMARY KEY, candidateName TEXT, candidateHouse TEXT)"
    con = db.connect("database\\candidate.db")
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    cur.close()
    con.close()

initializeDatabase()


def update(self):
    sql = "UPDATE candidate SET canditateID = ? WHERE userName = ?"
    con = db.connect("database\\login.db")
    cur = con.cursor()
    cur.execute(sql, (self.candidateID, self.username))
    con.commit()
    cur.close()
    con.close()
    return True