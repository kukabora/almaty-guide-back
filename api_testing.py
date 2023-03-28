import requests

# Set the base URL for your Django Rest Framework API
BASE_URL = "http://localhost:8000/api/data/"

# Define the data to be used for creating and updating records
event_data = {
    "events_name": "Test Event",
    "date": "2023-03-27",
    "description": "This is a test event",
    "location": "Test Location",
    "price_range": "Free",
    "image": "https://example.com/test_event.jpg"
}

tour_data = {
    "tours_name": "Test Tour",
    "date": "2023-03-27",
    "description": "This is a test tour",
    "location": "Test Location",
    "collection_time": "09:00:00",
    "check_out": "17:00:00",
    "place_collection": "Test Collection Place",
    "arrival_time": "18:00:00",
    "cost": 50.0
}

entertainment_place_data = {
    "entertainments_name": "Test Entertainment Place",
    "address": "Test Address",
    "description": "This is a test entertainment place"
}

entertainment_event_data = {
    "entertainments_event_name": "Test Entertainment Event",
    "entertainment_place_id": 1,
    "language": "English",
    "start_time": "20:00:00",
    "reserve_date": "2023-03-27",
    "hall": 1,
    "description": "This is a test entertainment event",
    "image": "https://example.com/test_event.jpg"
}

tour_schedule_data = {
    "tours_id": 1,
    "schedule_item": "Test Schedule Item",
    "schedule_item_description": "This is a test schedule item",
    "schedule_item_order": 1
}

tours_image_data = {
    "tours_id": 1,
    "image": "https://example.com/test_image.jpg"
}

food_place_category_data = {
    "category_name": "Test Category"
}

cuisine_data = {
    "cuisine_name": "Test Cuisine"
}

food_place_data = {
    "average_check": 50.0,
    "place_name": "Test Food Place",
    "address": "Test Address",
    "cuisine_id": 1,
    "food_place_category_id": 1
}

menu_data = {
    "food_places_id": 1,
    "food_item": "Test Food Item",
    "price": 10.0,
    "description": "This is a test food item"
}

# Perform CRUD operations on each of the tables

# Events table
# Create a new event
response = requests.post(BASE_URL + "events/", data=event_data)
print(response.json())

# Retrieve all events
response = requests.get(BASE_URL + "events/")
print(response.json())

# Retrieve a specific event by ID
response = requests.get(BASE_URL + "events/1/")
print(response.json())

# Update an existing event by ID
event_data["description"] = "This is an updated test event"
response = requests.put(BASE_URL + "events/1/", data=event_data)
print(response.json())

# Delete an event by ID
response = requests.delete(BASE_URL + "events/1/")
print(response.json())

# Tours table
# Create a new tour
response = requests.post(BASE_URL + "tours/", data=tour_data)
print(response.json())

# Retrieve all tours
response = requests.get(BASE_URL + "tours/")
# Retrieve a specific tour by ID
response = requests.get(BASE_URL + "tours/1/")
print(response.json())

# Update an existing tour by ID
tour_data["description"] = "This is an updated test tour"
response = requests.put(BASE_URL + "tours/1/", data=tour_data)
print(response.json())

# Delete a tour by ID
response = requests.delete(BASE_URL + "tours/1/")
print(response.json())

# EntertainmentsPlace table
# Create a new entertainment place
response = requests.post(
    BASE_URL + "entertainmentsplace/", data=entertainment_place_data)
print(response.json())

# Retrieve all entertainment places
response = requests.get(BASE_URL + "entertainmentsplace/")
print(response.json())

# Retrieve a specific entertainment place by ID
response = requests.get(BASE_URL + "entertainmentsplace/1/")
print(response.json())

# Update an existing entertainment place by ID
entertainment_place_data["description"] = "This is an updated test entertainment place"
response = requests.put(BASE_URL + "entertainmentsplace/1/",
                        data=entertainment_place_data)
print(response.json())

# Delete an entertainment place by ID
response = requests.delete(BASE_URL + "entertainmentsplace/1/")
print(response.json())

# EntertainmentsEvent table
# Create a new entertainment event
response = requests.post(
    BASE_URL + "entertainmentsevent/", data=entertainment_event_data)
print(response.json())

# Retrieve all entertainment events
response = requests.get(BASE_URL + "entertainmentsevent/")
print(response.json())

# Retrieve a specific entertainment event by ID
response = requests.get(BASE_URL + "entertainmentsevent/1/")
print(response.json())

