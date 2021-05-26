# from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets

from inventory.models import Inventory


class InventoryViewSet(viewsets.ModelViewSet):
    http_method_names = ["get", "post", "patch", "delete"]
    queryset = Inventory.objects.all().order_by("-id")
