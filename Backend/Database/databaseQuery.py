'''@author AJWuu'''

import sqlite3
import pandas as pd

db = 'business.db'
connection = sqlite3.connect('business.db')
cursor = connection.cursor()


def setBusinessAddress(name, formatted_address):
    query = "UPDATE business SET formatted_address = ? WHERE name = ?"
    data = (formatted_address, name)
    cursor.execute(query, data)
    connection.commit()


def setBusinessURL(name, url):
    query = "UPDATE business SET url = ? WHERE name = ?"
    data = (url, name)
    cursor.execute(query, data)
    connection.commit()


def setBusinessStatus(name, business_status):
    query = "UPDATE business SET business_status = ? WHERE name = ?"
    data = (business_status, name)
    cursor.execute(query, data)
    connection.commit()


def setBusinessCategories(name, category_1, category_2):
    query = "UPDATE business SET category_1 = ?, category_2 = ? WHERE name = ?"
    data = (category_1, category_2, name)
    cursor.execute(query, data)
    connection.commit()


def setBusinessCoordinates(name, longitude, lantitude):
    query = "UPDATE business SET longitude = ?, lantitude = ? WHERE name = ?"
    data = (longitude, lantitude, name)
    cursor.execute(query, data)
    connection.commit()


def getBusinessName(coordinates):
    query = "SELECT name FROM business WHERE longitude = ? AND lantitude = ?"
    cursor.execute(query, coordinates)
    temp = cursor.fetchone() # fetch() will always return a list
    return temp[0]
    


def getBusinessAddress(coordinates):
    query = "SELECT formatted_address FROM business WHERE longitude = ? AND lantitude = ?"
    cursor.execute(query, coordinates)
    temp = cursor.fetchone()
    return temp[0]


def getBusinessURL(coordinates):
    query = "SELECT url FROM business WHERE longitude = ? AND lantitude = ?"
    cursor.execute(query, coordinates)
    temp = cursor.fetchone()
    return temp[0]


def getBusinessStatus(coordinates):
    query = "SELECT business_status FROM business WHERE longitude = ? AND lantitude = ?"
    cursor.execute(query, coordinates)
    temp = cursor.fetchone()
    return temp[0]


def getBusinessCoordinates(name, category_1):
    # output: [longitude, lantitude]
    query = "SELECT longitude, lantitude FROM business WHERE name = ? AND category_1 = ?"
    data = [name, category_1]
    cursor.execute(query, data)
    temp = cursor.fetchone()
    return [temp[0],temp[1]]


def getBusinessInfo(coordinates):
    # input: [longitude, lantitude]
    # output: [name, formatted_address, business_status, url, vicinity, category_1, category_2, longitude, lantitude]
    query = "SELECT * FROM business WHERE longitude = ? AND lantitude = ?"
    cursor.execute(query, coordinates)
    temp = cursor.fetchone()
    return temp


def getCategoryInfo(category_1):
    # output: [business[0], business[1], ...]
    query = "SELECT * FROM business WHERE category_1 = \"" + category_1 + "\""
    cursor.execute(query)
    temp = cursor.fetchall()
    return temp


def insertBusiness(name, formatted_address, business_status, url, vicinity, category_1, category_2):
    insert = "INSERT INTO " + db + " (name, formatted_address, business_status, url, vicinity, category_1, category_2) " + "VALUES (" + \
        name + ", " + formatted_address + ", " + business_status + ", " + \
        url + ", " + vicinity + ", " + category_1 + ", " + category_2 + ")"
    cursor.execute(insert)


def deleteBusiness(name, category_1):
    delete = "DELETE FROM " + db + " WHERE name = ? AND category_1 = ?"
    cursor.execute(delete, (name, category_1))


def insertCoordinates(name, category_1):
    coordinates = getBusinessCoordinates(name, category_1)
    if coordinates[0] == None or coordinates[0] == '':
        coordinates = [1,2] #call Casilda's function
        setBusinessCoordinates(name, coordinates[0], coordinates[1])
