from django.db import models
class Warehouse(models.Model):
    name = models.CharField(max_length=200)
    state = models.CharField(max_length=80)
    capacity_tons = models.IntegerField(default=1000)
    used_tons = models.IntegerField(default=0)
