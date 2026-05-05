from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
import random

# TODO: Replace with real CNN/TensorFlow model for image-based detection
DISEASE_DB = {
    'leaf_spot':{'name':'Leaf Spot','severity':'Medium',
        'pesticide':'Mancozeb 75% WP','dosage':'2g/L water','interval':'7-10 days',
        'organic':'Neem oil spray','precautions':'Avoid overhead irrigation. Remove infected leaves.',
        'prevention':'Crop rotation, resistant varieties.'},
    'rust':{'name':'Rust Disease','severity':'High',
        'pesticide':'Propiconazole 25% EC','dosage':'1ml/L','interval':'10-14 days',
        'organic':'Sulfur dust','precautions':'Wear gloves and mask while spraying.',
        'prevention':'Plant resistant cultivars, ensure airflow.'},
    'blight':{'name':'Late Blight','severity':'Critical',
        'pesticide':'Metalaxyl + Mancozeb','dosage':'2.5g/L','interval':'7 days',
        'organic':'Bordeaux mixture','precautions':'Destroy infected plants.',
        'prevention':'Avoid waterlogging, use certified seeds.'},
    'powdery_mildew':{'name':'Powdery Mildew','severity':'Medium',
        'pesticide':'Sulfur 80% WP','dosage':'3g/L','interval':'10 days',
        'organic':'Milk spray (1:9 with water)','precautions':'Spray in early morning.',
        'prevention':'Proper spacing, prune affected parts.'},
    'healthy':{'name':'Healthy','severity':'None','pesticide':'None needed',
        'dosage':'-','interval':'-','organic':'-',
        'precautions':'Maintain regular care.','prevention':'Continue good practices.'},
}

@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def detect(request):
    img = request.FILES.get('image')
    if not img: return Response({'error':'image required'}, status=400)
    # TODO: Run real ML model on `img`. Currently returns random plausible result.
    key = random.choice(list(DISEASE_DB.keys()))
    res = DISEASE_DB[key]
    confidence = round(random.uniform(78,97),2)
    return Response({'detected':key,'confidence':confidence,'details':res,
                      'note':'Demo mode - integrate TensorFlow/PyTorch CNN for real detection.'})

@api_view(['GET'])
def diseases_list(_):
    return Response([{'key':k,**v} for k,v in DISEASE_DB.items()])
