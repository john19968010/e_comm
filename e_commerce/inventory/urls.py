from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from inventory.views import InventoryViewSet

router = DefaultRouter()
router.register("inventory", InventoryViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
