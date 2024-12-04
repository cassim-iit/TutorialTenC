""""
https://www.sqlitetutorial.net/sqlite-create-table/
"""
import sqlite3 as db
from entity.house import House


def initializeDatabase():
    sql = "CREATE TABLE IF NOT EXISTS house(house TEXT PRIMARY KEY, color TEXT, president TEXT, secretory TEXT, candidate NUMBER)"
    con = db.connect("database\\house.db")
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    cur.close()
    con.close()


def insertHouse(house, color, president, secretory, candidate):
    oHouse = House()
    oHouse.house = house
    oHouse.color = color
    oHouse.president = president
    oHouse.secretory = secretory
    oHouse.candidate = candidate
    oHouse.save()


def updateHouse(house, color, president, secretory, candidate):
    oHouse = House()
    oHouse.house = house
    oHouse.color = color
    oHouse.president = president
    oHouse.secretory = secretory
    oHouse.candidate = candidate
    oHouse.update()


def getHouse(house):
        ohouse = House()
        ohouse.house = house
        ohouse.load()
        return ohouse
    
    
def removeHouse(house):
    oHouse = House()
    oHouse.house = house
    oHouse.delete()
