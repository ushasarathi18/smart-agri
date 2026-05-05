from django.db import models
from django.contrib.auth.models import User
from apps.products.models import Product

class Order(models.Model):
    STATUS = [('pending','Pending'),('paid','Paid'),('shipped','Shipped'),
              ('delivered','Delivered'),('cancelled','Cancelled'),('refunded','Refunded')]
    PAYMENT = [('cod','Cash on Delivery'),('online','Online'),('upi','UPI/GPay'),('qr','QR Code')]
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    gst = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    transport = models.DecimalField(max_digits=10, decimal_places=2, default=100)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT, default='cod')
    status = models.CharField(max_length=20, choices=STATUS, default='pending')
    address = models.TextField(blank=True)
    state = models.CharField(max_length=80, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
