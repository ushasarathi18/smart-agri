from rest_framework.decorators import api_view
from rest_framework.response import Response

SCHEMES = [
    {'name':'PM-KISAN','benefit':'₹6000/year direct income support','link':'https://pmkisan.gov.in'},
    {'name':'PMFBY','benefit':'Crop insurance against natural calamities','link':'https://pmfby.gov.in'},
    {'name':'Kisan Credit Card','benefit':'Low-interest agricultural loans','link':'https://www.myscheme.gov.in'},
    {'name':'Soil Health Card','benefit':'Free soil testing every 2 years','link':'https://soilhealth.dac.gov.in'},
    {'name':'PKVY','benefit':'Organic farming promotion','link':'https://pgsindia-ncof.gov.in'},
    {'name':'eNAM','benefit':'Online national agriculture market','link':'https://enam.gov.in'},
]
SOILS = [
    {'type':'Alluvial','crops':['rice','wheat','sugarcane','maize']},
    {'type':'Black','crops':['cotton','sugarcane','jowar','wheat']},
    {'type':'Red','crops':['groundnut','ragi','potato','pulses']},
    {'type':'Laterite','crops':['coconut','cashew','tea','coffee']},
    {'type':'Mountain','crops':['tea','coffee','spices']},
    {'type':'Desert','crops':['bajra','jowar','pulses']},
]
WEATHER_TIPS = [
    {'season':'Kharif (Jun-Oct)','crops':'rice, maize, cotton, soybean','tip':'Monsoon-fed crops; ensure drainage.'},
    {'season':'Rabi (Nov-Apr)','crops':'wheat, mustard, barley','tip':'Cool-season crops; light irrigation.'},
    {'season':'Zaid (Mar-Jun)','crops':'watermelon, cucumber, fodder','tip':'Summer crops; frequent irrigation.'},
]
@api_view(['GET'])
def schemes(_): return Response(SCHEMES)
@api_view(['GET'])
def soils(_): return Response(SOILS)
@api_view(['GET'])
def weather(_):
    # TODO: integrate OpenWeatherMap real API
    return Response({'seasons':WEATHER_TIPS,
                      'current':{'temp':28,'rain':'Light','humidity':72,'note':'TODO real weather API'}})
@api_view(['GET'])
def policies(_):
    return Response({'terms':'Standard terms apply...','privacy':'We protect your data...',
                      'refund':'7-day return for damaged goods.','faq':[
                          {'q':'How are prices predicted?','a':'Using historical CSV + linear regression. ML upgrade planned.'},
                          {'q':'Is COD available?','a':'Yes, plus Online/UPI/QR.'},
                      ]})
