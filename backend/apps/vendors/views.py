from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Vendor
@api_view(['GET'])
def list_vendors(_):
    return Response([{'id':v.id,'business':v.business_name,'state':v.state,
                      'verified':v.verified,'rating':v.rating} for v in Vendor.objects.all()])
@api_view(['POST'])
def register_vendor(request):
    if not request.user.is_authenticated: return Response({'error':'login'}, status=401)
    v,_ = Vendor.objects.get_or_create(user=request.user, defaults={
        'business_name':request.data.get('business_name','My Farm Shop'),
        'gstin':request.data.get('gstin',''),'state':request.data.get('state','')})
    return Response({'ok':True,'vendor_id':v.id})
