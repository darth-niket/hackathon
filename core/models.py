from django.conf import settings
from django.db import models
from django.db.models import CharField

class Item(models.Model):
    imagePath = models.CharField(max_length=300)
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    price = models.FloatField()
    leodeliverable = models.BooleanField(default=False)
    def __str__(self):
        return self.title


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()