from django.urls import path
from . import views
urlpatterns=[path('plans/',views.plans),path('subscribe/',views.subscribe)]
