# Location Feature  
Contents include:  
1. Grasp user coordinates (based on the input) from Google Map API  
2. Fetch business coordinates from the database  
3. Calculate the distances between two sets of coordinates  
4. Sort the distances  
5. Output the closest ones  

TO-DO:  
call getCoordinates() in databaseQuery.insertCoordinates(name, category_1)  
call getCoordinates() in location.locationFeatureDriver(address, category_1)  
call calculateDistance() in location.getDistance(businessCoordinates)  
find outside packages for sorting (bypass the limitation of python supporting only 300 data)  
