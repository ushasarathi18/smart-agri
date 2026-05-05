from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view(['GET'])
def services_list(_):
    return Response([
        {'name':'Crop Advisory','desc':'Personalized crop recommendations'},
        {'name':'Soil Testing','desc':'Lab-grade soil analysis'},
        {'name':'Drone Spraying','desc':'On-demand pesticide spraying'},
        {'name':'Equipment Rental','desc':'Tractor & machinery rental'},
        {'name':'Cold Storage','desc':'Warehouse + cold chain'},
    ])
