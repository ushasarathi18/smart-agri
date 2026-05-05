from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings

@api_view(['POST'])
def send_email(request):
    try:
        send_mail(request.data.get('subject','Smart Agri'),
                  request.data.get('message',''),
                  settings.DEFAULT_FROM_EMAIL,
                  [request.data.get('to')], fail_silently=True)
        return Response({'ok':True,'channel':'gmail'})
    except Exception as e: return Response({'error':str(e)}, status=500)

@api_view(['POST'])
def send_sms(request):
    # TODO: integrate Twilio/Fast2SMS
    return Response({'ok':True,'channel':'sms','note':'TODO integrate SMS gateway',
                      'to':request.data.get('to'),'message':request.data.get('message')})

@api_view(['POST'])
def send_whatsapp(request):
    # TODO: integrate WhatsApp Business API
    num = settings.WHATSAPP_NUMBER
    msg = request.data.get('message','Hello from Smart Agri')
    return Response({'ok':True,'channel':'whatsapp',
                      'link':f'https://wa.me/{num}?text={msg}'})

@api_view(['POST'])
def push(request):
    # TODO: integrate FCM
    return Response({'ok':True,'channel':'push','note':'TODO FCM'})
