import sqlite3 as db
from entity.voter import Voter


def initializeDatabase():
    sql = "CREATE TABLE IF NOT EXISTS voter(iitNumber TEXT PRIMARY KEY, age INT, district TEXT)"
    con = db.connect("database\\voter.db")
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    cur.close()
    con.close()

def insertUser(iitNumber,age,district):
    oVoter = Voter()
    oVoter.iitNumber = iitNumber
    oVoter.age = age
    oVoter.save()

def removeUser(iitNumber):
    oVoter = Voter()
    oVoter.iitNumber = iitNumber
    oVoter.delete()

def updateUser(iitNumber, age,district):
    oVoter = Voter()
    oVoter.iitNumber = iitNumber
    oVoter.age = age
    oVoter.district = district
    oVoter.update()

def getUser(iitNumber):
    oVoter = Voter()
    oVoter.iitNumber = iitNumber
    oVoter.load()
    return oVoter

def getAllUsers():
    oVoters = []
    sql = "SELECT userName, passWord FROM user"
    con = db.connect("database\\voter.db")
    cur = con.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    for row in rows:
        oVoter = Voter()
        oVoter.iitNumber = row[0]
        oVoter.age = row[1]
        oVoter.district = row[2]
        oVoters.append(oVoter)
    return oVoters

def printUserList(oVoters):
    for oVoter in oVoters:
        print(oVoter.iitNumber, oVoter.age, oVoter.district)

def menu():
    x = 0;
    while (x != 9):
        print("1. Show all voters\n"
              "2. Add new voter\n"
              "3. Remove voter\n"
              "4. Update voter\n"
              "9. Exit")
        x = int(input("Enter your choice: "))
        match x:
            case 1:
                oList = getAllUsers()
                printUserList(oList)
            case 2:
                iitNumber = input("Enter your IIT Number: ")
                age = input(int("Enter your age: "))
                district = input("Enter your district: ")
                insertUser(iitNumber, age, district)
                print("Voter added successfully")
            case 3:
                iitNumber = input("Enter your IIT Number: ")
                removeUser(iitNumber)
                print("Voter removed successfully")
            case 4:
                iitNumber = input("Enter your IIT Number: ")
                age = input(int("Enter your age: "))
                district = input("Enter your district: ")
                updateUser(iitNumber, age, district)
                print("voter updated successfully")

#main for this module
initializeDatabase()
menu()