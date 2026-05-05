from rest_framework.decorators import api_view
from rest_framework.response import Response
SETTINGS = {'theme':'light','language':'en','currency':'INR','symbol':'₹',
            'languages':['en','hi','kn','ta','te','ml','mr','gu','bn','pa']}
@api_view(['GET','POST'])
def settings_view(request):
    if request.method=='POST':
        SETTINGS.update(request.data); return Response(SETTINGS)
    return Response(SETTINGS)
