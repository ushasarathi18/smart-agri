from django.urls import path
from . import views
urlpatterns = [
    path('create/', views.create_order),
    path('my/', views.my_orders),
    path('invoice/<int:pk>/', views.invoice),
]
