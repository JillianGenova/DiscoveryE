'''@author AJWuu'''

from pandas.core import series
import databaseQuery
import pandas as pd

N = 20  # return the top-20 closest businesses


def checkCoordinatesExistence(category_1):
    flag = True
    listCoordinates = databaseQuery.getCategoryCoordinates(category_1)
    for coordinates in listCoordinates:
        if (coordinates[0] == None or coordinates[0] == ''):
            flag = False
            break
    if flag == False:
        names = databaseQuery.getCategoryNames(category_1)
        for name in names:
            databaseQuery.insertCoordinates(name)


def getBusinessCoordinates(category_1):
    checkCoordinatesExistence(category_1)
    listCoordinates = databaseQuery.getCategoryCoordinates(category_1)
    return listCoordinates


def getDistance(businessCoordinates):
    # TO-DO: call calculateDistance(userCoordinates, businessCoordinates)
    print("TO-DO")


def sortDistance(listBusiness):
    sorted(listBusiness, key=lambda distance: listBusiness[2])
    return listBusiness


def outputTopN(listBusiness):
    return listBusiness[:N]


def locationFeatureDriver(address, category_1):
    # TO-DO: call getUserCoordinates(address)
    
    # output: [business0, business1, ..., business19],
    # where business = [name, formatted_address, business_status, url, vicinity, category_1, category_2, longitude, lantitude]
    listBusinessCoordinates = getBusinessCoordinates(category_1)
    listBusinessDistances = []
    for businessCoordinates in listBusinessCoordinates:
        listBusinessDistances.append(getDistance(businessCoordinates))
    df = pd.DataFrame(listBusinessCoordinates, columns=['longitude', 'lantitude'])
    series = pd.Series(listBusinessDistances)
    df['distance'] = series.values
    selectedBusiness = outputTopN(sortDistance(df.values.tolist())) # [longitude, lantitude, distance]
    
    selectedBusinessInfo = []
    for business in selectedBusiness:
        selectedBusinessInfo.append(databaseQuery.getBusinessInfo([business[0],business[1]]))
    return selectedBusinessInfo
