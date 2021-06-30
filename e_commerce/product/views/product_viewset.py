from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from product.models import Product
from product.serializers import ProductSerializer


class ProductCustomPagination(PageNumberPagination):
    page_size = 9
    page_size_query_param = "limit"
    max_page_size = 5


class ProductViewSet(viewsets.ModelViewSet):
    http_method_names = ["get", "post", "patch", "delete"]
    queryset = Product.objects.all().order_by("-last_update_date")
    pagination_class = ProductCustomPagination
    serializer_class = ProductSerializer
