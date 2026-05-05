from django.urls import path
from . import views
urlpatterns = [path('email/',views.send_email),path('sms/',views.send_sms),
                path('whatsapp/',views.send_whatsapp),path('push/',views.push)]
