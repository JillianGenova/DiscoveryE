'''@author AJWuu'''

import sqlite3
import csv
import pandas as pd

#define connection and cursor
connection = sqlite3.connect('business.db') #will create a new db if not already existed
cursor = connection.cursor() #cursor can interact with the database through SQL commands

#import data from .csv
pd.read_csv('yelpFullData.csv').to_sql('business.db', connection, if_exists='append', index=False)
