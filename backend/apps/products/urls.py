from django.urls import path
from . import views
urlpatterns = [
    path('', views.list_products),
    path('categories/', views.categories),
    path('cart/', views.cart),
    path('<int:pk>/', views.detail),
    path('<int:pk>/review/', views.add_review),
    path('<int:pk>/add-to-cart/', views.add_to_cart),
    path('<int:pk>/wishlist/', views.toggle_wishlist),
]
