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
        sql = "INSERT INTO house (house, color, president, secretory, candidate) VALUES (?, ?)"
        con = db.connect("database\\login.db")
        cur = con.cursor()
        cur.execute(sql, (self.username, self.password))
        con.commit()
        cur.close()
        con.close()

    def load(self):
        sql = "SELECT userName,passWord FROM user WHERE userName = ?"
        con = db.connect("database\\login.db")
        cur = con.cursor()
        cur.execute(sql, (self.username,))
        row = cur.fetchone()
        cur.close()
        con.close()
        self.username = row[0]
        self.password = row[1]
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
        sql = "UPDATE user SET passWord = ? WHERE userName = ?"
        con = db.connect("database\\login.db")
        cur = con.cursor()
        cur.execute(sql, (self.password, self.username))
        con.commit()
        cur.close()
        con.close()
        return True