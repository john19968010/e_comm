from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from product.views import ProductViewSet

router = DefaultRouter()
router.register("product", ProductViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
