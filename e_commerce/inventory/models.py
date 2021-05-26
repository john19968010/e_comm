from django.db import models


class Inventory(models.Model):
    storage_number = models.IntegerField()

    class Meta:
        db_table = "inventory"
