from django.db import models
from inventory.models import Inventory


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    style = models.CharField(max_length=20)
    buy_number = models.IntegerField()
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name.capitalize()} - ${self.price}"

    class Meta:
        db_table = "product"
