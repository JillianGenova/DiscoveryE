'''@author AJWuu'''

import sqlite3
from sqlite3.dbapi2 import Connection
import pandas as pd


fullDatabase = 'business'
categories = ['clothes', 'food', 'leisure', 'service', 'store']


def buildSeparateCategoryDatabase():
    # define connection and cursor
    # will create a new db if not already existed
    connection = sqlite3.connect(fullDatabase + '.db')
    # cursor = connection.cursor() #cursor can interact with the database through SQL commands
    # import data from .csv
    pd.read_csv(categories[0] + '.csv').to_sql(fullDatabase,
                                               connection, if_exists='append', index=False)

    for category in categories:
        connection = sqlite3.connect(category + '.db')
        pd.read_csv(category + '.csv').to_sql(category,
                                              connection, if_exists='append', index=False)

    connection.close()


def mergeDatabases(db1, db2):
    con3 = sqlite3.connect(db1)
    con3.execute("ATTACH '" + db2 + "' as db")
    con3.execute("BEGIN")
    for row in con3.execute("SELECT * FROM db.sqlite_master WHERE type='table'"):
        combine = "INSERT INTO " + row[1] + " SELECT * FROM db." + row[1]
        con3.execute(combine)
    combine = "INSERT INTO" + db1 + " SELECT * FROM db"
    con3.execute(combine)
    con3.commit()
    con3.execute("detach database db")


def main():
    buildSeparateCategoryDatabase()
    for i in range (1,len(categories)):
        mergeDatabases(fullDatabase + '.db', categories[i] + '.db')


if __name__ == "__main__":
    main()
