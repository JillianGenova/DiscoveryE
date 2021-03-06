import requests
import json
import time
import csv
# run pip install geopy for this!
import geopy.distance

# This class uses the Google Places and Geolocation API
# Class variables:  apiKey - The api key that confirms credentials
# Class functions:  search_places_by_coordinate
#                   get_place_details
#                   extract_lat_long_via_address
class GoogleMaps(object):
    def __init__(self, apiKey):
        super(GoogleMaps, self).__init__()
        self.apiKey = apiKey

    # This function finds the closest places and gets place IDs.
    # Arguments:    location -  coordinates of the user
    #               radius -    radius of search in meters
    #               types -     categories of small businesses
    # Returns :     places -    list of places with place_ids in json format
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

    # This function gets details abput a particular place using place ids
    # Arguments :   place_id -      unique identification of each place
    #               fields -        various details required. Eg. name, address, photo, etc.
    # Returns :     place_details - required field details of a particular place 
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

    # This function converts addresses to coordinates
    # Arguments :   address_or_zipcode -    address or zipcode to convert
    # Returns :     (lat, lng) -    coordinates
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

# This function calculates distances between two coordinates
# Arguments :   coord_1, coord_2 -  two tuples containing latitiude and longitude
# Returns :     distance -          distance in miles
def distance_between_coordinates(coord_1, coord_2):
    distance = geopy.distance.distance(coord_1, coord_2).miles
    return distance


def get_user_details(api):
    address = input("Enter your address or a zipcode: ")

    (user_lat, user_lng) = api.extract_lat_long_via_address(address)
    user_coord = str(user_lat) + ", " + str(user_lng)

    type = input("Enter a category: ")

    places = api.search_places_by_coordinate(user_coord, "1000", type)
    fields = ['name', 'formatted_address', 'business_status', 'url', 'vicinity']

    store_business_details(api, fields, places, user_lat, user_lng)


def store_business_details(api, fields, places, user_lat, user_lng):

    with open(type+".csv", 'w') as f:

        dw = csv.DictWriter(f, delimiter = ',', fieldnames=fields)
        dw.writeheader()

        for place in places:
            details = api.get_place_details(place['place_id'], fields)

            (business_lat, business_lng) = api.extract_lat_long_via_address(details['result']['formatted_address'])
            distance = distance_between_coordinates((user_lat, user_lng), (business_lat, business_lng))

            print("Distance of", distance, "miles")
            
            dw.writerow(details['result'])
            
        f.close()
    
    print("Extraction over. Check csv file.")