# Update an existing entertainment event by ID
entertainment_event_data["description"] = "This is an updated test entertainment event"
response = requests.put(BASE_URL + "entertainmentsevent/1/",
                        data=entertainment_event_data)
print(response.json())

# Delete an entertainment event by ID
response = requests.delete(BASE_URL + "entertainmentsevent/1/")
print(response.json())

# TourSchedule table
# Create a new tour schedule
response = requests.post(BASE_URL + "tourschedule/", data=tour_schedule_data)
print(response.json())

# Retrieve all tour schedules
response = requests.get(BASE_URL + "tourschedule/")
print(response.json())

# Retrieve a specific tour schedule by ID
response = requests.get(BASE_URL + "tourschedule/1/")
print(response.json())

# Update an existing tour schedule by ID
tour_schedule_data["schedule_item_description"] = "This is an updated test schedule item"
response = requests.put(BASE_URL + "tourschedule/1/", data=tour_schedule_data)
print(response.json())

# Delete a tour schedule by ID
response = requests.delete(BASE_URL + "tourschedule/1/")
print(response.json())

# ToursImage table
# Create a new tour image
response = requests.post(BASE_URL + "toursimage/", data=tours_image_data)
print(response.json())

# Retrieve all tour images
response = requests.get(BASE_URL + "toursimage/")
print(response.json())

# Retrieve a specific tour image by ID
response = requests.get(BASE_URL + "toursimage/1/")
print(response.json())

# Update an existing tour image by ID
tours_image_data["image"] = "https://example.com/updated_test_image.jpg"
response = requests.put(BASE_URL + "toursimage/1/", data=tours_image_data)
print(response.json())

# Delete a tour image by ID
response = requests.delete(BASE_URL + "toursimage/1/")
print(response.json())

# FoodPlaceCategory table
# Create a new food place category
response = requests.post(BASE_URL + "foodplacecategory/",
                         data=food_place_category_data)
print(response.json())

# Retrieve all food place categories
response = requests.get(BASE_URL + "foodplacecategory/")
print(response.json())

# Retrieve a specific food place category by ID
response = requests.get(BASE_URL + "foodplacecategory/1/")
print(response.json())

# Update an existing food place category by ID
food_place_category_data["category_name"] = "Updated Test Category"
response = requests.put(BASE_URL + "foodplacecategory/1/",
                        data=food_place_category_data)
print(response.json())

# Delete a food place category by ID
response = requests.delete(BASE_URL + "foodplacecategory/1/")
print(response.json())

# Cuisine table
# Create a new cuisine
response = requests.post(BASE_URL + "cuisine/", data=cuisine_data)
print(response.json())

# Retrieve all cuisines
response = requests.get(BASE_URL + "cuisine/")
print(response.json())

# Retrieve a specific cuisine by ID
response = requests.get(BASE_URL + "cuisine/1/")
print(response.json())

# Update an existing cuisine by ID
cuisine_data["cuisine_name"] = "Updated Test Cuisine"
response = requests.put(BASE_URL + "cuisine/1/", data=cuisine_data)
print(response.json())

# Delete a cuisine by ID
response = requests.delete(BASE_URL + "cuisine/1/")
print(response.json())

# FoodPlaces table
# Create a new food place
response = requests.post(BASE_URL + "foodplaces/", data=food_place_data)
print(response.json())

# Retrieve all food places
response = requests.get(BASE_URL + "foodplaces/")
print(response.json())

# Retrieve a specific food place by ID
response = requests.get(BASE_URL + "foodplaces/1/")
print(response.json())

# Update an existing food place by ID
food_place_data["address"] = "Updated Test Address"
response = requests.put(BASE_URL + "foodplaces/1/", data=food_place_data)
print(response.json())

# Delete a food place by ID
response = requests.delete(BASE_URL + "foodplaces/1/")
print(response.json())

# Menu table
# Create a new menu
response = requests.post(BASE_URL + "menu/", data=menu_data)
print(response.json())

# Retrieve all menus
response = requests.get(BASE_URL + "menu/")
print(response.json())

# Retrieve a specific menu by ID
response = requests.get(BASE_URL + "menu/1/")
print(response.json())

# Update an existing menu by ID
menu_data["price"] = 15.0
response = requests.put(BASE_URL + "menu/1/", data=menu_data)
print(response.json())

# Delete a menu by ID
response = requests.delete(BASE_URL + "menu/1/")
print(response.json())
