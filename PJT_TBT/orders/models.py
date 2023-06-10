from django.db import models
from products.models import Product
from django.conf import settings


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()

class Order(models.Model):
    order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)





