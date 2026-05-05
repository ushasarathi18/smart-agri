from django.urls import path
from . import views
urlpatterns = [path('detect/', views.detect), path('list/', views.diseases_list)]
