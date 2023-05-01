from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'entertainments-places', EntertainmentsPlaceViewSet)
router.register(r'entertainments-events', EntertainmentsEventViewSet)
router.register(r'events', EventViewSet)
router.register(r'tours', TourViewSet)
router.register(r'tour-schedules', TourScheduleViewSet)
router.register(r'tours-images', ToursImageViewSet)
router.register(r'food-place-categories', FoodPlaceCategoryViewSet)
router.register(r'cuisines', CuisineViewSet)
router.register(r'menutypes', MenuTypeViewSet)
router.register(r'food-places', FoodPlacesViewSet)
router.register(r'menus', MenuViewSet)
router.register(r'layouts', RestaurantTableViewSet)
router.register(r'entertainment-place-category',
                EntertainmentPlaceCategoriesViewSet)

urlpatterns = [
    path('test/', ProtectedView.as_view(), name='protected'),
    path('user-info', retrieve_user_info, name='user-info'),
    path('token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('data/', include(router.urls)),
    path('media/<path:file_path>/', media_view),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
