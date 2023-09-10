from django.db import models
from django.contrib.auth.models import User
from product.models import Product


# Create your models here.


class Order(models.Model):
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_user')
    full_name = models.CharField(max_length=50)
    address1 = models.CharField(max_length=250)
    address2 = models.CharField(max_length=250,blank=True)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    post_code = models.CharField(max_length=20,blank=True)
    status = models.CharField(
        max_length=255,
        choices=[
            ('PENDING', 'Pending'),
            ('SHIPPED', 'Shipped'),
            ('DELIVERED', 'Delivered'),
        ]
        ,
        default='Pending'
    )
    comment = models.TextField(blank=True,null=True)
    order_key = models.CharField(max_length=200)
    total_paid = models.DecimalField(max_digits=5, decimal_places=2)
    billing_status = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return str(self.customer_id.username)


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                related_name='order_items',
                                on_delete=models.CASCADE)
    
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{} order'.format(self.order.customer_id.first_name)
    
      
# class Coupon(models.Model):
#     code = models.CharField(max_length=255)
#     discount = models.DecimalField(max_digits=10, decimal_places=2)
#     start_date = models.DateTimeField()
#     end_date = models.DateTimeField()
#     active = models.BooleanField(default=True)
#     product = models.ForeignKey('Product', on_delete=models.CASCADE)

