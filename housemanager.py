import sqlite3 as db
from entity.house import House
def getUser(userName):
    house= House()
    house.username=userName
    house.load()
    return house

