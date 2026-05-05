from django.contrib import admin
from .models import Product, Category, Review, Wishlist, CartItem
admin.site.register([Product, Category, Review, Wishlist, CartItem])
