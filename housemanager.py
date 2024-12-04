from entity.house import House


def insertUser(house, color, president, secretory, candidate):
    oHouse = House()
    oHouse.house = house
    oHouse.color = color
    oHouse.president = president
    oHouse.secretory = secretory
    oHouse.candidate = candidate
    oHouse.save()
