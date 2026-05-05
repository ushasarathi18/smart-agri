from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Profile
import secrets

@api_view(['POST'])
def register(request):
    d = request.data
    if User.objects.filter(username=d.get('username')).exists():
        return Response({'error':'Username exists'}, status=400)
    u = User.objects.create_user(username=d['username'], email=d.get('email',''),
                                  password=d['password'], first_name=d.get('first_name',''))
    Profile.objects.create(user=u, role=d.get('role','user'), phone=d.get('phone',''),
                            state=d.get('state',''), district=d.get('district',''))
    r = RefreshToken.for_user(u)
    return Response({'access':str(r.access_token),'refresh':str(r),
                      'user':{'id':u.id,'username':u.username,'role':d.get('role','user')}})

@api_view(['POST'])
def login(request):
    u = authenticate(username=request.data.get('username'), password=request.data.get('password'))
    if not u: return Response({'error':'Invalid credentials'}, status=401)
    role = u.profile.role if hasattr(u,'profile') else ('admin' if u.is_superuser else 'user')
    r = RefreshToken.for_user(u)
    return Response({'access':str(r.access_token),'refresh':str(r),
                      'user':{'id':u.id,'username':u.username,'role':role}})

@api_view(['POST'])
def forgot_password(request):
    email = request.data.get('email')
    try: u = User.objects.get(email=email)
    except User.DoesNotExist: return Response({'error':'No user with that email'}, status=404)
    token = secrets.token_urlsafe(16); u.set_password(token); u.save()
    try:
        send_mail('Smart Agri Password Reset', f'Your temporary password: {token}',
                  settings.DEFAULT_FROM_EMAIL, [email], fail_silently=True)
    except Exception: pass
    # TODO: SMS reset placeholder
    return Response({'message':'Temporary password sent (check console/email)','temp_password':token})

@api_view(['POST'])
def reset_password(request):
    u = authenticate(username=request.data.get('username'), password=request.data.get('temp_password'))
    if not u: return Response({'error':'Invalid temp password'}, status=400)
    u.set_password(request.data.get('new_password')); u.save()
    return Response({'message':'Password reset successful'})

@api_view(['GET'])
def profile(request):
    if not request.user.is_authenticated: return Response({'error':'login required'}, status=401)
    p = getattr(request.user,'profile',None)
    return Response({'username':request.user.username,'email':request.user.email,
                      'role':p.role if p else 'user','phone':p.phone if p else '',
                      'state':p.state if p else '','district':p.district if p else '',
                      'verified':p.verified if p else False})
