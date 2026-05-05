from django.urls import path
from . import views
urlpatterns = [
    path('crops/', views.crops),
    path('locations/', views.locations),
    path('history/', views.history),
    path('compare/', views.compare),
    path('dynamic-price/', views.dynamic_price),
]
