from .models import *
from .serializers import *
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from .serializers import UserRegistrationSerializer
from rest_framework.response import Response
from rest_framework import viewsets, status
from django.http import FileResponse, HttpResponseNotFound
from .permissions import CustomModelPermission
from django_filters.rest_framework import DjangoFilterBackend
from django.conf import settings
import os
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, AuthenticationFailed
from rest_framework_simplejwt.tokens import AccessToken


@api_view(['POST'])
def retrieve_user_info(request):
    token = request.data.get('token', None)
    if token is None:
        return Response({'error': 'Token not provided'}, status=status.HTTP_400_BAD_REQUEST)
    access_token = AccessToken(token)
    user = User.objects.get(id=access_token['user_id'])
    user_data = UserSerializer(user).data
    return Response({'user': user_data}, status=status.HTTP_200_OK)


class ProtectedView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response({"message": "This is a protected view. You are authenticated!"})


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]


class EntertainmentPlaceCategoriesViewSet(viewsets.ModelViewSet):
    queryset = EntertainmentPlaceCategories.objects.all()
    serializer_class = EntertainmentPlaceCategoriesSerializer
    permission_classes = [CustomModelPermission]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'category_name',
    ]


class EntertainmentsPlaceViewSet(viewsets.ModelViewSet):
    queryset = EntertainmentsPlace.objects.all()
    serializer_class = EntertainmentsPlaceSerializer
    permission_classes = [CustomModelPermission]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'entertainments_name',
        'address',
        'description',
        'entertainment_place_category'
    ]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


class EntertainmentsEventViewSet(viewsets.ModelViewSet):
    queryset = EntertainmentsEvent.objects.all()
    serializer_class = EntertainmentsEventSerializer
    permission_classes = [CustomModelPermission]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'entertainments_event_name',
        'entertainment_place',
        'language',
        'start_time',
        'reserve_date',
        'hall',
        'description',
    ]


class EventViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventSerializer
    permission_classes = [CustomModelPermission]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'events_name',
        'date',
        'description',
        'location',
        'price_range',
    ]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


class TourViewSet(viewsets.ModelViewSet):
    queryset = Tours.objects.all()
    serializer_class = TourSerializer
    permission_classes = [CustomModelPermission]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'tours_name',
        'date',
        'description',
        'location',
        'collection_time',
        'check_out',
        'place_collection',
        'arrival_time',
        'cost',
    ]


class RestaurantTableViewSet(viewsets.ModelViewSet):
    queryset = RestaurantTable.objects.all()
    serializer_class = RestaurantTableSerializer
    permission_classes = [CustomModelPermission]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'food_place',
        'table_name',
        'table_capacity',
        'x',
        'y',
        'width',
        'height',
        'shape',
        'hover_color',
    ]

    def create(self, request, *args, **kwargs):
        is_many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=is_many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()


class TourScheduleViewSet(viewsets.ModelViewSet):
    queryset = TourSchedule.objects.all()
    serializer_class = TourScheduleSerializer
    permission_classes = [CustomModelPermission]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'tours',
        'schedule_item',
        'schedule_item_description',
        'schedule_item_order',
    ]


class ToursImageViewSet(viewsets.ModelViewSet):
    queryset = ToursImage.objects.all()
    serializer_class = ToursImageSerializer
    permission_classes = [CustomModelPermission]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tours']

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


class FoodPlaceCategoryViewSet(viewsets.ModelViewSet):
    queryset = FoodPlaceCategory.objects.all()
    serializer_class = FoodPlaceCategorySerializer
    permission_classes = [CustomModelPermission]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category_name']


class CuisineViewSet(viewsets.ModelViewSet):
    queryset = Cuisine.objects.all()
    serializer_class = CuisineSerializer
    permission_classes = [CustomModelPermission]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['cuisine_name']


class MenuTypeViewSet(viewsets.ModelViewSet):
    queryset = MenuType.objects.all()
    serializer_class = MenuTypeSerializer
    permission_classes = [CustomModelPermission]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['type_name']


class FoodPlacesViewSet(viewsets.ModelViewSet):
    queryset = FoodPlaces.objects.all()
    serializer_class = FoodPlacesSerializer
    permission_classes = [CustomModelPermission]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'average_check',
        'place_name',
        'address',
        'cuisine',
        'food_place_category',
    ]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [CustomModelPermission]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'food_places',
        'menu_type_id',
        'food_item',
        'price',
        'description',
        'menu_id'
    ]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


def media_view(request, file_path):
    full_file_path = os.path.join(settings.MEDIA_ROOT, file_path)
    if os.path.exists(full_file_path):
        return FileResponse(open(full_file_path, 'rb'))
    else:
        return HttpResponseNotFound('File not found')
