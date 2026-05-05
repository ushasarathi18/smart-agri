from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse

def root(_): return JsonResponse({'app':'Smart Agri Market & Disease Detection API','version':'1.0','status':'ok'})

urlpatterns = [
    path('', root),
    path('admin/', admin.site.urls),
    path('api/accounts/', include('apps.accounts.urls')),
    path('api/market/', include('apps.market.urls')),
    path('api/products/', include('apps.products.urls')),
    path('api/disease/', include('apps.disease.urls')),
    path('api/transactions/', include('apps.transactions.urls')),
    path('api/notifications/', include('apps.notifications.urls')),
    path('api/chatbot/', include('apps.chatbot.urls')),
    path('api/info/', include('apps.info.urls')),
    path('api/settings/', include('apps.settings_panel.urls')),
    path('api/services/', include('apps.services.urls')),
    path('api/vendors/', include('apps.vendors.urls')),
    path('api/logistics/', include('apps.logistics.urls')),
    path('api/analytics/', include('apps.analytics.urls')),
    path('api/subscriptions/', include('apps.subscriptions.urls')),
    path('api/fraud/', include('apps.fraud.urls')),
    path('api/warehouse/', include('apps.warehouse.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
