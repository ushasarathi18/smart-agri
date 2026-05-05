from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Warehouse
@api_view(['GET'])
def list_wh(_):
    if not Warehouse.objects.exists():
        for n,s in [('Bangalore Hub','karnataka'),('Mumbai Hub','maharashtra'),
                    ('Delhi Hub','delhi'),('Chennai Hub','tamilnadu')]:
            Warehouse.objects.create(name=n,state=s,capacity_tons=2000,used_tons=500)
    return Response([{'id':w.id,'name':w.name,'state':w.state,
                      'capacity':w.capacity_tons,'used':w.used_tons,
                      'available':w.capacity_tons-w.used_tons} for w in Warehouse.objects.all()])
