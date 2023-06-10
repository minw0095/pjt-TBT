from django.db import models
from products.models import Product, ProductImage
from accounts.models import User

# Create your models here.
class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)
    quantity = models.ManyToManyField("products.Product")

    class Meta:
        db_table = "Cart"
        ordering = ["date_added"]

        def __str__(self):
            return self.cart_id


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=False)

    class Meta:
        db_table = "CartItem"

    def sub_total(self):
        # 템플릿에서 사용하는 변수로 장바구니에 담긴 각 상품의 합계
        return self.product.pay * self.quantity

    def __int__(self):
        return self.product
