from .models import (
    EntertainmentsPlace,
    EntertainmentsEvent,
    Events,
    Tours,
    TourSchedule,
    ToursImage,
    FoodPlaceCategory,
    Cuisine,
    FoodPlaces,
    Menu
)
from django.contrib.auth.models import User
from rest_framework import serializers


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class EntertainmentsPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntertainmentsPlace
        fields = '__all__'


class EntertainmentsEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntertainmentsEvent
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'


class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tours
        fields = '__all__'


class TourScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourSchedule
        fields = '__all__'


class ToursImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToursImage
        fields = '__all__'


class FoodPlaceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodPlaceCategory
        fields = '__all__'


class CuisineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuisine
        fields = '__all__'


class FoodPlacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodPlaces
        fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
