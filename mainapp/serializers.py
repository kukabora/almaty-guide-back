from .models import *
from django.contrib.auth.models import User
from rest_framework import serializers


def get_base_url(request):
    scheme = request.scheme  # "http" or "https"
    host = request.get_host()  # The host, including the port (if specified)
    base_url = f"{scheme}://{host}"
    return base_url


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
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Events
        fields = ['events_id', 'events_name', 'date',
                  'description', 'location', 'price_range', 'image_url']

    def get_image_url(self, obj):
        if obj.image:
            request = self.context.get('request')
            base_url = get_base_url(request)
            new_image_url = f"{base_url}/api/media/events-image/{obj.image}/"
            return new_image_url
        return None


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


class RestaurantTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantTable
        fields = '__all__'

    def create(self, validated_data):
        if isinstance(validated_data, list):
            tables = [RestaurantTable(**table_data)
                      for table_data in validated_data]
            return RestaurantTable.objects.bulk_create(tables)
        else:
            return super().create(validated_data)
