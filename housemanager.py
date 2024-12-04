import sqlite3 as db
from entity.house import House
def getUser(userName):
    house= House()
    house.username=userName
    house.load()
    return house

def insertUser(house, color, president, secretory, candidate):
    oHouse = House()
    oHouse.house = house
    oHouse.color = color
    oHouse.president = president
    oHouse.secretory = secretory
    oHouse.candidate = candidate
    oHouse.save()
