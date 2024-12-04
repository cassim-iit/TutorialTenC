import sqlite3 as db
from math import trunc

class Voter:
    def __init__(self, iitNumber="", age="", district=""):
        self.iitNumber = iitNumber
        self.age = age
        self.district = district

    def save(self):
        sql = "INSERT INTO voter (iitNumber, age,district) VALUES (?, ?, ?)"
        con = db.connect("database\\voter.db")
        cur = con.cursor()
        cur.execute(sql, (self.iitNumber, self.age, self.district))
        con.commit()
        cur.close()
        con.close()

    def load(self):
        sql = "SELECT iitNumber,age,district FROM user WHERE iitNumber = ?"
        con = db.connect("database\\voter.db")
        cur = con.cursor()
        cur.execute(sql, (self.iitNumber,))
        row = cur.fetchone()
        cur.close()
        con.close()
        self.iitNumber = row[0]
        self.age = row[1]
        self.district = row[2]
        return True

    def delete(self):
        sql = "DELETE FROM voter WHERE iitNumber = ?"
        con = db.connect("database\\voter.db")
        cur = con.cursor()
        cur.execute(sql, (self.iitNumber,))
        con.commit()
        cur.close()
        con.close()
        return True

    def update(self):
        sql = "UPDATE voter SET age = ?,district= ? WHERE iitNumber = ?"
        con = db.connect("database\\voter.db")
        cur = con.cursor()
        cur.execute(sql, (self.age, self.district, self.iitNumber))
        con.commit()
        cur.close()
        con.close()
        return True