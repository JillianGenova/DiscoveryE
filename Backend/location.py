'''@author AJWuu'''

from pandas.core import series
import databaseQuery
import pandas as pd
import google_maps as map
import math

api = map.GoogleMaps("AIzaSyCxWIknbp4ZFgl8JbsVmYh-rJ_65cFttv0") # API Credentials
N = 20  # return the top-N closest businesses


def checkCoordinatesExistence(category_1):
    flag = True
    names = databaseQuery.getCategoryNames(category_1)
    listCoordinates = databaseQuery.getCategoryCoordinates(category_1)
    for i in range (0,len(names)):
        coordinates = listCoordinates[i]
        if (coordinates[0] == None or coordinates[0] == ''):
            flag = False
        if flag == False:
            name = names[i][0] # names[i] will return a "list" like (name)
            coordinates = api.extract_lat_long_via_address(databaseQuery.getBusinessAddressFromName(name))
            databaseQuery.insertCoordinates(name, coordinates)
            flag = True


def getBusinessCoordinates(category_1):
    checkCoordinatesExistence(category_1)
    listCoordinates = databaseQuery.getCategoryCoordinates(category_1)
    return listCoordinates


def getDistance(userCoordinates, businessCoordinates):
    return map.distance_between_coordinates(userCoordinates, businessCoordinates)


def sortDistance(listBusiness):
    sorted(listBusiness, key=lambda distance: listBusiness[2])
    return listBusiness


def outputTopN(listBusiness):
    return listBusiness[:N]


def locationFeatureForOneCategory(address, category_1):
    # input: userAddress and businessCategory
    # output: [business0, business1, ..., business19],
    # where business = [name, formatted_address, business_status, url, vicinity, category_1, category_2, lantitude, longitude]
    userCoordinates = api.extract_lat_long_via_address(address)
    listBusinessCoordinates = getBusinessCoordinates(category_1)
    listBusinessDistances = []
    for businessCoordinates in listBusinessCoordinates:
        listBusinessDistances.append(getDistance(userCoordinates, businessCoordinates))
    df = pd.DataFrame(listBusinessCoordinates, columns=['lantitude', 'longitude'])
    series = pd.Series(listBusinessDistances)
    df['distance'] = series.values
    selectedBusiness = outputTopN(sortDistance(df.values.tolist())) # [lantitude, longitude, distance]
    
    selectedBusinessInfo = []
    for business in selectedBusiness:
        selectedBusinessInfo.append(databaseQuery.getBusinessInfo([business[0],business[1]]))
    return selectedBusinessInfo

def locationFeatureDriver(address, categories): 
    # input: userAddress and businessCategories[],
    # where businessCategories = ["clothes", "food", "leisure", "service", "gift&store"] (choose one or multiple from this list)
    # output: [business0, business1, ..., business19],
    # where business = [name, formatted_address, business_status, url, vicinity, category_1, category_2, lantitude, longitude]
    if len(categories) == 1:
        N = 20
        return locationFeatureForOneCategory(address, categories[0])
    else:
        N = math.ceil(20 / len(categories))
        selectedBusinesses = []
        for category in categories:
            selectedBusinesses.append(locationFeatureForOneCategory(address, category))
        return selectedBusinesses
