from rest_framework import viewsets

from product.models import Product


class ProductViewSet(viewsets.ModelViewSet):
    http_method_names = ["get", "post", "patch", "delete"]
    queryset = Product.objects.all().order_by("-id")
