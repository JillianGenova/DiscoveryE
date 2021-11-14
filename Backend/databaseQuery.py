'''@author AJWuu'''

import sqlite3
import pandas as pd
import google_maps as map

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


def setBusinessCoordinates(name, lantitude, longitude):
    query = "UPDATE business SET lantitude = CAST(? as real), longitude = CAST(? as real) WHERE name = CAST(? as text)"
    data = (lantitude, longitude, name)
    cursor.execute(query, data)
    connection.commit()


def getBusinessName(coordinates):
    query = "SELECT name FROM business WHERE lantitude = ? AND longitude = ?"
    cursor.execute(query, coordinates)
    temp = cursor.fetchone() # fetch() will always return a list
    return temp[0]


def getBusinessAddressFromName(name):
    name = '\"' + name + '\"'
    query = "SELECT formatted_address FROM business WHERE name = " + name
    cursor.execute(query) # cannot directly put name as data, must be (name) <- as a list
    temp = cursor.fetchone()
    return temp[0]


def getBusinessAddressFromCoordinates(coordinates):
    query = "SELECT formatted_address FROM business WHERE lantitude = ? AND longitude = ?"
    cursor.execute(query, coordinates)
    temp = cursor.fetchone()
    return temp[0]


def getBusinessURL(coordinates):
    query = "SELECT url FROM business WHERE lantitude = ? AND longitude = ?"
    cursor.execute(query, coordinates)
    temp = cursor.fetchone()
    return temp[0]


def getBusinessStatus(coordinates):
    query = "SELECT business_status FROM business WHERE lantitude = ? AND longitude = ?"
    cursor.execute(query, coordinates)
    temp = cursor.fetchone()
    return temp[0]


def getBusinessCoordinates(name):
    # output: [lantitude, longitude]
    name = '\"' + name + '\"'
    query = "SELECT lantitude, longitude FROM business WHERE name = " + name
    cursor.execute(query)
    temp = cursor.fetchone()
    return [temp[0],temp[1]]


def getBusinessInfo(coordinates):
    # input: [lantitude, longitude]
    # output: [name, formatted_address, business_status, url, vicinity, category_1, category_2, lantitude, longitude]
    query = "SELECT * FROM business WHERE lantitude = ? AND longitude = ?"
    cursor.execute(query, coordinates)
    temp = cursor.fetchone()
    return temp


def getCategoryNames(category_1):
    if category_1 == 'all':
        query = "SELECT name FROM business"
    else:
        query = "SELECT name FROM business WHERE category_1 = \"" + category_1 + "\""
    cursor.execute(query)
    temp = cursor.fetchall()
    return temp


def getCategoryCoordinates(category_1):
    if category_1 == 'all':
        query = "SELECT lantitude, longitude FROM business"
    else:
        query = "SELECT lantitude, longitude FROM business WHERE category_1 = \"" + category_1 + "\""
    cursor.execute(query)
    temp = cursor.fetchall()
    return temp


def getCategoryInfo(category_1):
    # output: [business[0], business[1], ...]
    if category_1 == 'all':
        query = "SELECT * FROM business"
    else:
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


def insertCoordinates(name, coordinates):
    setBusinessCoordinates(name, coordinates[0], coordinates[1])
    
