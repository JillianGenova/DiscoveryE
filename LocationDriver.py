'''@author AJWuu'''

import sqlite3

connector = sqlite3.connect('business.db')
cursor = connector.cursor()
businessCoordinates = []
distances = []
N = 20 #return the top-20 closest businesses

def getCoordinates():
    cursor.execute('select Latitude, Longitude from business')
    businessCoordinates = cursor.fetchall()
    '''
    #print out the coordinates
    for row in businessCoordinates:
        print(row)
    '''

def getDistance(businessCoordinates):
    print("Use the calculateDistance() with the help of GoogleMap API")
    #calculateDistance()

def sortDistance(distancesSet):
    distancesSet.sort()

def outputTopN(distancesSet):
    return distancesSet[:N]

def main():
    getCoordinates() #get the coordinates of all the businesses in the database
    
    #get the distances between all the businesses and the user input (brute-force method)
    for row in businessCoordinates:
        getDistance(row)
    
    #sort the distances and output the top-N closest
    sortDistance(distances)
    outputTopN(distances)

if __name__ == "__main__":
    main()
