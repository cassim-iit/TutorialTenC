import sqlite3 as db

class Candidate:
    def __init__(self, candidate_id = ,  candidate_name = "", candidateHouse=""):
        self.candidate_id = candidate_id
        self.candidate_name = candidate_name
        self.candidateHouse = candidateHouse

    def View(self):
        sql = "SELECT * FROM candidate WHERE candidateName='Cassim'"
        con = db.connect("database\\candidate.db")
        cur = con.cursor()
        cur.execute(sql, (self.candidate_id,self.candidate_name,self.candidateHouse))
        record = cur.fetchone()
        cur.close()
        con.close()
        self.candidate_id= record[0]
        self.candidate_name = record[1]
        self.candidate_name = record[2]

        return True

