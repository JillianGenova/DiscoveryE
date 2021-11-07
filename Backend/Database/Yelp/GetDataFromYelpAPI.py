'''@author AJWuu'''

import requests
import json
import pandas as pd

#input and output settings
my_api_key = 'eue-NASbu9ZceffGnrHQ1x6zVqd-QeXaXmr114dqsVj3Kije_WzUHblD5ea5et3W3oi6uf5aU7144EkwXyOn1pANueUmm-a9bhKWNz-UnVbWBNaQkSyOloty8g5lYXYx'
input_url = 'https://api.yelp.com/v3/businesses/search'
csv_path = 'yelpData.csv'

'''get data from api to .json'''
def get_data(i: int) -> None:
    HEADERS = {'Authorization': 'Bearer %s' % my_api_key}
    params = {'location':'Madison', 'limit': 50, 'offset':(i*50+1)}
    data = requests.get(input_url, params=params, headers=HEADERS).json()
    '''store in yelpDataXX.json'''
    with open("yelpData%02d.json"%i, 'w', encoding='utf-8') as file:
        json.dump(data, file)

'''load .json and write the results to .csv'''
def load_json_write_csv(i: int) -> None:
    '''load .json'''
    with open("yelpData%02d.json"%i, encoding='utf-8') as json_data:    
        data = json.load(json_data)
    
    '''create data groups'''
    id = []
    name = []
    image_url = []
    is_closed = []
    url = []
    review_count = []
    rating = []
    latitude = []
    longitude = []
    address1 = []
    address2 = []
    address3 = []
    city = []
    zip_code = []
    country = []
    state = []
    phone = []
    pick_up = []
    delivery = []
    restaurant_reservation = []
    categories = []
    index = 0

    '''for well-organized, non-nested data, pandas.io.json.json_normalize() could be used directly'''
    '''loop over all the businesses in .json'''
    for business in data["businesses"]:
        '''take in all the information'''
        id.append(business["id"])
        name.append(business["name"])
        image_url.append(business["image_url"])
        is_closed.append(business["is_closed"])
        url.append(business["url"])
        review_count.append(business["review_count"])
        rating.append(business["rating"])
        latitude.append(business["coordinates"]["latitude"])
        longitude.append(business["coordinates"]["longitude"])
        address1.append(business["location"]["address1"])
        address2.append(business["location"]["address2"])
        address3.append(business["location"]["address3"])
        city.append(business["location"]["city"])
        zip_code.append(business["location"]["zip_code"])
        country.append(business["location"]["country"])
        state.append(business["location"]["state"])
        phone.append(business["phone"])

        '''check if the three kinds of transactions are available'''
        flag_pickup = False
        flag_delivery = False
        flag_restaurant_reservation = False
        for transaction in business["transactions"]:
            if transaction == 'pickup':
                flag_pickup = True
            elif transaction == 'delivery':
                flag_delivery = True
            elif transaction == 'restaurant_reservation':
                flag_restaurant_reservation = True
        pick_up.append(flag_pickup)
        delivery.append(flag_delivery)
        restaurant_reservation.append(flag_restaurant_reservation)
        
        '''get the full categories as one element'''
        categories.append([])
        for category in business["categories"]:
            categories[index].append(category["title"])
        index += 1

    '''output to .csv'''
    df = pd.DataFrame({'ID':id, 'Name':name, 'url':url, 'Number of Reviews':review_count, 
                       'Rating':rating, 'isClosed':is_closed, 'Latitude':latitude, 'Longitude':longitude,
                       'Address_1':address1, 'Address_2':address2, 'Address_3':address3,
                       'City':city, 'Zip':zip_code, 'State':state, 'Country':country, 'Phone':phone,
                       'pick_up':pick_up, 'delivery':delivery, 'restaurant_reservation':restaurant_reservation,
                       'Categories':categories, 'Image':image_url})
    with open("yelpData%02d.csv"%i, 'w', encoding='utf-8') as file:
        df.to_csv(file, index=False, encoding='utf-8')

if __name__ == '__main__':
    '''Yelp API only returns up to 1,000 results (which is actually only 250 now) and it doesn't allow more than 50 per request'''
    for i in range (0,20):
        get_data(i)
        load_json_write_csv(i)
        
