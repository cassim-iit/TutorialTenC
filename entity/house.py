import sqlite3 as db
from math import trunc

class House:
    def __init__(self, house = "", color = "", president = "", secretory="", candidate=0):
        self.house = house
        self.color = color
        self.president = president
        self.secretory = secretory
        self.candidate = candidate


    def save(self):
        sql = "INSERT INTO house (house, color, president, secretory, candidate) VALUES (?, ?, ?, ?, ?);"
        con = db.connect("database\\login.db")
        cur = con.cursor()
        cur.execute(sql, (self.house, self.color, self.president, self.secretory, self.candidate))
        con.commit()
        cur.close()
        con.close()

    def load(self):
        sql = "SELECT house,color,president,secretory,candidate FROM house WHERE house=?"
        con = db.connect("database\\login.db")
        cur = con.cursor()
        cur.execute(sql, (self.house,))
        row = cur.fetchone()
        cur.close()
        con.close()
        self.house = row[0]
        self.color= row[1]
        self.president=row[2]
        self.secretory=row[3]
        self.candidate=row[4]
        return True

    def delete(self):
        sql = "DELETE FROM user WHERE userName = ?"
        con = db.connect("database\\login.db")
        cur = con.cursor()
        cur.execute(sql, (self.username,))
        con.commit()
        cur.close()
        con.close()
        return True

    def update(self):
        sql = "UPDATE hosue SET house = ? , color = ? , president= ?, secretory=?, candidate=? WHERE house = ?"
        con = db.connect("database\\house.db")
        cur = con.cursor()
        cur.execute(sql, (self.house, self.color, self.president, self.secretory, self.candidate))
        con.commit()
        cur.close()
        con.close()
        return True