# Database  
1. Build the database from API (which is a one-time action)
2. Query data from the database (for single element of one business, full info for one business, full info for one category, etc.)  
3. Insert data into the database (may not be used at this stage)  
4. Delete data from the database (may not be used at this stage)  

# Location Feature  
1. Grasp user coordinates (based on the input) from Google Map API  
2. Fetch business coordinates from the database  
3. Calculate the distances between two sets of coordinates  
4. Sort the distances  
5. Output the closest ones  

# Final product  
1. business.db -- all the data in the database (full database with all categories)  
2. google_map.py --  
3. databaseQuery.py -- all codes for database query, insert and delete (including some additional functions for extensional use)  
4. location.py -- all codes for location feature (to use this feature, you only need to call locationFeatureDriver(address, category_1))  
