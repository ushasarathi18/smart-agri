from rest_framework.decorators import api_view
from rest_framework.response import Response
import random
@api_view(['GET'])
def track(request, order_id):
    # TODO: integrate Shiprocket/Delhivery
    stages = ['Order Placed','Packed','Dispatched','In Transit','Out for Delivery','Delivered']
    idx = random.randint(0,len(stages)-1)
    return Response({'order_id':order_id,'current_stage':stages[idx],
                      'eta_days':random.randint(2,7),
                      'history':stages[:idx+1]})
@api_view(['POST'])
def shipping_quote(request):
    weight = float(request.data.get('weight_kg',5))
    distance = float(request.data.get('distance_km',100))
    fee = round(50 + weight*5 + distance*0.5, 2)
    return Response({'shipping_fee':fee,'currency':'INR','eta_days':3})
