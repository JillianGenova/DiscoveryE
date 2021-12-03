'''@author AJWuu'''

from pandas.core import series
import databaseQuery
import pandas as pd
import google_maps as map
import math

api = map.GoogleMaps(
    "AIzaSyCxWIknbp4ZFgl8JbsVmYh-rJ_65cFttv0")  # API Credentials
Num = 20  # parameter for N


def checkCoordinatesExistence(category_1):
    flag = True
    names = databaseQuery.getCategoryNames(category_1)
    listCoordinates = databaseQuery.getCategoryCoordinates(category_1)
    for i in range(0, len(names)):
        coordinates = listCoordinates[i]
        if (coordinates[0] == None or coordinates[0] == ''):
            flag = False
        if flag == False:
            name = names[i][0]  # names[i] will return a "list" like (name)
            coordinates = api.extract_lat_long_via_address(
                databaseQuery.getBusinessAddressFromName(name))
            databaseQuery.insertCoordinates(name, coordinates)
            flag = True


def getBusinessCoordinates(category_1):
    checkCoordinatesExistence(category_1)
    listNameAndCoordinates = databaseQuery.getCategoryNameAndCoordinates(
        category_1)
    return listNameAndCoordinates


def getDistance(userCoordinates, businessCoordinates):
    return map.distance_between_coordinates(userCoordinates, businessCoordinates)


def sortDistance(listBusiness):
    # sort the list by the third column (distance)
    return sorted(listBusiness, key=lambda row: row[-1])


def outputTopN(N, listBusiness):
    if len(listBusiness) >= N:
        return listBusiness[:N]
    else:
        return listBusiness


def locationFeatureForOneCategory(N, address, category_1, selectedBusinessInfo):
    # input: userAddress and businessCategory
    # output: [business0, business1, ..., business19],
    # where business = [name, formatted_address, business_status, url, vicinity, category_1, category_2, latitude, longitude]
    userCoordinates = api.extract_lat_long_via_address(address)
    listBusinessNameAndCoordinates = getBusinessCoordinates(category_1)
    listBusinessDistances = []
    for businessNameAndCoordinates in listBusinessNameAndCoordinates:
        listBusinessDistances.append(getDistance(
            userCoordinates, [businessNameAndCoordinates[1], businessNameAndCoordinates[2]]))
    df = pd.DataFrame(listBusinessNameAndCoordinates, columns=['name',
                      'latitude', 'longitude'])
    series = pd.Series(listBusinessDistances)
    df['distance'] = series.values
    # [latitude, longitude, distance]
    selectedBusiness = outputTopN(N, sortDistance(df.values.tolist()))

    for business in selectedBusiness:
        # add distance to businessInfo tuple
        businessData = databaseQuery.getBusinessInfoByNameAndCoordinates(
            business[0], [business[1], business[2]]) + (business[-1],)
        selectedBusinessInfo.append(businessData)

    return selectedBusinessInfo


def filterConverter(categories):
    # Front End uses: "food", "clothes", "gift", "services", "other"
    # Back End uses: "food", "clothes", "gift&store", "service", "leisure"
    newCategories = []
    for category in categories:
        if (category == "gift"):
            newCategories.append("gift&store")
        elif (category == "services"):
            newCategories.append("service")
        elif (category == "other"):
            newCategories.append("leisure")
        else:
            newCategories.append(category)
    return newCategories


def locationFeatureDriver(address, frontendCategories):
    # input: userAddress and businessCategories[],
    # where businessCategories = ["clothes", "food", "leisure", "service", "gift&store"] (choose one or multiple from this list),
    # eg. locationFeatureDriver("2 E Main St, Madison, WI 53702", ["leisure"])
    # output: [business0, business1, ..., business19],
    # where business = [name, formatted_address, business_status, url, vicinity, category_1, category_2, latitude, longitude, distance]
    # Note: distance is in miles
    categories = filterConverter(frontendCategories)
    selectedBusinesses = []
    if len(categories) == 1:
        N = Num
        return locationFeatureForOneCategory(N, address, categories[0], selectedBusinesses)
    else:
        N = math.ceil(Num / len(categories))
        for category in categories:
            selectedBusinesses = locationFeatureForOneCategory(
                N, address, category, selectedBusinesses)
        # sort the selectedBusinesses by distance
        selectedBusinesses.sort(key=lambda row: row[-1])
        return selectedBusinesses


def printer(list):
    for element in list:
        print(element)


if __name__ == "__main__":
    printer(locationFeatureDriver("2 E Main St, Madison, WI 53702", [
        "gift", "other", "services"]))
