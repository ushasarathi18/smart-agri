from rest_framework.decorators import api_view
from rest_framework.response import Response
PLANS = [
    {'id':'free','name':'Free','price':0,'features':['Browse market','Basic forecasts']},
    {'id':'pro','name':'Pro Farmer','price':199,'features':['Live alerts','Disease detection','Priority support']},
    {'id':'enterprise','name':'Enterprise','price':999,'features':['API access','Bulk orders','Dedicated manager']},
]
@api_view(['GET'])
def plans(_): return Response(PLANS)
@api_view(['POST'])
def subscribe(request):
    # TODO: integrate Razorpay/Stripe recurring
    return Response({'ok':True,'plan':request.data.get('plan_id','pro'),'note':'TODO payment gateway'})
