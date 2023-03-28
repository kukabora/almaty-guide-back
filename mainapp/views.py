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
from .serializers import (
    EntertainmentsPlaceSerializer,
    EntertainmentsEventSerializer,
    EventSerializer,
    TourSerializer,
    TourScheduleSerializer,
    ToursImageSerializer,
    FoodPlaceCategorySerializer,
    CuisineSerializer,
    FoodPlacesSerializer,
    MenuSerializer
)
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from .serializers import UserRegistrationSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from django.http import FileResponse
from .permissions import CustomModelPermission
from django.conf import settings
import os


def test(req):
    return HttpResponse("Hello world")


class ProtectedView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response({"message": "This is a protected view. You are authenticated!"})


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]


class EntertainmentsPlaceViewSet(viewsets.ModelViewSet):
    queryset = EntertainmentsPlace.objects.all()
    serializer_class = EntertainmentsPlaceSerializer
    permission_classes = [permissions.IsAuthenticated, CustomModelPermission]


class EntertainmentsEventViewSet(viewsets.ModelViewSet):
    queryset = EntertainmentsEvent.objects.all()
    serializer_class = EntertainmentsEventSerializer
    permission_classes = [permissions.IsAuthenticated, CustomModelPermission]


class EventViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated, CustomModelPermission]


class TourViewSet(viewsets.ModelViewSet):
    queryset = Tours.objects.all()
    serializer_class = TourSerializer
    permission_classes = [permissions.IsAuthenticated, CustomModelPermission]


class TourScheduleViewSet(viewsets.ModelViewSet):
    queryset = TourSchedule.objects.all()
    serializer_class = TourScheduleSerializer
    permission_classes = [permissions.IsAuthenticated, CustomModelPermission]


class ToursImageViewSet(viewsets.ModelViewSet):
    queryset = ToursImage.objects.all()
    serializer_class = ToursImageSerializer
    permission_classes = [permissions.IsAuthenticated, CustomModelPermission]


class FoodPlaceCategoryViewSet(viewsets.ModelViewSet):
    queryset = FoodPlaceCategory.objects.all()
    serializer_class = FoodPlaceCategorySerializer
    permission_classes = [permissions.IsAuthenticated, CustomModelPermission]


class CuisineViewSet(viewsets.ModelViewSet):
    queryset = Cuisine.objects.all()
    serializer_class = CuisineSerializer
    permission_classes = [permissions.IsAuthenticated, CustomModelPermission]


class FoodPlacesViewSet(viewsets.ModelViewSet):
    queryset = FoodPlaces.objects.all()
    serializer_class = FoodPlacesSerializer
    permission_classes = [permissions.IsAuthenticated, CustomModelPermission]


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated, CustomModelPermission]


def media_view(request, file_path):
    full_file_path = os.path.join(settings.MEDIA_ROOT, file_path)
    if os.path.exists(full_file_path):
        return FileResponse(open(full_file_path, 'rb'))
    else:
        return Response(status=404)
