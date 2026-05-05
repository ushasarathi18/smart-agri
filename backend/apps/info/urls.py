from django.urls import path
from . import views
urlpatterns = [path('schemes/',views.schemes),path('soils/',views.soils),
                path('weather/',views.weather),path('policies/',views.policies)]
