from django.db import models
from django.contrib.auth.models import User
class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=200)
    gstin = models.CharField(max_length=20, blank=True)
    state = models.CharField(max_length=80, blank=True)
    verified = models.BooleanField(default=False)
    rating = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
