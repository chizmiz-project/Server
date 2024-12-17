from django.urls import include, path
from rest_framework.routers import DefaultRouter

from ad.views import AdvertisementViewSet

router = DefaultRouter()
router.register(r'', AdvertisementViewSet, basename='ads')

urlpatterns = [
    path('', include(router.urls)),
]