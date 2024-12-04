import sqlite3 as db

class Candidate:
    def __init__(self, candidate_id = 0,  candidate_name = "", candidate_house=""):
        self.candidate_id = candidate_id
        self.candidate_name = candidate_name
        self.candidate_house = candidate_house

    def save(self):
        sql = "INSERT INTO candidate (candidateID, candidateName, candidateHouse) VALUES (?, ?, ?)"
        con = db.connect("database\\candidate.db")
        cur = con.cursor()
        cur.execute(sql, (self.candidate_id, self.candidate_name,self.candidate_house))
        con.commit()
        cur.close()
        con.close()

    def update(self):
        sql = "UPDATE candidate SET candidate_name = ? WHERE candiate_id = ?"
        con = db.connect("database\\candidate.db")
        cur = con.cursor()
        cur.execute(sql, (self.candidate_name, self.candidate_id))
        con.commit()
        cur.close()
        con.close()
        return True

    def load(self):
        sql = "SELECT candidate_id, candidate_name, candidate_house FROM candidate WHERE candidate_name = 'Cassim'"
        con = db.connect("database\\candidate.db")
        cur = con.cursor()
        cur.execute(sql, (self.candidate_id,self.candidate_name,self.candidate_house))
        row = cur.fetchone()
        cur.close()
        con.close()
        self.candidate_id = row[0]
        self.candidate_name= row[1]
        self.candidate_house=row[2]

        return True

    def delete(self):
        sql = "DELETE FROM candidate WHERE candidate_name = ?"
        con = db.connect("database\\candidate.db")
        cur = con.cursor()
        cur.execute(sql, (self.candidate_name,))
        con.commit()
        cur.close()
        con.close()
        return True