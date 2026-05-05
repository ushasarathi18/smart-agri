from rest_framework.decorators import api_view
from rest_framework.response import Response

KB = {
    'price':'Visit Market page to see live prices and forecasts for 25+ crops across all Indian states.',
    'disease':'Upload a leaf image on the Disease page to get pesticide and treatment advice.',
    'scheme':'Check Government Schemes section: PM-KISAN, PMFBY (insurance), KCC (loans), Soil Health Card.',
    'soil':'For soil suitability, see each product page Cultivation Guide section.',
    'payment':'We support COD, Online, UPI/GPay, and QR Code payments. GST 5% + Rs.100 transport applies.',
    'support':'Use the floating WhatsApp button or email support@smartagri.in.',
    'weather':'Weather-based pricing is integrated in the Dynamic Pricing engine.',
    'organic':'Organic alternatives are listed on the Disease detection result page.',
}
@api_view(['POST'])
def chat(request):
    msg = (request.data.get('message') or '').lower()
    for k,v in KB.items():
        if k in msg: return Response({'reply':v})
    # TODO: integrate OpenAI / Lovable AI gateway for real AI replies
    return Response({'reply':"I can help with prices, diseases, schemes, soil, payments, weather, organic farming, support. Try asking about one!"})
