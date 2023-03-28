from django.db import models


class EntertainmentsPlace(models.Model):
    entertainments_place_id = models.AutoField(primary_key=True)
    entertainments_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    description = models.CharField(max_length=100)


class EntertainmentsEvent(models.Model):
    id = models.AutoField(primary_key=True)
    entertainments_event_name = models.CharField(max_length=50)
    entertainment_place = models.ForeignKey(
        EntertainmentsPlace, on_delete=models.CASCADE)
    language = models.CharField(max_length=10)
    start_time = models.TimeField()
    reserve_date = models.DateField()
    hall = models.IntegerField()
    description = models.CharField(max_length=100)
    image = models.CharField(max_length=200)


class Events(models.Model):
    events_id = models.AutoField(primary_key=True)
    events_name = models.CharField(max_length=50)
    date = models.DateField()
    description = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    price_range = models.CharField(max_length=50)
    image = models.CharField(max_length=200)


class Tours(models.Model):
    tours_id = models.AutoField(primary_key=True)
    tours_name = models.CharField(max_length=50)
    date = models.DateField()
    description = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    collection_time = models.TimeField()
    check_out = models.TimeField()
    place_collection = models.CharField(max_length=200)
    arrival_time = models.CharField(max_length=50)
    cost = models.FloatField()


class TourSchedule(models.Model):
    tour_schedule_id = models.AutoField(primary_key=True)
    tours = models.ForeignKey(Tours, on_delete=models.CASCADE)
    schedule_item = models.CharField(max_length=50)
    schedule_item_description = models.CharField(max_length=100)
    schedule_item_order = models.IntegerField()


class ToursImage(models.Model):
    tours_image_id = models.AutoField(primary_key=True)
    tours = models.ForeignKey(Tours, on_delete=models.CASCADE)
    image = models.CharField(max_length=200)


class FoodPlaceCategory(models.Model):
    food_place_category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50)


class Cuisine(models.Model):
    cuisine_id = models.AutoField(primary_key=True)
    cuisine_name = models.CharField(max_length=100)


class FoodPlaces(models.Model):
    food_place_id = models.AutoField(primary_key=True)
    average_check = models.FloatField()
    place_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE)
    food_place_category = models.ForeignKey(
        FoodPlaceCategory, on_delete=models.SET_NULL, null=True)


class Menu(models.Model):
    menu_id = models.AutoField(primary_key=True)
    food_places = models.ForeignKey(FoodPlaces, on_delete=models.CASCADE)
    food_item = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.CharField(max_length=255)