from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from apps.products.models import Product
from apps.transactions.models import Order
@api_view(['GET'])
def dashboard(_):
    return Response({
        'total_users':User.objects.count(),
        'total_products':Product.objects.count(),
        'total_orders':Order.objects.count(),
        'revenue':float(sum(o.total_price for o in Order.objects.all())),
        'low_stock':[{'id':p.id,'title':p.title,'stock':p.stock}
                     for p in Product.objects.filter(stock__lt=10)],
        'top_products':[{'title':p.title,'sold':p.sold} for p in Product.objects.order_by('-sold')[:5]],
    })
