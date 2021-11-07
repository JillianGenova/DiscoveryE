'''@author AJWuu'''

import sqlite3
import pandas as pd

categories = ['clothes', 'food', 'leisure', 'service', 'store']

for category in categories:
    #define connection and cursor
    connection = sqlite3.connect(category + '.db') #will create a new db if not already existed
    cursor = connection.cursor() #cursor can interact with the database through SQL commands

    #import data from .csv
    pd.read_csv(category + '.csv').to_sql(category, connection, if_exists='append', index=False)
    
    connection.close()
