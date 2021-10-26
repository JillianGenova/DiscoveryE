import requests
import json
import time
import pandas as pd
import csv

class GoogleMaps(object):
    def __init__(self, apiKey):
        super(GoogleMaps, self).__init__()
        self.apiKey = apiKey

    # To get place details, you need to search for places and get the place IDs first. 
    # Fortunately there is an API endpoint for this with which you will send a GPS Coordinate and a radius to the API and it 
    # will return the nearby places by your defined radius. Also there is a filter called 
    # "types" which can filter out only the types of the places that you are interested in 
    # like "school" or "restaurant"
    def search_places_by_coordinate(self, location, radius, types):
        endpoint_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        places = []
        params = {
            'location': location,
            'radius': radius,
            'types': types,
            'key': self.apiKey
        }
        res = requests.get(endpoint_url, params = params)
        results =  json.loads(res.content)
        places.extend(results['results'])
        time.sleep(2)
        while "next_page_token" in results:
            params['pagetoken'] = results['next_page_token'],
            res = requests.get(endpoint_url, params = params)
            results = json.loads(res.content)
            places.extend(results['results'])
            time.sleep(2)
        return places

    def get_place_details(self, place_id, fields):
        endpoint_url = "https://maps.googleapis.com/maps/api/place/details/json"
        params = {
            'placeid': place_id,
            'fields': ",".join(fields),
            'key': self.apiKey
        }
        res = requests.get(endpoint_url, params = params)
        place_details =  json.loads(res.content)
        return place_details

    def extract_lat_long_via_address(self, address_or_zipcode):
        lat, lng = None, None
        base_url = "https://maps.googleapis.com/maps/api/geocode/json"
        endpoint_url = f"{base_url}?address={address_or_zipcode}&key={self.apiKey}"
        r = requests.get(endpoint_url)
        if r.status_code not in range(200, 299):
            return None, None
        try:
            results = r.json()['results'][0]
            lat = results['geometry']['location']['lat']
            lng = results['geometry']['location']['lng']
        except:
            pass
        return (lat, lng)

if __name__ == "__main__":
    api = GoogleMaps("AIzaSyCxWIknbp4ZFgl8JbsVmYh-rJ_65cFttv0")

    address = input("Enter your address or a zipcode: ")

    (lat, lng) = api.extract_lat_long_via_address(address)
    coordinates = str(lat) + ", " + str(lng)

    places = api.search_places_by_coordinate(coordinates, "1000", "restaurant")

    fields = ['name', 'formatted_address', 'business_status', 'url', 'vicinity', 'photo']

    for place in places:
        details = api.get_place_details(place['place_id'], fields)

        try:
            business_status = details['result']['business_status']
        except KeyError:
            business_status = ""
    
        try:
            name = details['result']['name']
        except KeyError:
            name = ""
    
        try:
            address = details['result']['formatted_address']
        except KeyError:
            address = ""
    
        try:
            url = details['result']['url']
        except KeyError:
            url = ""
    
        try:
            vicinity = details['result']['vicinity']
        except KeyError:
            vicinity = ""

        try:
            photo = details['result']['photo']
        except KeyError:
            photo = ""
        print("===================PLACE===================")
        print("Name:", name)
        print("Address:", address)
        print("Business status:", business_status)
        print("URL:", url)
        print("Vicinity:", vicinity)
        print("Photo:", photo, "\n")
        


    # with open('output.csv', 'w') as output:
    #     writer = csv.writer(output)
    #     for key, value in details.items():
    #         writer.writerow([key, value])

    # df = pd.DataFrame(data=details)
    # df = (df.T)
    # df.to_excel('details.xlsx')
