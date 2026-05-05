from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view(['POST'])
def check(request):
    # TODO: ML fraud scoring
    score = 0
    amt = float(request.data.get('amount',0))
    if amt > 50000: score += 30
    if request.data.get('new_user'): score += 20
    return Response({'risk_score':score,'verdict':'high' if score>40 else 'low'})
@api_view(['POST'])
def dispute(request):
    return Response({'ok':True,'dispute_id':123,'status':'open','note':'TODO dispute workflow'})
